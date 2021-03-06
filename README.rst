.. vim: set fileencoding=utf-8 :
.. Pavel Korshunov <pavel.korshunov@idiap.ch>
.. Thu 23 Jun 13:43:22 2016

.. image:: https://img.shields.io/badge/docs-available-orange.svg
   :target: https://www.idiap.ch/software/bob/docs/bob/bob.pad.voice/master/index.html
.. image:: https://gitlab.idiap.ch/bob/bob.pad.voice/badges/master/pipeline.svg
   :target: https://gitlab.idiap.ch/bob/bob.pad.voice/commits/master
.. image:: https://gitlab.idiap.ch/bob/bob.pad.voice/badges/master/coverage.svg
   :target: https://gitlab.idiap.ch/bob/bob.pad.voice/commits/master
.. image:: https://img.shields.io/badge/gitlab-project-0000c0.svg
   :target: https://gitlab.idiap.ch/bob/bob.pad.voice

=================================================
Presentation Attack Detection in Voice Biometrics
=================================================

This package is part of the signal-processing and machine learning toolbox
Bob_. This package is an extension to the ``bob.pad.base`` package, which provides the basic presentation attack
detection (PAD) framework.

The ``bob.pad.voice`` contains additional functionality to run PAD experiments using speech databases.
Wrappers for speech databases are also included in this package.


Installation
------------

Follow our `installation`_ instructions. Then, using the Python interpreter
provided by the distribution, bootstrap and buildout this package::

  $ python bootstrap-buildout.py
  $ ./bin/buildout


Contact
-------

For questions or reporting issues to this software package, contact our
development `mailing list`_.


.. Place your references here:
.. _bob: https://www.idiap.ch/software/bob
.. _installation: https://gitlab.idiap.ch/bob/bob/wikis/Installation
.. _mailing list: https://groups.google.com/forum/?fromgroups#!forum/bob-devel
