OpenGL bindings for Python 3
============================

Python bindings for OpenGL 3.x and 4.x. Core profile only.

Slim and fast. Python only. No external dependencies.

It's just a thin `ctypes` wrapper around the OpenGL C API.

This will allow you to crash the Python interpreter! Why leave all the
segfaulting-fun to the C programmers? ;)

* * *

**Python 2 note**: The raw bindings (`from gl.api import *`) actually
works on Python 2. But that is by accident, not by design!

- - -

They are auto-generated from these files:

* <https://www.opengl.org/registry/api/GL/glcorearb.h>
* <https://www.opengl.org/registry/oldspecs/glcorearb.h> (OpenGL 3)

Tested on: Linux (Debian testing).
