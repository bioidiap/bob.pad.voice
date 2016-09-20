
from bob.pad.base.algorithm import Algorithm

import logging
logger = logging.getLogger("bob.pad.voice")

class DummyAlgorithm (Algorithm):
  """This class is used to test all the possible functions of the tool chain, but it does basically nothing."""

  def __init__(self, **kwargs):
    """Generates a test value that is read and written"""

    # call base class constructor registering that this tool performs everything.
    Algorithm.__init__(
        self,
        performs_projection = False,
        requires_projector_training = False,
    )
  
  def score(self, toscore):
    """Returns the evarage value of the probe"""
    logger.info("score() score %f", toscore)
    
    return toscore

algorithm = DummyAlgorithm()
