import ctypes

if getattr (ctypes.CDLL('libGL.so.1'), 'glTextureStorage1D', None) is None:
    from .api3 import *
    version = 3
else:
    from .api4 import *
    version = 4

del ctypes
