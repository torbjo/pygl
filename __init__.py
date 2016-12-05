from .api import *

for i in range (16):
    globals()['TEXUNIT' + str(i)] = i
