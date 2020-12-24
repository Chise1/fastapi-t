__version__ = "0.1.0"
from rearq import ReArq

from src import settings

rearq = ReArq(**settings.REARQ,)
