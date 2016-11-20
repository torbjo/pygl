import ctypes

if getattr (ctypes.CDLL('libGL.so.1'), 'glTextureStorage1D', None):
    from .api4 import *
    version = 4
else:
    from .api3 import *
    version = 3

del ctypes
