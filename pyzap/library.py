from ctypes import cdll
from ctypes.util import find_library

_FILEPATH = find_library('zaplib')
if _FILEPATH is None:
    _FILEPATH = 'libzaplib.so'

instance = cdll.LoadLibrary(_FILEPATH)
