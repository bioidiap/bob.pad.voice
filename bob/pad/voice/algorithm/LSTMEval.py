#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# @author: Pavel Korshunov <pavel.korshunov@idiap.ch>
# @date: Wed 19 Oct 23:43:22 2016

from bob.pad.base.algorithm import Algorithm
import numpy


# import tensorflow as tf

import logging

logger = logging.getLogger("bob.pad.voice")


class LSTMEval(Algorithm):
    """This class is used to test all the possible functions of the tool chain, but it does basically nothing."""

    def __init__(self,
                 input_shape=[200, 81],  # [temporal_length, feature_size]
                 lstm_network_size=60,  # the output size of LSTM cell
                 **kwargs):
        """Generates a test value that is read and written"""

        # call base class constructor registering that this tool performs everything.
        Algorithm.__init__(
            self,
            performs_projection=True,
            requires_projector_training=False,
            **kwargs
        )

        self.input_shape = input_shape
        self.num_time_steps = input_shape[0]
        self.lstm_network_size = lstm_network_size

        self.data_reader = None
        self.session = None
        self.dnn_model = None
        self.data_placeholder = None

#    def __del__(self):
#        self.session.close()

    def simple_lstm_network(self, train_data_shuffler, batch_size=10, lstm_cell_size=64,
                            num_time_steps=28, num_classes=10, seed=10, reuse=False):
        import tensorflow as tf
        from bob.learn.tensorflow.layers import lstm
        slim = tf.contrib.slim

        if isinstance(train_data_shuffler, tf.Tensor):
            inputs = train_data_shuffler
        else:
            inputs = train_data_shuffler("data", from_queue=False)

        initializer = tf.contrib.layers.xavier_initializer(seed=seed)

        # Creating an LSTM network
        graph = lstm(inputs, lstm_cell_size, num_time_steps=num_time_steps, batch_size=batch_size,
                     output_activation_size=num_classes, scope='lstm',
                     weights_initializer=initializer, activation=tf.nn.sigmoid, reuse=reuse)

        # fully connect the LSTM output to the classes
#        graph = slim.fully_connected(graph, num_classes, activation_fn=None, scope='fc1',
#                                     weights_initializer=initializer, reuse=reuse)

        return graph

    def _check_feature(self, feature):
        """Checks that the features are appropriate."""
        if not isinstance(feature, numpy.ndarray) or feature.ndim != 2 or feature.dtype != numpy.float32:
            raise ValueError("The given feature is not appropriate", feature)
        return True

    def restore_trained_model(self, projector_file):
        import tensorflow as tf
        if self.session is None:
            self.session = tf.Session()
        data_pl = tf.placeholder(tf.float32, shape=(None, ) + tuple(self.input_shape))
        graph = self.simple_lstm_network(data_pl, batch_size=1,
                                         lstm_cell_size=self.lstm_network_size, num_time_steps=self.num_time_steps,
                                         num_classes=2, reuse=False)

        self.session.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
#        saver = tf.train.import_meta_graph(projector_file + ".meta", clear_devices=True)
        saver.restore(self.session, projector_file)
        return tf.nn.softmax(graph, name="softmax"), data_pl

    def load_projector(self, projector_file):
        logger.info("Loading pretrained model from {0}".format(projector_file))

        self.dnn_model, self.data_placeholder = self.restore_trained_model(projector_file)

    def project_feature(self, feature):

        logger.info(" .... Projecting %d features vector" % feature.shape[0])
        from bob.learn.tensorflow.datashuffler import DiskAudio
        if not self.data_reader:
            self.data_reader = DiskAudio([0], [0], [1] + self.input_shape)
        # frames, labels = self.data_reader.extract_frames_from_wav(feature, 0)
        frames, labels = self.data_reader.split_features_in_windows(features=feature, label=1,
                                                                    win_size=self.num_time_steps)
#        frames = numpy.asarray(frames)
#        logger.info(" .... And frames of shape {0} are extracted to pass into DNN model".format(frames.shape))
        projections = numpy.zeros((len(frames), 2), dtype=numpy.float32)
        for frame, i in zip(frames, range(len(frames))):
            frame = numpy.reshape(frame, ([1] + list(frames[0].shape)))
#        frames = numpy.reshape(frames, (frames.shape[0], -1, 1))
            logger.info(" .... projecting frame of shape {0} onto DNN model".format(frame.shape))

            if self.session is not None:
                forward_output = self.session.run(self.dnn_model, feed_dict={self.data_placeholder: frame})
                projections[i]=forward_output[0]
            else:
                raise ValueError("Tensorflow session was not initialized, so cannot project on DNN model!")
        logger.info("Projected scores {0}".format(projections))
        return numpy.asarray(projections, dtype=numpy.float32)

    def project(self, feature):
        """project(feature) -> projected

        This function will project the given feature.
        It is assured that the :py:meth:`load_projector` was called once before the ``project`` function is executed.

        **Parameters:**

        feature : object
          The feature to be projected.

        **Returns:**

        projected : object
          The projected features.
          Must be writable with the :py:meth:`write_feature` function and readable with the :py:meth:`read_feature` function.

        """
        if len(feature) > 0:
            feature = numpy.cast['float32'](feature)
            self._check_feature(feature)
            return self.project_feature(feature)
        else:
            return numpy.zeros(1, dtype=numpy.float64)

    def score_for_multiple_projections(self, toscore):
        """scorescore_for_multiple_projections(toscore) -> score

        **Returns:**

        score : float
          A score value for the object ``toscore``.
        """
        scores = numpy.asarray(toscore, dtype=numpy.float32)
        real_scores = scores[:, 1]
        logger.debug("Mean score %f", numpy.mean(real_scores))
        return [numpy.mean(real_scores)]

    def score(self, toscore):
        """Returns the evarage value of the probe"""
        logger.debug("score() score %f", toscore)
        # return only real score
        return [toscore[0]]


algorithm = LSTMEval()
