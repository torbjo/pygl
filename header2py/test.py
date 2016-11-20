r"""
Test against glitter (https://pypi.python.org/pypi/glitter/0.1.7). Will
check that all symbols exists, and that their (ctypes) signature match.

NOTE: glitter needs this patch to work with Python 3:
https://gist.github.com/torbjo/c2ccc681adff2ec73b57a819d963cf5d

See also: make test

BUG: Will not work when API passes a structure. So ignore these:
glFenceSync.restype: missmatch!
glGetSynciv.argtypes: missmatch!
glClientWaitSync.argtypes: missmatch!
glDeleteSync.argtypes: missmatch!
glWaitSync.argtypes: missmatch!
glIsSync.argtypes: missmatch!
"""

import sys
try:
    VERBOSE = sys.argv[1] in ('-v', '--verbose')
except:
    VERBOSE = False

import api3 as api      # glitter has no gl4 support
from glitter import raw

for key,val in raw.__dict__.items():
    if not key.startswith ('gl'): continue
    if key.startswith ('glX'): continue
    if len(key)<3 or not key[2].isupper(): continue
    o = getattr (api, key, None)
    
    if o is None:
        print (key, 'is missing!')
        continue

    if o.restype != val.restype:
        print ('{}.restype: missmatch!'.format (key))
        if VERBOSE:
            print ('  expected:', val.restype)
            print ('       got:', o.restype)

    #if list(o.argtypes) != val.argtypes:
    if not all (map (lambda a,b: a==b, o.argtypes, val.argtypes)):
        print ('{}.argtypes: missmatch!'.format (key))
        if VERBOSE:
            print ('  expected:', val.argtypes)
            print ('       got:', list(o.argtypes))
