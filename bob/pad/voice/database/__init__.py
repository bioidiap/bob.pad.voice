from .database import PadVoiceFile
from .asvspoof import ASVspoofPadDatabase
from .avspoof import AVspoofPadDatabase
from .replay import ReplayPadDatabase
from .replaymobile import ReplayMobilePadDatabase
from .voicepa import VoicePAPadDatabase

# gets sphinx autodoc done right - don't remove it
__all__ = [_ for _ in dir() if not _.startswith('_')]
