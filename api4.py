# This file was auto-generated on 2016-11-20T16:46:30Z from:
# https://www.opengl.org/registry/api/GL/glcorearb.h

from ctypes import *

_gl = CDLL('libGL.so.1')

GLenum = c_uint
GLboolean = c_ubyte
GLbitfield = c_uint
GLchar = c_char
GLbyte = c_byte
GLshort = c_short
GLint = c_int
GLsizei = c_int
GLubyte = c_ubyte
GLushort = c_ushort
GLuint = c_uint
GLhalf = c_ushort
GLfloat = c_float
GLclampf = c_float
GLdouble = c_double
GLclampd = c_double
GLvoid = None

ptrdiff_t = c_long      # assumes sizeof(ptrdiff_t) == sizeof(long)
GLintptr = ptrdiff_t
GLsizeiptr = ptrdiff_t
GLint64 = c_int64
GLuint64 = c_uint64

STRING = c_char_p

class __GLsync (Structure):
    _fields_ = ()
GLsync = POINTER(__GLsync)

# @todo auto-generate these?
STRING = c_char_p
GLDEBUGPROCARB = CFUNCTYPE (None, GLenum, GLenum, GLuint, GLenum, GLsizei, STRING, POINTER(GLvoid))
# GLDEBUGPROCAMD = (GLuint, GLenum, GLenum, GLsizei, const GLchar*, GLvoid*);
GLDEBUGPROCAMD = CFUNCTYPE (GLuint, GLenum, GLenum, GLsizei, STRING, POINTER(GLvoid))
# GLDEBUGPROC         = (GLenum, GLenum, GLuint, GLenum, GLsizei, const GLchar*, GLvoid*);
GLDEBUGPROC = CFUNCTYPE (GLenum, GLenum, GLuint, GLenum, GLsizei, STRING, POINTER(GLvoid))

GL_VERSION_1_0 = 1
glCullFace = _gl.glCullFace
glCullFace.restype = None
glCullFace.argtypes = (GLenum,)

glFrontFace = _gl.glFrontFace
glFrontFace.restype = None
glFrontFace.argtypes = (GLenum,)

glHint = _gl.glHint
glHint.restype = None
glHint.argtypes = (GLenum, GLenum,)

glLineWidth = _gl.glLineWidth
glLineWidth.restype = None
glLineWidth.argtypes = (GLfloat,)

glPointSize = _gl.glPointSize
glPointSize.restype = None
glPointSize.argtypes = (GLfloat,)

glPolygonMode = _gl.glPolygonMode
glPolygonMode.restype = None
glPolygonMode.argtypes = (GLenum, GLenum,)

glScissor = _gl.glScissor
glScissor.restype = None
glScissor.argtypes = (GLint, GLint, GLsizei, GLsizei,)

glTexParameterf = _gl.glTexParameterf
glTexParameterf.restype = None
glTexParameterf.argtypes = (GLenum, GLenum, GLfloat,)

glTexParameterfv = _gl.glTexParameterfv
glTexParameterfv.restype = None
glTexParameterfv.argtypes = (GLenum, GLenum, POINTER(GLfloat),)

glTexParameteri = _gl.glTexParameteri
glTexParameteri.restype = None
glTexParameteri.argtypes = (GLenum, GLenum, GLint,)

glTexParameteriv = _gl.glTexParameteriv
glTexParameteriv.restype = None
glTexParameteriv.argtypes = (GLenum, GLenum, POINTER(GLint),)

glTexImage1D = _gl.glTexImage1D
glTexImage1D.restype = None
glTexImage1D.argtypes = (GLenum, GLint, GLint, GLsizei, GLint, GLenum, GLenum, POINTER(None),)

glTexImage2D = _gl.glTexImage2D
glTexImage2D.restype = None
glTexImage2D.argtypes = (GLenum, GLint, GLint, GLsizei, GLsizei, GLint, GLenum, GLenum, POINTER(None),)

glDrawBuffer = _gl.glDrawBuffer
glDrawBuffer.restype = None
glDrawBuffer.argtypes = (GLenum,)

glClear = _gl.glClear
glClear.restype = None
glClear.argtypes = (GLbitfield,)

glClearColor = _gl.glClearColor
glClearColor.restype = None
glClearColor.argtypes = (GLfloat, GLfloat, GLfloat, GLfloat,)

glClearStencil = _gl.glClearStencil
glClearStencil.restype = None
glClearStencil.argtypes = (GLint,)

glClearDepth = _gl.glClearDepth
glClearDepth.restype = None
glClearDepth.argtypes = (GLdouble,)

glStencilMask = _gl.glStencilMask
glStencilMask.restype = None
glStencilMask.argtypes = (GLuint,)

glColorMask = _gl.glColorMask
glColorMask.restype = None
glColorMask.argtypes = (GLboolean, GLboolean, GLboolean, GLboolean,)

glDepthMask = _gl.glDepthMask
glDepthMask.restype = None
glDepthMask.argtypes = (GLboolean,)

glDisable = _gl.glDisable
glDisable.restype = None
glDisable.argtypes = (GLenum,)

glEnable = _gl.glEnable
glEnable.restype = None
glEnable.argtypes = (GLenum,)

glFinish = _gl.glFinish
glFinish.restype = None
glFinish.argtypes = ()

glFlush = _gl.glFlush
glFlush.restype = None
glFlush.argtypes = ()

glBlendFunc = _gl.glBlendFunc
glBlendFunc.restype = None
glBlendFunc.argtypes = (GLenum, GLenum,)

glLogicOp = _gl.glLogicOp
glLogicOp.restype = None
glLogicOp.argtypes = (GLenum,)

glStencilFunc = _gl.glStencilFunc
glStencilFunc.restype = None
glStencilFunc.argtypes = (GLenum, GLint, GLuint,)

glStencilOp = _gl.glStencilOp
glStencilOp.restype = None
glStencilOp.argtypes = (GLenum, GLenum, GLenum,)

glDepthFunc = _gl.glDepthFunc
glDepthFunc.restype = None
glDepthFunc.argtypes = (GLenum,)

glPixelStoref = _gl.glPixelStoref
glPixelStoref.restype = None
glPixelStoref.argtypes = (GLenum, GLfloat,)

glPixelStorei = _gl.glPixelStorei
glPixelStorei.restype = None
glPixelStorei.argtypes = (GLenum, GLint,)

glReadBuffer = _gl.glReadBuffer
glReadBuffer.restype = None
glReadBuffer.argtypes = (GLenum,)

glReadPixels = _gl.glReadPixels
glReadPixels.restype = None
glReadPixels.argtypes = (GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, POINTER(None),)

glGetBooleanv = _gl.glGetBooleanv
glGetBooleanv.restype = None
glGetBooleanv.argtypes = (GLenum, POINTER(GLboolean),)

glGetDoublev = _gl.glGetDoublev
glGetDoublev.restype = None
glGetDoublev.argtypes = (GLenum, POINTER(GLdouble),)

glGetError = _gl.glGetError
glGetError.restype = GLenum
glGetError.argtypes = ()

glGetFloatv = _gl.glGetFloatv
glGetFloatv.restype = None
glGetFloatv.argtypes = (GLenum, POINTER(GLfloat),)

glGetIntegerv = _gl.glGetIntegerv
glGetIntegerv.restype = None
glGetIntegerv.argtypes = (GLenum, POINTER(GLint),)

glGetString = _gl.glGetString
glGetString.restype = POINTER(GLubyte)
glGetString.argtypes = (GLenum,)

glGetTexImage = _gl.glGetTexImage
glGetTexImage.restype = None
glGetTexImage.argtypes = (GLenum, GLint, GLenum, GLenum, POINTER(None),)

glGetTexParameterfv = _gl.glGetTexParameterfv
glGetTexParameterfv.restype = None
glGetTexParameterfv.argtypes = (GLenum, GLenum, POINTER(GLfloat),)

glGetTexParameteriv = _gl.glGetTexParameteriv
glGetTexParameteriv.restype = None
glGetTexParameteriv.argtypes = (GLenum, GLenum, POINTER(GLint),)

glGetTexLevelParameterfv = _gl.glGetTexLevelParameterfv
glGetTexLevelParameterfv.restype = None
glGetTexLevelParameterfv.argtypes = (GLenum, GLint, GLenum, POINTER(GLfloat),)

glGetTexLevelParameteriv = _gl.glGetTexLevelParameteriv
glGetTexLevelParameteriv.restype = None
glGetTexLevelParameteriv.argtypes = (GLenum, GLint, GLenum, POINTER(GLint),)

glIsEnabled = _gl.glIsEnabled
glIsEnabled.restype = GLboolean
glIsEnabled.argtypes = (GLenum,)

glDepthRange = _gl.glDepthRange
glDepthRange.restype = None
glDepthRange.argtypes = (GLdouble, GLdouble,)

glViewport = _gl.glViewport
glViewport.restype = None
glViewport.argtypes = (GLint, GLint, GLsizei, GLsizei,)

GL_VERSION_1_1 = 1
GL_DEPTH_BUFFER_BIT = 0x00000100
GL_STENCIL_BUFFER_BIT = 0x00000400
GL_COLOR_BUFFER_BIT = 0x00004000
GL_FALSE = 0
GL_TRUE = 1
GL_POINTS = 0x0000
GL_LINES = 0x0001
GL_LINE_LOOP = 0x0002
GL_LINE_STRIP = 0x0003
GL_TRIANGLES = 0x0004
GL_TRIANGLE_STRIP = 0x0005
GL_TRIANGLE_FAN = 0x0006
GL_QUADS = 0x0007
GL_NEVER = 0x0200
GL_LESS = 0x0201
GL_EQUAL = 0x0202
GL_LEQUAL = 0x0203
GL_GREATER = 0x0204
GL_NOTEQUAL = 0x0205
GL_GEQUAL = 0x0206
GL_ALWAYS = 0x0207
GL_ZERO = 0
GL_ONE = 1
GL_SRC_COLOR = 0x0300
GL_ONE_MINUS_SRC_COLOR = 0x0301
GL_SRC_ALPHA = 0x0302
GL_ONE_MINUS_SRC_ALPHA = 0x0303
GL_DST_ALPHA = 0x0304
GL_ONE_MINUS_DST_ALPHA = 0x0305
GL_DST_COLOR = 0x0306
GL_ONE_MINUS_DST_COLOR = 0x0307
GL_SRC_ALPHA_SATURATE = 0x0308
GL_NONE = 0
GL_FRONT_LEFT = 0x0400
GL_FRONT_RIGHT = 0x0401
GL_BACK_LEFT = 0x0402
GL_BACK_RIGHT = 0x0403
GL_FRONT = 0x0404
GL_BACK = 0x0405
GL_LEFT = 0x0406
GL_RIGHT = 0x0407
GL_FRONT_AND_BACK = 0x0408
GL_NO_ERROR = 0
GL_INVALID_ENUM = 0x0500
GL_INVALID_VALUE = 0x0501
GL_INVALID_OPERATION = 0x0502
GL_OUT_OF_MEMORY = 0x0505
GL_CW = 0x0900
GL_CCW = 0x0901
GL_POINT_SIZE = 0x0B11
GL_POINT_SIZE_RANGE = 0x0B12
GL_POINT_SIZE_GRANULARITY = 0x0B13
GL_LINE_SMOOTH = 0x0B20
GL_LINE_WIDTH = 0x0B21
GL_LINE_WIDTH_RANGE = 0x0B22
GL_LINE_WIDTH_GRANULARITY = 0x0B23
GL_POLYGON_MODE = 0x0B40
GL_POLYGON_SMOOTH = 0x0B41
GL_CULL_FACE = 0x0B44
GL_CULL_FACE_MODE = 0x0B45
GL_FRONT_FACE = 0x0B46
GL_DEPTH_RANGE = 0x0B70
GL_DEPTH_TEST = 0x0B71
GL_DEPTH_WRITEMASK = 0x0B72
GL_DEPTH_CLEAR_VALUE = 0x0B73
GL_DEPTH_FUNC = 0x0B74
GL_STENCIL_TEST = 0x0B90
GL_STENCIL_CLEAR_VALUE = 0x0B91
GL_STENCIL_FUNC = 0x0B92
GL_STENCIL_VALUE_MASK = 0x0B93
GL_STENCIL_FAIL = 0x0B94
GL_STENCIL_PASS_DEPTH_FAIL = 0x0B95
GL_STENCIL_PASS_DEPTH_PASS = 0x0B96
GL_STENCIL_REF = 0x0B97
GL_STENCIL_WRITEMASK = 0x0B98
GL_VIEWPORT = 0x0BA2
GL_DITHER = 0x0BD0
GL_BLEND_DST = 0x0BE0
GL_BLEND_SRC = 0x0BE1
GL_BLEND = 0x0BE2
GL_LOGIC_OP_MODE = 0x0BF0
GL_COLOR_LOGIC_OP = 0x0BF2
GL_DRAW_BUFFER = 0x0C01
GL_READ_BUFFER = 0x0C02
GL_SCISSOR_BOX = 0x0C10
GL_SCISSOR_TEST = 0x0C11
GL_COLOR_CLEAR_VALUE = 0x0C22
GL_COLOR_WRITEMASK = 0x0C23
GL_DOUBLEBUFFER = 0x0C32
GL_STEREO = 0x0C33
GL_LINE_SMOOTH_HINT = 0x0C52
GL_POLYGON_SMOOTH_HINT = 0x0C53
GL_UNPACK_SWAP_BYTES = 0x0CF0
GL_UNPACK_LSB_FIRST = 0x0CF1
GL_UNPACK_ROW_LENGTH = 0x0CF2
GL_UNPACK_SKIP_ROWS = 0x0CF3
GL_UNPACK_SKIP_PIXELS = 0x0CF4
GL_UNPACK_ALIGNMENT = 0x0CF5
GL_PACK_SWAP_BYTES = 0x0D00
GL_PACK_LSB_FIRST = 0x0D01
GL_PACK_ROW_LENGTH = 0x0D02
GL_PACK_SKIP_ROWS = 0x0D03
GL_PACK_SKIP_PIXELS = 0x0D04
GL_PACK_ALIGNMENT = 0x0D05
GL_MAX_TEXTURE_SIZE = 0x0D33
GL_MAX_VIEWPORT_DIMS = 0x0D3A
GL_SUBPIXEL_BITS = 0x0D50
GL_TEXTURE_1D = 0x0DE0
GL_TEXTURE_2D = 0x0DE1
GL_POLYGON_OFFSET_UNITS = 0x2A00
GL_POLYGON_OFFSET_POINT = 0x2A01
GL_POLYGON_OFFSET_LINE = 0x2A02
GL_POLYGON_OFFSET_FILL = 0x8037
GL_POLYGON_OFFSET_FACTOR = 0x8038
GL_TEXTURE_BINDING_1D = 0x8068
GL_TEXTURE_BINDING_2D = 0x8069
GL_TEXTURE_WIDTH = 0x1000
GL_TEXTURE_HEIGHT = 0x1001
GL_TEXTURE_INTERNAL_FORMAT = 0x1003
GL_TEXTURE_BORDER_COLOR = 0x1004
GL_TEXTURE_RED_SIZE = 0x805C
GL_TEXTURE_GREEN_SIZE = 0x805D
GL_TEXTURE_BLUE_SIZE = 0x805E
GL_TEXTURE_ALPHA_SIZE = 0x805F
GL_DONT_CARE = 0x1100
GL_FASTEST = 0x1101
GL_NICEST = 0x1102
GL_BYTE = 0x1400
GL_UNSIGNED_BYTE = 0x1401
GL_SHORT = 0x1402
GL_UNSIGNED_SHORT = 0x1403
GL_INT = 0x1404
GL_UNSIGNED_INT = 0x1405
GL_FLOAT = 0x1406
GL_DOUBLE = 0x140A
GL_STACK_OVERFLOW = 0x0503
GL_STACK_UNDERFLOW = 0x0504
GL_CLEAR = 0x1500
GL_AND = 0x1501
GL_AND_REVERSE = 0x1502
GL_COPY = 0x1503
GL_AND_INVERTED = 0x1504
GL_NOOP = 0x1505
GL_XOR = 0x1506
GL_OR = 0x1507
GL_NOR = 0x1508
GL_EQUIV = 0x1509
GL_INVERT = 0x150A
GL_OR_REVERSE = 0x150B
GL_COPY_INVERTED = 0x150C
GL_OR_INVERTED = 0x150D
GL_NAND = 0x150E
GL_SET = 0x150F
GL_TEXTURE = 0x1702
GL_COLOR = 0x1800
GL_DEPTH = 0x1801
GL_STENCIL = 0x1802
GL_STENCIL_INDEX = 0x1901
GL_DEPTH_COMPONENT = 0x1902
GL_RED = 0x1903
GL_GREEN = 0x1904
GL_BLUE = 0x1905
GL_ALPHA = 0x1906
GL_RGB = 0x1907
GL_RGBA = 0x1908
GL_POINT = 0x1B00
GL_LINE = 0x1B01
GL_FILL = 0x1B02
GL_KEEP = 0x1E00
GL_REPLACE = 0x1E01
GL_INCR = 0x1E02
GL_DECR = 0x1E03
GL_VENDOR = 0x1F00
GL_RENDERER = 0x1F01
GL_VERSION = 0x1F02
GL_EXTENSIONS = 0x1F03
GL_NEAREST = 0x2600
GL_LINEAR = 0x2601
GL_NEAREST_MIPMAP_NEAREST = 0x2700
GL_LINEAR_MIPMAP_NEAREST = 0x2701
GL_NEAREST_MIPMAP_LINEAR = 0x2702
GL_LINEAR_MIPMAP_LINEAR = 0x2703
GL_TEXTURE_MAG_FILTER = 0x2800
GL_TEXTURE_MIN_FILTER = 0x2801
GL_TEXTURE_WRAP_S = 0x2802
GL_TEXTURE_WRAP_T = 0x2803
GL_PROXY_TEXTURE_1D = 0x8063
GL_PROXY_TEXTURE_2D = 0x8064
GL_REPEAT = 0x2901
GL_R3_G3_B2 = 0x2A10
GL_RGB4 = 0x804F
GL_RGB5 = 0x8050
GL_RGB8 = 0x8051
GL_RGB10 = 0x8052
GL_RGB12 = 0x8053
GL_RGB16 = 0x8054
GL_RGBA2 = 0x8055
GL_RGBA4 = 0x8056
GL_RGB5_A1 = 0x8057
GL_RGBA8 = 0x8058
GL_RGB10_A2 = 0x8059
GL_RGBA12 = 0x805A
GL_RGBA16 = 0x805B
GL_VERTEX_ARRAY = 0x8074
glDrawArrays = _gl.glDrawArrays
glDrawArrays.restype = None
glDrawArrays.argtypes = (GLenum, GLint, GLsizei,)

glDrawElements = _gl.glDrawElements
glDrawElements.restype = None
glDrawElements.argtypes = (GLenum, GLsizei, GLenum, POINTER(None),)

glGetPointerv = _gl.glGetPointerv
glGetPointerv.restype = None
glGetPointerv.argtypes = (GLenum, POINTER(POINTER(None)),)

glPolygonOffset = _gl.glPolygonOffset
glPolygonOffset.restype = None
glPolygonOffset.argtypes = (GLfloat, GLfloat,)

glCopyTexImage1D = _gl.glCopyTexImage1D
glCopyTexImage1D.restype = None
glCopyTexImage1D.argtypes = (GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLint,)

glCopyTexImage2D = _gl.glCopyTexImage2D
glCopyTexImage2D.restype = None
glCopyTexImage2D.argtypes = (GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLsizei, GLint,)

glCopyTexSubImage1D = _gl.glCopyTexSubImage1D
glCopyTexSubImage1D.restype = None
glCopyTexSubImage1D.argtypes = (GLenum, GLint, GLint, GLint, GLint, GLsizei,)

glCopyTexSubImage2D = _gl.glCopyTexSubImage2D
glCopyTexSubImage2D.restype = None
glCopyTexSubImage2D.argtypes = (GLenum, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei,)

glTexSubImage1D = _gl.glTexSubImage1D
glTexSubImage1D.restype = None
glTexSubImage1D.argtypes = (GLenum, GLint, GLint, GLsizei, GLenum, GLenum, POINTER(None),)

glTexSubImage2D = _gl.glTexSubImage2D
glTexSubImage2D.restype = None
glTexSubImage2D.argtypes = (GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, POINTER(None),)

glBindTexture = _gl.glBindTexture
glBindTexture.restype = None
glBindTexture.argtypes = (GLenum, GLuint,)

glDeleteTextures = _gl.glDeleteTextures
glDeleteTextures.restype = None
glDeleteTextures.argtypes = (GLsizei, POINTER(GLuint),)

glGenTextures = _gl.glGenTextures
glGenTextures.restype = None
glGenTextures.argtypes = (GLsizei, POINTER(GLuint),)

glIsTexture = _gl.glIsTexture
glIsTexture.restype = GLboolean
glIsTexture.argtypes = (GLuint,)

GL_VERSION_1_2 = 1
GL_UNSIGNED_BYTE_3_3_2 = 0x8032
GL_UNSIGNED_SHORT_4_4_4_4 = 0x8033
GL_UNSIGNED_SHORT_5_5_5_1 = 0x8034
GL_UNSIGNED_INT_8_8_8_8 = 0x8035
GL_UNSIGNED_INT_10_10_10_2 = 0x8036
GL_TEXTURE_BINDING_3D = 0x806A
GL_PACK_SKIP_IMAGES = 0x806B
GL_PACK_IMAGE_HEIGHT = 0x806C
GL_UNPACK_SKIP_IMAGES = 0x806D
GL_UNPACK_IMAGE_HEIGHT = 0x806E
GL_TEXTURE_3D = 0x806F
GL_PROXY_TEXTURE_3D = 0x8070
GL_TEXTURE_DEPTH = 0x8071
GL_TEXTURE_WRAP_R = 0x8072
GL_MAX_3D_TEXTURE_SIZE = 0x8073
GL_UNSIGNED_BYTE_2_3_3_REV = 0x8362
GL_UNSIGNED_SHORT_5_6_5 = 0x8363
GL_UNSIGNED_SHORT_5_6_5_REV = 0x8364
GL_UNSIGNED_SHORT_4_4_4_4_REV = 0x8365
GL_UNSIGNED_SHORT_1_5_5_5_REV = 0x8366
GL_UNSIGNED_INT_8_8_8_8_REV = 0x8367
GL_UNSIGNED_INT_2_10_10_10_REV = 0x8368
GL_BGR = 0x80E0
GL_BGRA = 0x80E1
GL_MAX_ELEMENTS_VERTICES = 0x80E8
GL_MAX_ELEMENTS_INDICES = 0x80E9
GL_CLAMP_TO_EDGE = 0x812F
GL_TEXTURE_MIN_LOD = 0x813A
GL_TEXTURE_MAX_LOD = 0x813B
GL_TEXTURE_BASE_LEVEL = 0x813C
GL_TEXTURE_MAX_LEVEL = 0x813D
GL_SMOOTH_POINT_SIZE_RANGE = 0x0B12
GL_SMOOTH_POINT_SIZE_GRANULARITY = 0x0B13
GL_SMOOTH_LINE_WIDTH_RANGE = 0x0B22
GL_SMOOTH_LINE_WIDTH_GRANULARITY = 0x0B23
GL_ALIASED_LINE_WIDTH_RANGE = 0x846E
glDrawRangeElements = _gl.glDrawRangeElements
glDrawRangeElements.restype = None
glDrawRangeElements.argtypes = (GLenum, GLuint, GLuint, GLsizei, GLenum, POINTER(None),)

glTexImage3D = _gl.glTexImage3D
glTexImage3D.restype = None
glTexImage3D.argtypes = (GLenum, GLint, GLint, GLsizei, GLsizei, GLsizei, GLint, GLenum, GLenum, POINTER(None),)

glTexSubImage3D = _gl.glTexSubImage3D
glTexSubImage3D.restype = None
glTexSubImage3D.argtypes = (GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLenum, POINTER(None),)

glCopyTexSubImage3D = _gl.glCopyTexSubImage3D
glCopyTexSubImage3D.restype = None
glCopyTexSubImage3D.argtypes = (GLenum, GLint, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei,)

GL_VERSION_1_3 = 1
GL_TEXTURE0 = 0x84C0
GL_TEXTURE1 = 0x84C1
GL_TEXTURE2 = 0x84C2
GL_TEXTURE3 = 0x84C3
GL_TEXTURE4 = 0x84C4
GL_TEXTURE5 = 0x84C5
GL_TEXTURE6 = 0x84C6
GL_TEXTURE7 = 0x84C7
GL_TEXTURE8 = 0x84C8
GL_TEXTURE9 = 0x84C9
GL_TEXTURE10 = 0x84CA
GL_TEXTURE11 = 0x84CB
GL_TEXTURE12 = 0x84CC
GL_TEXTURE13 = 0x84CD
GL_TEXTURE14 = 0x84CE
GL_TEXTURE15 = 0x84CF
GL_TEXTURE16 = 0x84D0
GL_TEXTURE17 = 0x84D1
GL_TEXTURE18 = 0x84D2
GL_TEXTURE19 = 0x84D3
GL_TEXTURE20 = 0x84D4
GL_TEXTURE21 = 0x84D5
GL_TEXTURE22 = 0x84D6
GL_TEXTURE23 = 0x84D7
GL_TEXTURE24 = 0x84D8
GL_TEXTURE25 = 0x84D9
GL_TEXTURE26 = 0x84DA
GL_TEXTURE27 = 0x84DB
GL_TEXTURE28 = 0x84DC
GL_TEXTURE29 = 0x84DD
GL_TEXTURE30 = 0x84DE
GL_TEXTURE31 = 0x84DF
GL_ACTIVE_TEXTURE = 0x84E0
GL_MULTISAMPLE = 0x809D
GL_SAMPLE_ALPHA_TO_COVERAGE = 0x809E
GL_SAMPLE_ALPHA_TO_ONE = 0x809F
GL_SAMPLE_COVERAGE = 0x80A0
GL_SAMPLE_BUFFERS = 0x80A8
GL_SAMPLES = 0x80A9
GL_SAMPLE_COVERAGE_VALUE = 0x80AA
GL_SAMPLE_COVERAGE_INVERT = 0x80AB
GL_TEXTURE_CUBE_MAP = 0x8513
GL_TEXTURE_BINDING_CUBE_MAP = 0x8514
GL_TEXTURE_CUBE_MAP_POSITIVE_X = 0x8515
GL_TEXTURE_CUBE_MAP_NEGATIVE_X = 0x8516
GL_TEXTURE_CUBE_MAP_POSITIVE_Y = 0x8517
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y = 0x8518
GL_TEXTURE_CUBE_MAP_POSITIVE_Z = 0x8519
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z = 0x851A
GL_PROXY_TEXTURE_CUBE_MAP = 0x851B
GL_MAX_CUBE_MAP_TEXTURE_SIZE = 0x851C
GL_COMPRESSED_RGB = 0x84ED
GL_COMPRESSED_RGBA = 0x84EE
GL_TEXTURE_COMPRESSION_HINT = 0x84EF
GL_TEXTURE_COMPRESSED_IMAGE_SIZE = 0x86A0
GL_TEXTURE_COMPRESSED = 0x86A1
GL_NUM_COMPRESSED_TEXTURE_FORMATS = 0x86A2
GL_COMPRESSED_TEXTURE_FORMATS = 0x86A3
GL_CLAMP_TO_BORDER = 0x812D
glActiveTexture = _gl.glActiveTexture
glActiveTexture.restype = None
glActiveTexture.argtypes = (GLenum,)

glSampleCoverage = _gl.glSampleCoverage
glSampleCoverage.restype = None
glSampleCoverage.argtypes = (GLfloat, GLboolean,)

glCompressedTexImage3D = _gl.glCompressedTexImage3D
glCompressedTexImage3D.restype = None
glCompressedTexImage3D.argtypes = (GLenum, GLint, GLenum, GLsizei, GLsizei, GLsizei, GLint, GLsizei, POINTER(None),)

glCompressedTexImage2D = _gl.glCompressedTexImage2D
glCompressedTexImage2D.restype = None
glCompressedTexImage2D.argtypes = (GLenum, GLint, GLenum, GLsizei, GLsizei, GLint, GLsizei, POINTER(None),)

glCompressedTexImage1D = _gl.glCompressedTexImage1D
glCompressedTexImage1D.restype = None
glCompressedTexImage1D.argtypes = (GLenum, GLint, GLenum, GLsizei, GLint, GLsizei, POINTER(None),)

glCompressedTexSubImage3D = _gl.glCompressedTexSubImage3D
glCompressedTexSubImage3D.restype = None
glCompressedTexSubImage3D.argtypes = (GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLsizei, POINTER(None),)

glCompressedTexSubImage2D = _gl.glCompressedTexSubImage2D
glCompressedTexSubImage2D.restype = None
glCompressedTexSubImage2D.argtypes = (GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLsizei, POINTER(None),)

glCompressedTexSubImage1D = _gl.glCompressedTexSubImage1D
glCompressedTexSubImage1D.restype = None
glCompressedTexSubImage1D.argtypes = (GLenum, GLint, GLint, GLsizei, GLenum, GLsizei, POINTER(None),)

glGetCompressedTexImage = _gl.glGetCompressedTexImage
glGetCompressedTexImage.restype = None
glGetCompressedTexImage.argtypes = (GLenum, GLint, POINTER(None),)

GL_VERSION_1_4 = 1
GL_BLEND_DST_RGB = 0x80C8
GL_BLEND_SRC_RGB = 0x80C9
GL_BLEND_DST_ALPHA = 0x80CA
GL_BLEND_SRC_ALPHA = 0x80CB
GL_POINT_FADE_THRESHOLD_SIZE = 0x8128
GL_DEPTH_COMPONENT16 = 0x81A5
GL_DEPTH_COMPONENT24 = 0x81A6
GL_DEPTH_COMPONENT32 = 0x81A7
GL_MIRRORED_REPEAT = 0x8370
GL_MAX_TEXTURE_LOD_BIAS = 0x84FD
GL_TEXTURE_LOD_BIAS = 0x8501
GL_INCR_WRAP = 0x8507
GL_DECR_WRAP = 0x8508
GL_TEXTURE_DEPTH_SIZE = 0x884A
GL_TEXTURE_COMPARE_MODE = 0x884C
GL_TEXTURE_COMPARE_FUNC = 0x884D
GL_FUNC_ADD = 0x8006
GL_FUNC_SUBTRACT = 0x800A
GL_FUNC_REVERSE_SUBTRACT = 0x800B
GL_MIN = 0x8007
GL_MAX = 0x8008
GL_CONSTANT_COLOR = 0x8001
GL_ONE_MINUS_CONSTANT_COLOR = 0x8002
GL_CONSTANT_ALPHA = 0x8003
GL_ONE_MINUS_CONSTANT_ALPHA = 0x8004
glBlendFuncSeparate = _gl.glBlendFuncSeparate
glBlendFuncSeparate.restype = None
glBlendFuncSeparate.argtypes = (GLenum, GLenum, GLenum, GLenum,)

glMultiDrawArrays = _gl.glMultiDrawArrays
glMultiDrawArrays.restype = None
glMultiDrawArrays.argtypes = (GLenum, POINTER(GLint), POINTER(GLsizei), GLsizei,)

glMultiDrawElements = _gl.glMultiDrawElements
glMultiDrawElements.restype = None
glMultiDrawElements.argtypes = (GLenum, POINTER(GLsizei), GLenum, POINTER(POINTER(None)), GLsizei,)

glPointParameterf = _gl.glPointParameterf
glPointParameterf.restype = None
glPointParameterf.argtypes = (GLenum, GLfloat,)

glPointParameterfv = _gl.glPointParameterfv
glPointParameterfv.restype = None
glPointParameterfv.argtypes = (GLenum, POINTER(GLfloat),)

glPointParameteri = _gl.glPointParameteri
glPointParameteri.restype = None
glPointParameteri.argtypes = (GLenum, GLint,)

glPointParameteriv = _gl.glPointParameteriv
glPointParameteriv.restype = None
glPointParameteriv.argtypes = (GLenum, POINTER(GLint),)

glBlendColor = _gl.glBlendColor
glBlendColor.restype = None
glBlendColor.argtypes = (GLfloat, GLfloat, GLfloat, GLfloat,)

glBlendEquation = _gl.glBlendEquation
glBlendEquation.restype = None
glBlendEquation.argtypes = (GLenum,)

GL_VERSION_1_5 = 1
GL_BUFFER_SIZE = 0x8764
GL_BUFFER_USAGE = 0x8765
GL_QUERY_COUNTER_BITS = 0x8864
GL_CURRENT_QUERY = 0x8865
GL_QUERY_RESULT = 0x8866
GL_QUERY_RESULT_AVAILABLE = 0x8867
GL_ARRAY_BUFFER = 0x8892
GL_ELEMENT_ARRAY_BUFFER = 0x8893
GL_ARRAY_BUFFER_BINDING = 0x8894
GL_ELEMENT_ARRAY_BUFFER_BINDING = 0x8895
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING = 0x889F
GL_READ_ONLY = 0x88B8
GL_WRITE_ONLY = 0x88B9
GL_READ_WRITE = 0x88BA
GL_BUFFER_ACCESS = 0x88BB
GL_BUFFER_MAPPED = 0x88BC
GL_BUFFER_MAP_POINTER = 0x88BD
GL_STREAM_DRAW = 0x88E0
GL_STREAM_READ = 0x88E1
GL_STREAM_COPY = 0x88E2
GL_STATIC_DRAW = 0x88E4
GL_STATIC_READ = 0x88E5
GL_STATIC_COPY = 0x88E6
GL_DYNAMIC_DRAW = 0x88E8
GL_DYNAMIC_READ = 0x88E9
GL_DYNAMIC_COPY = 0x88EA
GL_SAMPLES_PASSED = 0x8914
GL_SRC1_ALPHA = 0x8589
glGenQueries = _gl.glGenQueries
glGenQueries.restype = None
glGenQueries.argtypes = (GLsizei, POINTER(GLuint),)

glDeleteQueries = _gl.glDeleteQueries
glDeleteQueries.restype = None
glDeleteQueries.argtypes = (GLsizei, POINTER(GLuint),)

glIsQuery = _gl.glIsQuery
glIsQuery.restype = GLboolean
glIsQuery.argtypes = (GLuint,)

glBeginQuery = _gl.glBeginQuery
glBeginQuery.restype = None
glBeginQuery.argtypes = (GLenum, GLuint,)

glEndQuery = _gl.glEndQuery
glEndQuery.restype = None
glEndQuery.argtypes = (GLenum,)

glGetQueryiv = _gl.glGetQueryiv
glGetQueryiv.restype = None
glGetQueryiv.argtypes = (GLenum, GLenum, POINTER(GLint),)

glGetQueryObjectiv = _gl.glGetQueryObjectiv
glGetQueryObjectiv.restype = None
glGetQueryObjectiv.argtypes = (GLuint, GLenum, POINTER(GLint),)

glGetQueryObjectuiv = _gl.glGetQueryObjectuiv
glGetQueryObjectuiv.restype = None
glGetQueryObjectuiv.argtypes = (GLuint, GLenum, POINTER(GLuint),)

glBindBuffer = _gl.glBindBuffer
glBindBuffer.restype = None
glBindBuffer.argtypes = (GLenum, GLuint,)

glDeleteBuffers = _gl.glDeleteBuffers
glDeleteBuffers.restype = None
glDeleteBuffers.argtypes = (GLsizei, POINTER(GLuint),)

glGenBuffers = _gl.glGenBuffers
glGenBuffers.restype = None
glGenBuffers.argtypes = (GLsizei, POINTER(GLuint),)

glIsBuffer = _gl.glIsBuffer
glIsBuffer.restype = GLboolean
glIsBuffer.argtypes = (GLuint,)

glBufferData = _gl.glBufferData
glBufferData.restype = None
glBufferData.argtypes = (GLenum, GLsizeiptr, POINTER(None), GLenum,)

glBufferSubData = _gl.glBufferSubData
glBufferSubData.restype = None
glBufferSubData.argtypes = (GLenum, GLintptr, GLsizeiptr, POINTER(None),)

glGetBufferSubData = _gl.glGetBufferSubData
glGetBufferSubData.restype = None
glGetBufferSubData.argtypes = (GLenum, GLintptr, GLsizeiptr, POINTER(None),)

glMapBuffer = _gl.glMapBuffer
glMapBuffer.restype = POINTER(None)
glMapBuffer.argtypes = (GLenum, GLenum,)

glUnmapBuffer = _gl.glUnmapBuffer
glUnmapBuffer.restype = GLboolean
glUnmapBuffer.argtypes = (GLenum,)

glGetBufferParameteriv = _gl.glGetBufferParameteriv
glGetBufferParameteriv.restype = None
glGetBufferParameteriv.argtypes = (GLenum, GLenum, POINTER(GLint),)

glGetBufferPointerv = _gl.glGetBufferPointerv
glGetBufferPointerv.restype = None
glGetBufferPointerv.argtypes = (GLenum, GLenum, POINTER(POINTER(None)),)

GL_VERSION_2_0 = 1
GL_BLEND_EQUATION_RGB = 0x8009
GL_VERTEX_ATTRIB_ARRAY_ENABLED = 0x8622
GL_VERTEX_ATTRIB_ARRAY_SIZE = 0x8623
GL_VERTEX_ATTRIB_ARRAY_STRIDE = 0x8624
GL_VERTEX_ATTRIB_ARRAY_TYPE = 0x8625
GL_CURRENT_VERTEX_ATTRIB = 0x8626
GL_VERTEX_PROGRAM_POINT_SIZE = 0x8642
GL_VERTEX_ATTRIB_ARRAY_POINTER = 0x8645
GL_STENCIL_BACK_FUNC = 0x8800
GL_STENCIL_BACK_FAIL = 0x8801
GL_STENCIL_BACK_PASS_DEPTH_FAIL = 0x8802
GL_STENCIL_BACK_PASS_DEPTH_PASS = 0x8803
GL_MAX_DRAW_BUFFERS = 0x8824
GL_DRAW_BUFFER0 = 0x8825
GL_DRAW_BUFFER1 = 0x8826
GL_DRAW_BUFFER2 = 0x8827
GL_DRAW_BUFFER3 = 0x8828
GL_DRAW_BUFFER4 = 0x8829
GL_DRAW_BUFFER5 = 0x882A
GL_DRAW_BUFFER6 = 0x882B
GL_DRAW_BUFFER7 = 0x882C
GL_DRAW_BUFFER8 = 0x882D
GL_DRAW_BUFFER9 = 0x882E
GL_DRAW_BUFFER10 = 0x882F
GL_DRAW_BUFFER11 = 0x8830
GL_DRAW_BUFFER12 = 0x8831
GL_DRAW_BUFFER13 = 0x8832
GL_DRAW_BUFFER14 = 0x8833
GL_DRAW_BUFFER15 = 0x8834
GL_BLEND_EQUATION_ALPHA = 0x883D
GL_MAX_VERTEX_ATTRIBS = 0x8869
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED = 0x886A
GL_MAX_TEXTURE_IMAGE_UNITS = 0x8872
GL_FRAGMENT_SHADER = 0x8B30
GL_VERTEX_SHADER = 0x8B31
GL_MAX_FRAGMENT_UNIFORM_COMPONENTS = 0x8B49
GL_MAX_VERTEX_UNIFORM_COMPONENTS = 0x8B4A
GL_MAX_VARYING_FLOATS = 0x8B4B
GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS = 0x8B4C
GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS = 0x8B4D
GL_SHADER_TYPE = 0x8B4F
GL_FLOAT_VEC2 = 0x8B50
GL_FLOAT_VEC3 = 0x8B51
GL_FLOAT_VEC4 = 0x8B52
GL_INT_VEC2 = 0x8B53
GL_INT_VEC3 = 0x8B54
GL_INT_VEC4 = 0x8B55
GL_BOOL = 0x8B56
GL_BOOL_VEC2 = 0x8B57
GL_BOOL_VEC3 = 0x8B58
GL_BOOL_VEC4 = 0x8B59
GL_FLOAT_MAT2 = 0x8B5A
GL_FLOAT_MAT3 = 0x8B5B
GL_FLOAT_MAT4 = 0x8B5C
GL_SAMPLER_1D = 0x8B5D
GL_SAMPLER_2D = 0x8B5E
GL_SAMPLER_3D = 0x8B5F
GL_SAMPLER_CUBE = 0x8B60
GL_SAMPLER_1D_SHADOW = 0x8B61
GL_SAMPLER_2D_SHADOW = 0x8B62
GL_DELETE_STATUS = 0x8B80
GL_COMPILE_STATUS = 0x8B81
GL_LINK_STATUS = 0x8B82
GL_VALIDATE_STATUS = 0x8B83
GL_INFO_LOG_LENGTH = 0x8B84
GL_ATTACHED_SHADERS = 0x8B85
GL_ACTIVE_UNIFORMS = 0x8B86
GL_ACTIVE_UNIFORM_MAX_LENGTH = 0x8B87
GL_SHADER_SOURCE_LENGTH = 0x8B88
GL_ACTIVE_ATTRIBUTES = 0x8B89
GL_ACTIVE_ATTRIBUTE_MAX_LENGTH = 0x8B8A
GL_FRAGMENT_SHADER_DERIVATIVE_HINT = 0x8B8B
GL_SHADING_LANGUAGE_VERSION = 0x8B8C
GL_CURRENT_PROGRAM = 0x8B8D
GL_POINT_SPRITE_COORD_ORIGIN = 0x8CA0
GL_LOWER_LEFT = 0x8CA1
GL_UPPER_LEFT = 0x8CA2
GL_STENCIL_BACK_REF = 0x8CA3
GL_STENCIL_BACK_VALUE_MASK = 0x8CA4
GL_STENCIL_BACK_WRITEMASK = 0x8CA5
glBlendEquationSeparate = _gl.glBlendEquationSeparate
glBlendEquationSeparate.restype = None
glBlendEquationSeparate.argtypes = (GLenum, GLenum,)

glDrawBuffers = _gl.glDrawBuffers
glDrawBuffers.restype = None
glDrawBuffers.argtypes = (GLsizei, POINTER(GLenum),)

glStencilOpSeparate = _gl.glStencilOpSeparate
glStencilOpSeparate.restype = None
glStencilOpSeparate.argtypes = (GLenum, GLenum, GLenum, GLenum,)

glStencilFuncSeparate = _gl.glStencilFuncSeparate
glStencilFuncSeparate.restype = None
glStencilFuncSeparate.argtypes = (GLenum, GLenum, GLint, GLuint,)

glStencilMaskSeparate = _gl.glStencilMaskSeparate
glStencilMaskSeparate.restype = None
glStencilMaskSeparate.argtypes = (GLenum, GLuint,)

glAttachShader = _gl.glAttachShader
glAttachShader.restype = None
glAttachShader.argtypes = (GLuint, GLuint,)

glBindAttribLocation = _gl.glBindAttribLocation
glBindAttribLocation.restype = None
glBindAttribLocation.argtypes = (GLuint, GLuint, STRING,)

glCompileShader = _gl.glCompileShader
glCompileShader.restype = None
glCompileShader.argtypes = (GLuint,)

glCreateProgram = _gl.glCreateProgram
glCreateProgram.restype = GLuint
glCreateProgram.argtypes = ()

glCreateShader = _gl.glCreateShader
glCreateShader.restype = GLuint
glCreateShader.argtypes = (GLenum,)

glDeleteProgram = _gl.glDeleteProgram
glDeleteProgram.restype = None
glDeleteProgram.argtypes = (GLuint,)

glDeleteShader = _gl.glDeleteShader
glDeleteShader.restype = None
glDeleteShader.argtypes = (GLuint,)

glDetachShader = _gl.glDetachShader
glDetachShader.restype = None
glDetachShader.argtypes = (GLuint, GLuint,)

glDisableVertexAttribArray = _gl.glDisableVertexAttribArray
glDisableVertexAttribArray.restype = None
glDisableVertexAttribArray.argtypes = (GLuint,)

glEnableVertexAttribArray = _gl.glEnableVertexAttribArray
glEnableVertexAttribArray.restype = None
glEnableVertexAttribArray.argtypes = (GLuint,)

glGetActiveAttrib = _gl.glGetActiveAttrib
glGetActiveAttrib.restype = None
glGetActiveAttrib.argtypes = (GLuint, GLuint, GLsizei, POINTER(GLsizei), POINTER(GLint), POINTER(GLenum), STRING,)

glGetActiveUniform = _gl.glGetActiveUniform
glGetActiveUniform.restype = None
glGetActiveUniform.argtypes = (GLuint, GLuint, GLsizei, POINTER(GLsizei), POINTER(GLint), POINTER(GLenum), STRING,)

glGetAttachedShaders = _gl.glGetAttachedShaders
glGetAttachedShaders.restype = None
glGetAttachedShaders.argtypes = (GLuint, GLsizei, POINTER(GLsizei), POINTER(GLuint),)

glGetAttribLocation = _gl.glGetAttribLocation
glGetAttribLocation.restype = GLint
glGetAttribLocation.argtypes = (GLuint, STRING,)

glGetProgramiv = _gl.glGetProgramiv
glGetProgramiv.restype = None
glGetProgramiv.argtypes = (GLuint, GLenum, POINTER(GLint),)

glGetProgramInfoLog = _gl.glGetProgramInfoLog
glGetProgramInfoLog.restype = None
glGetProgramInfoLog.argtypes = (GLuint, GLsizei, POINTER(GLsizei), STRING,)

glGetShaderiv = _gl.glGetShaderiv
glGetShaderiv.restype = None
glGetShaderiv.argtypes = (GLuint, GLenum, POINTER(GLint),)

glGetShaderInfoLog = _gl.glGetShaderInfoLog
glGetShaderInfoLog.restype = None
glGetShaderInfoLog.argtypes = (GLuint, GLsizei, POINTER(GLsizei), STRING,)

glGetShaderSource = _gl.glGetShaderSource
glGetShaderSource.restype = None
glGetShaderSource.argtypes = (GLuint, GLsizei, POINTER(GLsizei), STRING,)

glGetUniformLocation = _gl.glGetUniformLocation
glGetUniformLocation.restype = GLint
glGetUniformLocation.argtypes = (GLuint, STRING,)

glGetUniformfv = _gl.glGetUniformfv
glGetUniformfv.restype = None
glGetUniformfv.argtypes = (GLuint, GLint, POINTER(GLfloat),)

glGetUniformiv = _gl.glGetUniformiv
glGetUniformiv.restype = None
glGetUniformiv.argtypes = (GLuint, GLint, POINTER(GLint),)

glGetVertexAttribdv = _gl.glGetVertexAttribdv
glGetVertexAttribdv.restype = None
glGetVertexAttribdv.argtypes = (GLuint, GLenum, POINTER(GLdouble),)

glGetVertexAttribfv = _gl.glGetVertexAttribfv
glGetVertexAttribfv.restype = None
glGetVertexAttribfv.argtypes = (GLuint, GLenum, POINTER(GLfloat),)

glGetVertexAttribiv = _gl.glGetVertexAttribiv
glGetVertexAttribiv.restype = None
glGetVertexAttribiv.argtypes = (GLuint, GLenum, POINTER(GLint),)

glGetVertexAttribPointerv = _gl.glGetVertexAttribPointerv
glGetVertexAttribPointerv.restype = None
glGetVertexAttribPointerv.argtypes = (GLuint, GLenum, POINTER(POINTER(None)),)

glIsProgram = _gl.glIsProgram
glIsProgram.restype = GLboolean
glIsProgram.argtypes = (GLuint,)

glIsShader = _gl.glIsShader
glIsShader.restype = GLboolean
glIsShader.argtypes = (GLuint,)

glLinkProgram = _gl.glLinkProgram
glLinkProgram.restype = None
glLinkProgram.argtypes = (GLuint,)

glShaderSource = _gl.glShaderSource
glShaderSource.restype = None
glShaderSource.argtypes = (GLuint, GLsizei, POINTER(STRING), POINTER(GLint),)

glUseProgram = _gl.glUseProgram
glUseProgram.restype = None
glUseProgram.argtypes = (GLuint,)

glUniform1f = _gl.glUniform1f
glUniform1f.restype = None
glUniform1f.argtypes = (GLint, GLfloat,)

glUniform2f = _gl.glUniform2f
glUniform2f.restype = None
glUniform2f.argtypes = (GLint, GLfloat, GLfloat,)

glUniform3f = _gl.glUniform3f
glUniform3f.restype = None
glUniform3f.argtypes = (GLint, GLfloat, GLfloat, GLfloat,)

glUniform4f = _gl.glUniform4f
glUniform4f.restype = None
glUniform4f.argtypes = (GLint, GLfloat, GLfloat, GLfloat, GLfloat,)

glUniform1i = _gl.glUniform1i
glUniform1i.restype = None
glUniform1i.argtypes = (GLint, GLint,)

glUniform2i = _gl.glUniform2i
glUniform2i.restype = None
glUniform2i.argtypes = (GLint, GLint, GLint,)

glUniform3i = _gl.glUniform3i
glUniform3i.restype = None
glUniform3i.argtypes = (GLint, GLint, GLint, GLint,)

glUniform4i = _gl.glUniform4i
glUniform4i.restype = None
glUniform4i.argtypes = (GLint, GLint, GLint, GLint, GLint,)

glUniform1fv = _gl.glUniform1fv
glUniform1fv.restype = None
glUniform1fv.argtypes = (GLint, GLsizei, POINTER(GLfloat),)

glUniform2fv = _gl.glUniform2fv
glUniform2fv.restype = None
glUniform2fv.argtypes = (GLint, GLsizei, POINTER(GLfloat),)

glUniform3fv = _gl.glUniform3fv
glUniform3fv.restype = None
glUniform3fv.argtypes = (GLint, GLsizei, POINTER(GLfloat),)

glUniform4fv = _gl.glUniform4fv
glUniform4fv.restype = None
glUniform4fv.argtypes = (GLint, GLsizei, POINTER(GLfloat),)

glUniform1iv = _gl.glUniform1iv
glUniform1iv.restype = None
glUniform1iv.argtypes = (GLint, GLsizei, POINTER(GLint),)

glUniform2iv = _gl.glUniform2iv
glUniform2iv.restype = None
glUniform2iv.argtypes = (GLint, GLsizei, POINTER(GLint),)

glUniform3iv = _gl.glUniform3iv
glUniform3iv.restype = None
glUniform3iv.argtypes = (GLint, GLsizei, POINTER(GLint),)

glUniform4iv = _gl.glUniform4iv
glUniform4iv.restype = None
glUniform4iv.argtypes = (GLint, GLsizei, POINTER(GLint),)

glUniformMatrix2fv = _gl.glUniformMatrix2fv
glUniformMatrix2fv.restype = None
glUniformMatrix2fv.argtypes = (GLint, GLsizei, GLboolean, POINTER(GLfloat),)

glUniformMatrix3fv = _gl.glUniformMatrix3fv
glUniformMatrix3fv.restype = None
glUniformMatrix3fv.argtypes = (GLint, GLsizei, GLboolean, POINTER(GLfloat),)

glUniformMatrix4fv = _gl.glUniformMatrix4fv
glUniformMatrix4fv.restype = None
glUniformMatrix4fv.argtypes = (GLint, GLsizei, GLboolean, POINTER(GLfloat),)

glValidateProgram = _gl.glValidateProgram
glValidateProgram.restype = None
glValidateProgram.argtypes = (GLuint,)

glVertexAttrib1d = _gl.glVertexAttrib1d
glVertexAttrib1d.restype = None
glVertexAttrib1d.argtypes = (GLuint, GLdouble,)

glVertexAttrib1dv = _gl.glVertexAttrib1dv
glVertexAttrib1dv.restype = None
glVertexAttrib1dv.argtypes = (GLuint, POINTER(GLdouble),)

glVertexAttrib1f = _gl.glVertexAttrib1f
glVertexAttrib1f.restype = None
glVertexAttrib1f.argtypes = (GLuint, GLfloat,)

glVertexAttrib1fv = _gl.glVertexAttrib1fv
glVertexAttrib1fv.restype = None
glVertexAttrib1fv.argtypes = (GLuint, POINTER(GLfloat),)

glVertexAttrib1s = _gl.glVertexAttrib1s
glVertexAttrib1s.restype = None
glVertexAttrib1s.argtypes = (GLuint, GLshort,)

glVertexAttrib1sv = _gl.glVertexAttrib1sv
glVertexAttrib1sv.restype = None
glVertexAttrib1sv.argtypes = (GLuint, POINTER(GLshort),)

glVertexAttrib2d = _gl.glVertexAttrib2d
glVertexAttrib2d.restype = None
glVertexAttrib2d.argtypes = (GLuint, GLdouble, GLdouble,)

glVertexAttrib2dv = _gl.glVertexAttrib2dv
glVertexAttrib2dv.restype = None
glVertexAttrib2dv.argtypes = (GLuint, POINTER(GLdouble),)

glVertexAttrib2f = _gl.glVertexAttrib2f
glVertexAttrib2f.restype = None
glVertexAttrib2f.argtypes = (GLuint, GLfloat, GLfloat,)

glVertexAttrib2fv = _gl.glVertexAttrib2fv
glVertexAttrib2fv.restype = None
glVertexAttrib2fv.argtypes = (GLuint, POINTER(GLfloat),)

glVertexAttrib2s = _gl.glVertexAttrib2s
glVertexAttrib2s.restype = None
glVertexAttrib2s.argtypes = (GLuint, GLshort, GLshort,)

glVertexAttrib2sv = _gl.glVertexAttrib2sv
glVertexAttrib2sv.restype = None
glVertexAttrib2sv.argtypes = (GLuint, POINTER(GLshort),)

glVertexAttrib3d = _gl.glVertexAttrib3d
glVertexAttrib3d.restype = None
glVertexAttrib3d.argtypes = (GLuint, GLdouble, GLdouble, GLdouble,)

glVertexAttrib3dv = _gl.glVertexAttrib3dv
glVertexAttrib3dv.restype = None
glVertexAttrib3dv.argtypes = (GLuint, POINTER(GLdouble),)

glVertexAttrib3f = _gl.glVertexAttrib3f
glVertexAttrib3f.restype = None
glVertexAttrib3f.argtypes = (GLuint, GLfloat, GLfloat, GLfloat,)

glVertexAttrib3fv = _gl.glVertexAttrib3fv
glVertexAttrib3fv.restype = None
glVertexAttrib3fv.argtypes = (GLuint, POINTER(GLfloat),)

glVertexAttrib3s = _gl.glVertexAttrib3s
glVertexAttrib3s.restype = None
glVertexAttrib3s.argtypes = (GLuint, GLshort, GLshort, GLshort,)

glVertexAttrib3sv = _gl.glVertexAttrib3sv
glVertexAttrib3sv.restype = None
glVertexAttrib3sv.argtypes = (GLuint, POINTER(GLshort),)

glVertexAttrib4Nbv = _gl.glVertexAttrib4Nbv
glVertexAttrib4Nbv.restype = None
glVertexAttrib4Nbv.argtypes = (GLuint, POINTER(GLbyte),)

glVertexAttrib4Niv = _gl.glVertexAttrib4Niv
glVertexAttrib4Niv.restype = None
glVertexAttrib4Niv.argtypes = (GLuint, POINTER(GLint),)

glVertexAttrib4Nsv = _gl.glVertexAttrib4Nsv
glVertexAttrib4Nsv.restype = None
glVertexAttrib4Nsv.argtypes = (GLuint, POINTER(GLshort),)

glVertexAttrib4Nub = _gl.glVertexAttrib4Nub
glVertexAttrib4Nub.restype = None
glVertexAttrib4Nub.argtypes = (GLuint, GLubyte, GLubyte, GLubyte, GLubyte,)

glVertexAttrib4Nubv = _gl.glVertexAttrib4Nubv
glVertexAttrib4Nubv.restype = None
glVertexAttrib4Nubv.argtypes = (GLuint, POINTER(GLubyte),)

glVertexAttrib4Nuiv = _gl.glVertexAttrib4Nuiv
glVertexAttrib4Nuiv.restype = None
glVertexAttrib4Nuiv.argtypes = (GLuint, POINTER(GLuint),)

glVertexAttrib4Nusv = _gl.glVertexAttrib4Nusv
glVertexAttrib4Nusv.restype = None
glVertexAttrib4Nusv.argtypes = (GLuint, POINTER(GLushort),)

glVertexAttrib4bv = _gl.glVertexAttrib4bv
glVertexAttrib4bv.restype = None
glVertexAttrib4bv.argtypes = (GLuint, POINTER(GLbyte),)

glVertexAttrib4d = _gl.glVertexAttrib4d
glVertexAttrib4d.restype = None
glVertexAttrib4d.argtypes = (GLuint, GLdouble, GLdouble, GLdouble, GLdouble,)

glVertexAttrib4dv = _gl.glVertexAttrib4dv
glVertexAttrib4dv.restype = None
glVertexAttrib4dv.argtypes = (GLuint, POINTER(GLdouble),)

glVertexAttrib4f = _gl.glVertexAttrib4f
glVertexAttrib4f.restype = None
glVertexAttrib4f.argtypes = (GLuint, GLfloat, GLfloat, GLfloat, GLfloat,)

glVertexAttrib4fv = _gl.glVertexAttrib4fv
glVertexAttrib4fv.restype = None
glVertexAttrib4fv.argtypes = (GLuint, POINTER(GLfloat),)

glVertexAttrib4iv = _gl.glVertexAttrib4iv
glVertexAttrib4iv.restype = None
glVertexAttrib4iv.argtypes = (GLuint, POINTER(GLint),)

glVertexAttrib4s = _gl.glVertexAttrib4s
glVertexAttrib4s.restype = None
glVertexAttrib4s.argtypes = (GLuint, GLshort, GLshort, GLshort, GLshort,)

glVertexAttrib4sv = _gl.glVertexAttrib4sv
glVertexAttrib4sv.restype = None
glVertexAttrib4sv.argtypes = (GLuint, POINTER(GLshort),)

glVertexAttrib4ubv = _gl.glVertexAttrib4ubv
glVertexAttrib4ubv.restype = None
glVertexAttrib4ubv.argtypes = (GLuint, POINTER(GLubyte),)

glVertexAttrib4uiv = _gl.glVertexAttrib4uiv
glVertexAttrib4uiv.restype = None
glVertexAttrib4uiv.argtypes = (GLuint, POINTER(GLuint),)

glVertexAttrib4usv = _gl.glVertexAttrib4usv
glVertexAttrib4usv.restype = None
glVertexAttrib4usv.argtypes = (GLuint, POINTER(GLushort),)

glVertexAttribPointer = _gl.glVertexAttribPointer
glVertexAttribPointer.restype = None
glVertexAttribPointer.argtypes = (GLuint, GLint, GLenum, GLboolean, GLsizei, POINTER(None),)

GL_VERSION_2_1 = 1
GL_PIXEL_PACK_BUFFER = 0x88EB
GL_PIXEL_UNPACK_BUFFER = 0x88EC
GL_PIXEL_PACK_BUFFER_BINDING = 0x88ED
GL_PIXEL_UNPACK_BUFFER_BINDING = 0x88EF
GL_FLOAT_MAT2x3 = 0x8B65
GL_FLOAT_MAT2x4 = 0x8B66
GL_FLOAT_MAT3x2 = 0x8B67
GL_FLOAT_MAT3x4 = 0x8B68
GL_FLOAT_MAT4x2 = 0x8B69
GL_FLOAT_MAT4x3 = 0x8B6A
GL_SRGB = 0x8C40
GL_SRGB8 = 0x8C41
GL_SRGB_ALPHA = 0x8C42
GL_SRGB8_ALPHA8 = 0x8C43
GL_COMPRESSED_SRGB = 0x8C48
GL_COMPRESSED_SRGB_ALPHA = 0x8C49
glUniformMatrix2x3fv = _gl.glUniformMatrix2x3fv
glUniformMatrix2x3fv.restype = None
glUniformMatrix2x3fv.argtypes = (GLint, GLsizei, GLboolean, POINTER(GLfloat),)

glUniformMatrix3x2fv = _gl.glUniformMatrix3x2fv
glUniformMatrix3x2fv.restype = None
glUniformMatrix3x2fv.argtypes = (GLint, GLsizei, GLboolean, POINTER(GLfloat),)

glUniformMatrix2x4fv = _gl.glUniformMatrix2x4fv
glUniformMatrix2x4fv.restype = None
glUniformMatrix2x4fv.argtypes = (GLint, GLsizei, GLboolean, POINTER(GLfloat),)

glUniformMatrix4x2fv = _gl.glUniformMatrix4x2fv
glUniformMatrix4x2fv.restype = None
glUniformMatrix4x2fv.argtypes = (GLint, GLsizei, GLboolean, POINTER(GLfloat),)

glUniformMatrix3x4fv = _gl.glUniformMatrix3x4fv
glUniformMatrix3x4fv.restype = None
glUniformMatrix3x4fv.argtypes = (GLint, GLsizei, GLboolean, POINTER(GLfloat),)

glUniformMatrix4x3fv = _gl.glUniformMatrix4x3fv
glUniformMatrix4x3fv.restype = None
glUniformMatrix4x3fv.argtypes = (GLint, GLsizei, GLboolean, POINTER(GLfloat),)

GL_VERSION_3_0 = 1
GL_COMPARE_REF_TO_TEXTURE = 0x884E
GL_CLIP_DISTANCE0 = 0x3000
GL_CLIP_DISTANCE1 = 0x3001
GL_CLIP_DISTANCE2 = 0x3002
GL_CLIP_DISTANCE3 = 0x3003
GL_CLIP_DISTANCE4 = 0x3004
GL_CLIP_DISTANCE5 = 0x3005
GL_CLIP_DISTANCE6 = 0x3006
GL_CLIP_DISTANCE7 = 0x3007
GL_MAX_CLIP_DISTANCES = 0x0D32
GL_MAJOR_VERSION = 0x821B
GL_MINOR_VERSION = 0x821C
GL_NUM_EXTENSIONS = 0x821D
GL_CONTEXT_FLAGS = 0x821E
GL_COMPRESSED_RED = 0x8225
GL_COMPRESSED_RG = 0x8226
GL_CONTEXT_FLAG_FORWARD_COMPATIBLE_BIT = 0x00000001
GL_RGBA32F = 0x8814
GL_RGB32F = 0x8815
GL_RGBA16F = 0x881A
GL_RGB16F = 0x881B
GL_VERTEX_ATTRIB_ARRAY_INTEGER = 0x88FD
GL_MAX_ARRAY_TEXTURE_LAYERS = 0x88FF
GL_MIN_PROGRAM_TEXEL_OFFSET = 0x8904
GL_MAX_PROGRAM_TEXEL_OFFSET = 0x8905
GL_CLAMP_READ_COLOR = 0x891C
GL_FIXED_ONLY = 0x891D
GL_MAX_VARYING_COMPONENTS = 0x8B4B
GL_TEXTURE_1D_ARRAY = 0x8C18
GL_PROXY_TEXTURE_1D_ARRAY = 0x8C19
GL_TEXTURE_2D_ARRAY = 0x8C1A
GL_PROXY_TEXTURE_2D_ARRAY = 0x8C1B
GL_TEXTURE_BINDING_1D_ARRAY = 0x8C1C
GL_TEXTURE_BINDING_2D_ARRAY = 0x8C1D
GL_R11F_G11F_B10F = 0x8C3A
GL_UNSIGNED_INT_10F_11F_11F_REV = 0x8C3B
GL_RGB9_E5 = 0x8C3D
GL_UNSIGNED_INT_5_9_9_9_REV = 0x8C3E
GL_TEXTURE_SHARED_SIZE = 0x8C3F
GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH = 0x8C76
GL_TRANSFORM_FEEDBACK_BUFFER_MODE = 0x8C7F
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS = 0x8C80
GL_TRANSFORM_FEEDBACK_VARYINGS = 0x8C83
GL_TRANSFORM_FEEDBACK_BUFFER_START = 0x8C84
GL_TRANSFORM_FEEDBACK_BUFFER_SIZE = 0x8C85
GL_PRIMITIVES_GENERATED = 0x8C87
GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN = 0x8C88
GL_RASTERIZER_DISCARD = 0x8C89
GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS = 0x8C8A
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS = 0x8C8B
GL_INTERLEAVED_ATTRIBS = 0x8C8C
GL_SEPARATE_ATTRIBS = 0x8C8D
GL_TRANSFORM_FEEDBACK_BUFFER = 0x8C8E
GL_TRANSFORM_FEEDBACK_BUFFER_BINDING = 0x8C8F
GL_RGBA32UI = 0x8D70
GL_RGB32UI = 0x8D71
GL_RGBA16UI = 0x8D76
GL_RGB16UI = 0x8D77
GL_RGBA8UI = 0x8D7C
GL_RGB8UI = 0x8D7D
GL_RGBA32I = 0x8D82
GL_RGB32I = 0x8D83
GL_RGBA16I = 0x8D88
GL_RGB16I = 0x8D89
GL_RGBA8I = 0x8D8E
GL_RGB8I = 0x8D8F
GL_RED_INTEGER = 0x8D94
GL_GREEN_INTEGER = 0x8D95
GL_BLUE_INTEGER = 0x8D96
GL_RGB_INTEGER = 0x8D98
GL_RGBA_INTEGER = 0x8D99
GL_BGR_INTEGER = 0x8D9A
GL_BGRA_INTEGER = 0x8D9B
GL_SAMPLER_1D_ARRAY = 0x8DC0
GL_SAMPLER_2D_ARRAY = 0x8DC1
GL_SAMPLER_1D_ARRAY_SHADOW = 0x8DC3
GL_SAMPLER_2D_ARRAY_SHADOW = 0x8DC4
GL_SAMPLER_CUBE_SHADOW = 0x8DC5
GL_UNSIGNED_INT_VEC2 = 0x8DC6
GL_UNSIGNED_INT_VEC3 = 0x8DC7
GL_UNSIGNED_INT_VEC4 = 0x8DC8
GL_INT_SAMPLER_1D = 0x8DC9
GL_INT_SAMPLER_2D = 0x8DCA
GL_INT_SAMPLER_3D = 0x8DCB
GL_INT_SAMPLER_CUBE = 0x8DCC
GL_INT_SAMPLER_1D_ARRAY = 0x8DCE
GL_INT_SAMPLER_2D_ARRAY = 0x8DCF
GL_UNSIGNED_INT_SAMPLER_1D = 0x8DD1
GL_UNSIGNED_INT_SAMPLER_2D = 0x8DD2
GL_UNSIGNED_INT_SAMPLER_3D = 0x8DD3
GL_UNSIGNED_INT_SAMPLER_CUBE = 0x8DD4
GL_UNSIGNED_INT_SAMPLER_1D_ARRAY = 0x8DD6
GL_UNSIGNED_INT_SAMPLER_2D_ARRAY = 0x8DD7
GL_QUERY_WAIT = 0x8E13
GL_QUERY_NO_WAIT = 0x8E14
GL_QUERY_BY_REGION_WAIT = 0x8E15
GL_QUERY_BY_REGION_NO_WAIT = 0x8E16
GL_BUFFER_ACCESS_FLAGS = 0x911F
GL_BUFFER_MAP_LENGTH = 0x9120
GL_BUFFER_MAP_OFFSET = 0x9121
GL_DEPTH_COMPONENT32F = 0x8CAC
GL_DEPTH32F_STENCIL8 = 0x8CAD
GL_FLOAT_32_UNSIGNED_INT_24_8_REV = 0x8DAD
GL_INVALID_FRAMEBUFFER_OPERATION = 0x0506
GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING = 0x8210
GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE = 0x8211
GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE = 0x8212
GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE = 0x8213
GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE = 0x8214
GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE = 0x8215
GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE = 0x8216
GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE = 0x8217
GL_FRAMEBUFFER_DEFAULT = 0x8218
GL_FRAMEBUFFER_UNDEFINED = 0x8219
GL_DEPTH_STENCIL_ATTACHMENT = 0x821A
GL_MAX_RENDERBUFFER_SIZE = 0x84E8
GL_DEPTH_STENCIL = 0x84F9
GL_UNSIGNED_INT_24_8 = 0x84FA
GL_DEPTH24_STENCIL8 = 0x88F0
GL_TEXTURE_STENCIL_SIZE = 0x88F1
GL_TEXTURE_RED_TYPE = 0x8C10
GL_TEXTURE_GREEN_TYPE = 0x8C11
GL_TEXTURE_BLUE_TYPE = 0x8C12
GL_TEXTURE_ALPHA_TYPE = 0x8C13
GL_TEXTURE_DEPTH_TYPE = 0x8C16
GL_UNSIGNED_NORMALIZED = 0x8C17
GL_FRAMEBUFFER_BINDING = 0x8CA6
GL_DRAW_FRAMEBUFFER_BINDING = 0x8CA6
GL_RENDERBUFFER_BINDING = 0x8CA7
GL_READ_FRAMEBUFFER = 0x8CA8
GL_DRAW_FRAMEBUFFER = 0x8CA9
GL_READ_FRAMEBUFFER_BINDING = 0x8CAA
GL_RENDERBUFFER_SAMPLES = 0x8CAB
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE = 0x8CD0
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME = 0x8CD1
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL = 0x8CD2
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE = 0x8CD3
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER = 0x8CD4
GL_FRAMEBUFFER_COMPLETE = 0x8CD5
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT = 0x8CD6
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT = 0x8CD7
GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER = 0x8CDB
GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER = 0x8CDC
GL_FRAMEBUFFER_UNSUPPORTED = 0x8CDD
GL_MAX_COLOR_ATTACHMENTS = 0x8CDF
GL_COLOR_ATTACHMENT0 = 0x8CE0
GL_COLOR_ATTACHMENT1 = 0x8CE1
GL_COLOR_ATTACHMENT2 = 0x8CE2
GL_COLOR_ATTACHMENT3 = 0x8CE3
GL_COLOR_ATTACHMENT4 = 0x8CE4
GL_COLOR_ATTACHMENT5 = 0x8CE5
GL_COLOR_ATTACHMENT6 = 0x8CE6
GL_COLOR_ATTACHMENT7 = 0x8CE7
GL_COLOR_ATTACHMENT8 = 0x8CE8
GL_COLOR_ATTACHMENT9 = 0x8CE9
GL_COLOR_ATTACHMENT10 = 0x8CEA
GL_COLOR_ATTACHMENT11 = 0x8CEB
GL_COLOR_ATTACHMENT12 = 0x8CEC
GL_COLOR_ATTACHMENT13 = 0x8CED
GL_COLOR_ATTACHMENT14 = 0x8CEE
GL_COLOR_ATTACHMENT15 = 0x8CEF
GL_COLOR_ATTACHMENT16 = 0x8CF0
GL_COLOR_ATTACHMENT17 = 0x8CF1
GL_COLOR_ATTACHMENT18 = 0x8CF2
GL_COLOR_ATTACHMENT19 = 0x8CF3
GL_COLOR_ATTACHMENT20 = 0x8CF4
GL_COLOR_ATTACHMENT21 = 0x8CF5
GL_COLOR_ATTACHMENT22 = 0x8CF6
GL_COLOR_ATTACHMENT23 = 0x8CF7
GL_COLOR_ATTACHMENT24 = 0x8CF8
GL_COLOR_ATTACHMENT25 = 0x8CF9
GL_COLOR_ATTACHMENT26 = 0x8CFA
GL_COLOR_ATTACHMENT27 = 0x8CFB
GL_COLOR_ATTACHMENT28 = 0x8CFC
GL_COLOR_ATTACHMENT29 = 0x8CFD
GL_COLOR_ATTACHMENT30 = 0x8CFE
GL_COLOR_ATTACHMENT31 = 0x8CFF
GL_DEPTH_ATTACHMENT = 0x8D00
GL_STENCIL_ATTACHMENT = 0x8D20
GL_FRAMEBUFFER = 0x8D40
GL_RENDERBUFFER = 0x8D41
GL_RENDERBUFFER_WIDTH = 0x8D42
GL_RENDERBUFFER_HEIGHT = 0x8D43
GL_RENDERBUFFER_INTERNAL_FORMAT = 0x8D44
GL_STENCIL_INDEX1 = 0x8D46
GL_STENCIL_INDEX4 = 0x8D47
GL_STENCIL_INDEX8 = 0x8D48
GL_STENCIL_INDEX16 = 0x8D49
GL_RENDERBUFFER_RED_SIZE = 0x8D50
GL_RENDERBUFFER_GREEN_SIZE = 0x8D51
GL_RENDERBUFFER_BLUE_SIZE = 0x8D52
GL_RENDERBUFFER_ALPHA_SIZE = 0x8D53
GL_RENDERBUFFER_DEPTH_SIZE = 0x8D54
GL_RENDERBUFFER_STENCIL_SIZE = 0x8D55
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE = 0x8D56
GL_MAX_SAMPLES = 0x8D57
GL_FRAMEBUFFER_SRGB = 0x8DB9
GL_HALF_FLOAT = 0x140B
GL_MAP_READ_BIT = 0x0001
GL_MAP_WRITE_BIT = 0x0002
GL_MAP_INVALIDATE_RANGE_BIT = 0x0004
GL_MAP_INVALIDATE_BUFFER_BIT = 0x0008
GL_MAP_FLUSH_EXPLICIT_BIT = 0x0010
GL_MAP_UNSYNCHRONIZED_BIT = 0x0020
GL_COMPRESSED_RED_RGTC1 = 0x8DBB
GL_COMPRESSED_SIGNED_RED_RGTC1 = 0x8DBC
GL_COMPRESSED_RG_RGTC2 = 0x8DBD
GL_COMPRESSED_SIGNED_RG_RGTC2 = 0x8DBE
GL_RG = 0x8227
GL_RG_INTEGER = 0x8228
GL_R8 = 0x8229
GL_R16 = 0x822A
GL_RG8 = 0x822B
GL_RG16 = 0x822C
GL_R16F = 0x822D
GL_R32F = 0x822E
GL_RG16F = 0x822F
GL_RG32F = 0x8230
GL_R8I = 0x8231
GL_R8UI = 0x8232
GL_R16I = 0x8233
GL_R16UI = 0x8234
GL_R32I = 0x8235
GL_R32UI = 0x8236
GL_RG8I = 0x8237
GL_RG8UI = 0x8238
GL_RG16I = 0x8239
GL_RG16UI = 0x823A
GL_RG32I = 0x823B
GL_RG32UI = 0x823C
GL_VERTEX_ARRAY_BINDING = 0x85B5
glColorMaski = _gl.glColorMaski
glColorMaski.restype = None
glColorMaski.argtypes = (GLuint, GLboolean, GLboolean, GLboolean, GLboolean,)

glGetBooleani_v = _gl.glGetBooleani_v
glGetBooleani_v.restype = None
glGetBooleani_v.argtypes = (GLenum, GLuint, POINTER(GLboolean),)

glGetIntegeri_v = _gl.glGetIntegeri_v
glGetIntegeri_v.restype = None
glGetIntegeri_v.argtypes = (GLenum, GLuint, POINTER(GLint),)

glEnablei = _gl.glEnablei
glEnablei.restype = None
glEnablei.argtypes = (GLenum, GLuint,)

glDisablei = _gl.glDisablei
glDisablei.restype = None
glDisablei.argtypes = (GLenum, GLuint,)

glIsEnabledi = _gl.glIsEnabledi
glIsEnabledi.restype = GLboolean
glIsEnabledi.argtypes = (GLenum, GLuint,)

glBeginTransformFeedback = _gl.glBeginTransformFeedback
glBeginTransformFeedback.restype = None
glBeginTransformFeedback.argtypes = (GLenum,)

glEndTransformFeedback = _gl.glEndTransformFeedback
glEndTransformFeedback.restype = None
glEndTransformFeedback.argtypes = ()

glBindBufferRange = _gl.glBindBufferRange
glBindBufferRange.restype = None
glBindBufferRange.argtypes = (GLenum, GLuint, GLuint, GLintptr, GLsizeiptr,)

glBindBufferBase = _gl.glBindBufferBase
glBindBufferBase.restype = None
glBindBufferBase.argtypes = (GLenum, GLuint, GLuint,)

glTransformFeedbackVaryings = _gl.glTransformFeedbackVaryings
glTransformFeedbackVaryings.restype = None
glTransformFeedbackVaryings.argtypes = (GLuint, GLsizei, POINTER(STRING), GLenum,)

glGetTransformFeedbackVarying = _gl.glGetTransformFeedbackVarying
glGetTransformFeedbackVarying.restype = None
glGetTransformFeedbackVarying.argtypes = (GLuint, GLuint, GLsizei, POINTER(GLsizei), POINTER(GLsizei), POINTER(GLenum), STRING,)

glClampColor = _gl.glClampColor
glClampColor.restype = None
glClampColor.argtypes = (GLenum, GLenum,)

glBeginConditionalRender = _gl.glBeginConditionalRender
glBeginConditionalRender.restype = None
glBeginConditionalRender.argtypes = (GLuint, GLenum,)

glEndConditionalRender = _gl.glEndConditionalRender
glEndConditionalRender.restype = None
glEndConditionalRender.argtypes = ()

glVertexAttribIPointer = _gl.glVertexAttribIPointer
glVertexAttribIPointer.restype = None
glVertexAttribIPointer.argtypes = (GLuint, GLint, GLenum, GLsizei, POINTER(None),)

glGetVertexAttribIiv = _gl.glGetVertexAttribIiv
glGetVertexAttribIiv.restype = None
glGetVertexAttribIiv.argtypes = (GLuint, GLenum, POINTER(GLint),)

glGetVertexAttribIuiv = _gl.glGetVertexAttribIuiv
glGetVertexAttribIuiv.restype = None
glGetVertexAttribIuiv.argtypes = (GLuint, GLenum, POINTER(GLuint),)

glVertexAttribI1i = _gl.glVertexAttribI1i
glVertexAttribI1i.restype = None
glVertexAttribI1i.argtypes = (GLuint, GLint,)

glVertexAttribI2i = _gl.glVertexAttribI2i
glVertexAttribI2i.restype = None
glVertexAttribI2i.argtypes = (GLuint, GLint, GLint,)

glVertexAttribI3i = _gl.glVertexAttribI3i
glVertexAttribI3i.restype = None
glVertexAttribI3i.argtypes = (GLuint, GLint, GLint, GLint,)

glVertexAttribI4i = _gl.glVertexAttribI4i
glVertexAttribI4i.restype = None
glVertexAttribI4i.argtypes = (GLuint, GLint, GLint, GLint, GLint,)

glVertexAttribI1ui = _gl.glVertexAttribI1ui
glVertexAttribI1ui.restype = None
glVertexAttribI1ui.argtypes = (GLuint, GLuint,)

glVertexAttribI2ui = _gl.glVertexAttribI2ui
glVertexAttribI2ui.restype = None
glVertexAttribI2ui.argtypes = (GLuint, GLuint, GLuint,)

glVertexAttribI3ui = _gl.glVertexAttribI3ui
glVertexAttribI3ui.restype = None
glVertexAttribI3ui.argtypes = (GLuint, GLuint, GLuint, GLuint,)

glVertexAttribI4ui = _gl.glVertexAttribI4ui
glVertexAttribI4ui.restype = None
glVertexAttribI4ui.argtypes = (GLuint, GLuint, GLuint, GLuint, GLuint,)

glVertexAttribI1iv = _gl.glVertexAttribI1iv
glVertexAttribI1iv.restype = None
glVertexAttribI1iv.argtypes = (GLuint, POINTER(GLint),)

glVertexAttribI2iv = _gl.glVertexAttribI2iv
glVertexAttribI2iv.restype = None
glVertexAttribI2iv.argtypes = (GLuint, POINTER(GLint),)

glVertexAttribI3iv = _gl.glVertexAttribI3iv
glVertexAttribI3iv.restype = None
glVertexAttribI3iv.argtypes = (GLuint, POINTER(GLint),)

glVertexAttribI4iv = _gl.glVertexAttribI4iv
glVertexAttribI4iv.restype = None
glVertexAttribI4iv.argtypes = (GLuint, POINTER(GLint),)

glVertexAttribI1uiv = _gl.glVertexAttribI1uiv
glVertexAttribI1uiv.restype = None
glVertexAttribI1uiv.argtypes = (GLuint, POINTER(GLuint),)

glVertexAttribI2uiv = _gl.glVertexAttribI2uiv
glVertexAttribI2uiv.restype = None
glVertexAttribI2uiv.argtypes = (GLuint, POINTER(GLuint),)

glVertexAttribI3uiv = _gl.glVertexAttribI3uiv
glVertexAttribI3uiv.restype = None
glVertexAttribI3uiv.argtypes = (GLuint, POINTER(GLuint),)

glVertexAttribI4uiv = _gl.glVertexAttribI4uiv
glVertexAttribI4uiv.restype = None
glVertexAttribI4uiv.argtypes = (GLuint, POINTER(GLuint),)

glVertexAttribI4bv = _gl.glVertexAttribI4bv
glVertexAttribI4bv.restype = None
glVertexAttribI4bv.argtypes = (GLuint, POINTER(GLbyte),)

glVertexAttribI4sv = _gl.glVertexAttribI4sv
glVertexAttribI4sv.restype = None
glVertexAttribI4sv.argtypes = (GLuint, POINTER(GLshort),)

glVertexAttribI4ubv = _gl.glVertexAttribI4ubv
glVertexAttribI4ubv.restype = None
glVertexAttribI4ubv.argtypes = (GLuint, POINTER(GLubyte),)

glVertexAttribI4usv = _gl.glVertexAttribI4usv
glVertexAttribI4usv.restype = None
glVertexAttribI4usv.argtypes = (GLuint, POINTER(GLushort),)

glGetUniformuiv = _gl.glGetUniformuiv
glGetUniformuiv.restype = None
glGetUniformuiv.argtypes = (GLuint, GLint, POINTER(GLuint),)

glBindFragDataLocation = _gl.glBindFragDataLocation
glBindFragDataLocation.restype = None
glBindFragDataLocation.argtypes = (GLuint, GLuint, STRING,)

glGetFragDataLocation = _gl.glGetFragDataLocation
glGetFragDataLocation.restype = GLint
glGetFragDataLocation.argtypes = (GLuint, STRING,)

glUniform1ui = _gl.glUniform1ui
glUniform1ui.restype = None
glUniform1ui.argtypes = (GLint, GLuint,)

glUniform2ui = _gl.glUniform2ui
glUniform2ui.restype = None
glUniform2ui.argtypes = (GLint, GLuint, GLuint,)

glUniform3ui = _gl.glUniform3ui
glUniform3ui.restype = None
glUniform3ui.argtypes = (GLint, GLuint, GLuint, GLuint,)

glUniform4ui = _gl.glUniform4ui
glUniform4ui.restype = None
glUniform4ui.argtypes = (GLint, GLuint, GLuint, GLuint, GLuint,)

glUniform1uiv = _gl.glUniform1uiv
glUniform1uiv.restype = None
glUniform1uiv.argtypes = (GLint, GLsizei, POINTER(GLuint),)

glUniform2uiv = _gl.glUniform2uiv
glUniform2uiv.restype = None
glUniform2uiv.argtypes = (GLint, GLsizei, POINTER(GLuint),)

glUniform3uiv = _gl.glUniform3uiv
glUniform3uiv.restype = None
glUniform3uiv.argtypes = (GLint, GLsizei, POINTER(GLuint),)

glUniform4uiv = _gl.glUniform4uiv
glUniform4uiv.restype = None
glUniform4uiv.argtypes = (GLint, GLsizei, POINTER(GLuint),)

glTexParameterIiv = _gl.glTexParameterIiv
glTexParameterIiv.restype = None
glTexParameterIiv.argtypes = (GLenum, GLenum, POINTER(GLint),)

glTexParameterIuiv = _gl.glTexParameterIuiv
glTexParameterIuiv.restype = None
glTexParameterIuiv.argtypes = (GLenum, GLenum, POINTER(GLuint),)

glGetTexParameterIiv = _gl.glGetTexParameterIiv
glGetTexParameterIiv.restype = None
glGetTexParameterIiv.argtypes = (GLenum, GLenum, POINTER(GLint),)

glGetTexParameterIuiv = _gl.glGetTexParameterIuiv
glGetTexParameterIuiv.restype = None
glGetTexParameterIuiv.argtypes = (GLenum, GLenum, POINTER(GLuint),)

glClearBufferiv = _gl.glClearBufferiv
glClearBufferiv.restype = None
glClearBufferiv.argtypes = (GLenum, GLint, POINTER(GLint),)

glClearBufferuiv = _gl.glClearBufferuiv
glClearBufferuiv.restype = None
glClearBufferuiv.argtypes = (GLenum, GLint, POINTER(GLuint),)

glClearBufferfv = _gl.glClearBufferfv
glClearBufferfv.restype = None
glClearBufferfv.argtypes = (GLenum, GLint, POINTER(GLfloat),)

glClearBufferfi = _gl.glClearBufferfi
glClearBufferfi.restype = None
glClearBufferfi.argtypes = (GLenum, GLint, GLfloat, GLint,)

glGetStringi = _gl.glGetStringi
glGetStringi.restype = POINTER(GLubyte)
glGetStringi.argtypes = (GLenum, GLuint,)

glIsRenderbuffer = _gl.glIsRenderbuffer
glIsRenderbuffer.restype = GLboolean
glIsRenderbuffer.argtypes = (GLuint,)

glBindRenderbuffer = _gl.glBindRenderbuffer
glBindRenderbuffer.restype = None
glBindRenderbuffer.argtypes = (GLenum, GLuint,)

glDeleteRenderbuffers = _gl.glDeleteRenderbuffers
glDeleteRenderbuffers.restype = None
glDeleteRenderbuffers.argtypes = (GLsizei, POINTER(GLuint),)

glGenRenderbuffers = _gl.glGenRenderbuffers
glGenRenderbuffers.restype = None
glGenRenderbuffers.argtypes = (GLsizei, POINTER(GLuint),)

glRenderbufferStorage = _gl.glRenderbufferStorage
glRenderbufferStorage.restype = None
glRenderbufferStorage.argtypes = (GLenum, GLenum, GLsizei, GLsizei,)

glGetRenderbufferParameteriv = _gl.glGetRenderbufferParameteriv
glGetRenderbufferParameteriv.restype = None
glGetRenderbufferParameteriv.argtypes = (GLenum, GLenum, POINTER(GLint),)

glIsFramebuffer = _gl.glIsFramebuffer
glIsFramebuffer.restype = GLboolean
glIsFramebuffer.argtypes = (GLuint,)

glBindFramebuffer = _gl.glBindFramebuffer
glBindFramebuffer.restype = None
glBindFramebuffer.argtypes = (GLenum, GLuint,)

glDeleteFramebuffers = _gl.glDeleteFramebuffers
glDeleteFramebuffers.restype = None
glDeleteFramebuffers.argtypes = (GLsizei, POINTER(GLuint),)

glGenFramebuffers = _gl.glGenFramebuffers
glGenFramebuffers.restype = None
glGenFramebuffers.argtypes = (GLsizei, POINTER(GLuint),)

glCheckFramebufferStatus = _gl.glCheckFramebufferStatus
glCheckFramebufferStatus.restype = GLenum
glCheckFramebufferStatus.argtypes = (GLenum,)

glFramebufferTexture1D = _gl.glFramebufferTexture1D
glFramebufferTexture1D.restype = None
glFramebufferTexture1D.argtypes = (GLenum, GLenum, GLenum, GLuint, GLint,)

glFramebufferTexture2D = _gl.glFramebufferTexture2D
glFramebufferTexture2D.restype = None
glFramebufferTexture2D.argtypes = (GLenum, GLenum, GLenum, GLuint, GLint,)

glFramebufferTexture3D = _gl.glFramebufferTexture3D
glFramebufferTexture3D.restype = None
glFramebufferTexture3D.argtypes = (GLenum, GLenum, GLenum, GLuint, GLint, GLint,)

glFramebufferRenderbuffer = _gl.glFramebufferRenderbuffer
glFramebufferRenderbuffer.restype = None
glFramebufferRenderbuffer.argtypes = (GLenum, GLenum, GLenum, GLuint,)

glGetFramebufferAttachmentParameteriv = _gl.glGetFramebufferAttachmentParameteriv
glGetFramebufferAttachmentParameteriv.restype = None
glGetFramebufferAttachmentParameteriv.argtypes = (GLenum, GLenum, GLenum, POINTER(GLint),)

glGenerateMipmap = _gl.glGenerateMipmap
glGenerateMipmap.restype = None
glGenerateMipmap.argtypes = (GLenum,)

glBlitFramebuffer = _gl.glBlitFramebuffer
glBlitFramebuffer.restype = None
glBlitFramebuffer.argtypes = (GLint, GLint, GLint, GLint, GLint, GLint, GLint, GLint, GLbitfield, GLenum,)

glRenderbufferStorageMultisample = _gl.glRenderbufferStorageMultisample
glRenderbufferStorageMultisample.restype = None
glRenderbufferStorageMultisample.argtypes = (GLenum, GLsizei, GLenum, GLsizei, GLsizei,)

glFramebufferTextureLayer = _gl.glFramebufferTextureLayer
glFramebufferTextureLayer.restype = None
glFramebufferTextureLayer.argtypes = (GLenum, GLenum, GLuint, GLint, GLint,)

glMapBufferRange = _gl.glMapBufferRange
glMapBufferRange.restype = POINTER(None)
glMapBufferRange.argtypes = (GLenum, GLintptr, GLsizeiptr, GLbitfield,)

glFlushMappedBufferRange = _gl.glFlushMappedBufferRange
glFlushMappedBufferRange.restype = None
glFlushMappedBufferRange.argtypes = (GLenum, GLintptr, GLsizeiptr,)

glBindVertexArray = _gl.glBindVertexArray
glBindVertexArray.restype = None
glBindVertexArray.argtypes = (GLuint,)

glDeleteVertexArrays = _gl.glDeleteVertexArrays
glDeleteVertexArrays.restype = None
glDeleteVertexArrays.argtypes = (GLsizei, POINTER(GLuint),)

glGenVertexArrays = _gl.glGenVertexArrays
glGenVertexArrays.restype = None
glGenVertexArrays.argtypes = (GLsizei, POINTER(GLuint),)

glIsVertexArray = _gl.glIsVertexArray
glIsVertexArray.restype = GLboolean
glIsVertexArray.argtypes = (GLuint,)

GL_VERSION_3_1 = 1
GL_SAMPLER_2D_RECT = 0x8B63
GL_SAMPLER_2D_RECT_SHADOW = 0x8B64
GL_SAMPLER_BUFFER = 0x8DC2
GL_INT_SAMPLER_2D_RECT = 0x8DCD
GL_INT_SAMPLER_BUFFER = 0x8DD0
GL_UNSIGNED_INT_SAMPLER_2D_RECT = 0x8DD5
GL_UNSIGNED_INT_SAMPLER_BUFFER = 0x8DD8
GL_TEXTURE_BUFFER = 0x8C2A
GL_MAX_TEXTURE_BUFFER_SIZE = 0x8C2B
GL_TEXTURE_BINDING_BUFFER = 0x8C2C
GL_TEXTURE_BUFFER_DATA_STORE_BINDING = 0x8C2D
GL_TEXTURE_RECTANGLE = 0x84F5
GL_TEXTURE_BINDING_RECTANGLE = 0x84F6
GL_PROXY_TEXTURE_RECTANGLE = 0x84F7
GL_MAX_RECTANGLE_TEXTURE_SIZE = 0x84F8
GL_R8_SNORM = 0x8F94
GL_RG8_SNORM = 0x8F95
GL_RGB8_SNORM = 0x8F96
GL_RGBA8_SNORM = 0x8F97
GL_R16_SNORM = 0x8F98
GL_RG16_SNORM = 0x8F99
GL_RGB16_SNORM = 0x8F9A
GL_RGBA16_SNORM = 0x8F9B
GL_SIGNED_NORMALIZED = 0x8F9C
GL_PRIMITIVE_RESTART = 0x8F9D
GL_PRIMITIVE_RESTART_INDEX = 0x8F9E
GL_COPY_READ_BUFFER = 0x8F36
GL_COPY_WRITE_BUFFER = 0x8F37
GL_UNIFORM_BUFFER = 0x8A11
GL_UNIFORM_BUFFER_BINDING = 0x8A28
GL_UNIFORM_BUFFER_START = 0x8A29
GL_UNIFORM_BUFFER_SIZE = 0x8A2A
GL_MAX_VERTEX_UNIFORM_BLOCKS = 0x8A2B
GL_MAX_GEOMETRY_UNIFORM_BLOCKS = 0x8A2C
GL_MAX_FRAGMENT_UNIFORM_BLOCKS = 0x8A2D
GL_MAX_COMBINED_UNIFORM_BLOCKS = 0x8A2E
GL_MAX_UNIFORM_BUFFER_BINDINGS = 0x8A2F
GL_MAX_UNIFORM_BLOCK_SIZE = 0x8A30
GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS = 0x8A31
GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS = 0x8A32
GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS = 0x8A33
GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT = 0x8A34
GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH = 0x8A35
GL_ACTIVE_UNIFORM_BLOCKS = 0x8A36
GL_UNIFORM_TYPE = 0x8A37
GL_UNIFORM_SIZE = 0x8A38
GL_UNIFORM_NAME_LENGTH = 0x8A39
GL_UNIFORM_BLOCK_INDEX = 0x8A3A
GL_UNIFORM_OFFSET = 0x8A3B
GL_UNIFORM_ARRAY_STRIDE = 0x8A3C
GL_UNIFORM_MATRIX_STRIDE = 0x8A3D
GL_UNIFORM_IS_ROW_MAJOR = 0x8A3E
GL_UNIFORM_BLOCK_BINDING = 0x8A3F
GL_UNIFORM_BLOCK_DATA_SIZE = 0x8A40
GL_UNIFORM_BLOCK_NAME_LENGTH = 0x8A41
GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS = 0x8A42
GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES = 0x8A43
GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER = 0x8A44
GL_UNIFORM_BLOCK_REFERENCED_BY_GEOMETRY_SHADER = 0x8A45
GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER = 0x8A46
GL_INVALID_INDEX = 0xFFFFFFFF
glDrawArraysInstanced = _gl.glDrawArraysInstanced
glDrawArraysInstanced.restype = None
glDrawArraysInstanced.argtypes = (GLenum, GLint, GLsizei, GLsizei,)

glDrawElementsInstanced = _gl.glDrawElementsInstanced
glDrawElementsInstanced.restype = None
glDrawElementsInstanced.argtypes = (GLenum, GLsizei, GLenum, POINTER(None), GLsizei,)

glTexBuffer = _gl.glTexBuffer
glTexBuffer.restype = None
glTexBuffer.argtypes = (GLenum, GLenum, GLuint,)

glPrimitiveRestartIndex = _gl.glPrimitiveRestartIndex
glPrimitiveRestartIndex.restype = None
glPrimitiveRestartIndex.argtypes = (GLuint,)

glCopyBufferSubData = _gl.glCopyBufferSubData
glCopyBufferSubData.restype = None
glCopyBufferSubData.argtypes = (GLenum, GLenum, GLintptr, GLintptr, GLsizeiptr,)

glGetUniformIndices = _gl.glGetUniformIndices
glGetUniformIndices.restype = None
glGetUniformIndices.argtypes = (GLuint, GLsizei, POINTER(STRING), POINTER(GLuint),)

glGetActiveUniformsiv = _gl.glGetActiveUniformsiv
glGetActiveUniformsiv.restype = None
glGetActiveUniformsiv.argtypes = (GLuint, GLsizei, POINTER(GLuint), GLenum, POINTER(GLint),)

glGetActiveUniformName = _gl.glGetActiveUniformName
glGetActiveUniformName.restype = None
glGetActiveUniformName.argtypes = (GLuint, GLuint, GLsizei, POINTER(GLsizei), STRING,)

glGetUniformBlockIndex = _gl.glGetUniformBlockIndex
glGetUniformBlockIndex.restype = GLuint
glGetUniformBlockIndex.argtypes = (GLuint, STRING,)

glGetActiveUniformBlockiv = _gl.glGetActiveUniformBlockiv
glGetActiveUniformBlockiv.restype = None
glGetActiveUniformBlockiv.argtypes = (GLuint, GLuint, GLenum, POINTER(GLint),)

glGetActiveUniformBlockName = _gl.glGetActiveUniformBlockName
glGetActiveUniformBlockName.restype = None
glGetActiveUniformBlockName.argtypes = (GLuint, GLuint, GLsizei, POINTER(GLsizei), STRING,)

glUniformBlockBinding = _gl.glUniformBlockBinding
glUniformBlockBinding.restype = None
glUniformBlockBinding.argtypes = (GLuint, GLuint, GLuint,)

GL_VERSION_3_2 = 1
GL_CONTEXT_CORE_PROFILE_BIT = 0x00000001
GL_CONTEXT_COMPATIBILITY_PROFILE_BIT = 0x00000002
GL_LINES_ADJACENCY = 0x000A
GL_LINE_STRIP_ADJACENCY = 0x000B
GL_TRIANGLES_ADJACENCY = 0x000C
GL_TRIANGLE_STRIP_ADJACENCY = 0x000D
GL_PROGRAM_POINT_SIZE = 0x8642
GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS = 0x8C29
GL_FRAMEBUFFER_ATTACHMENT_LAYERED = 0x8DA7
GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS = 0x8DA8
GL_GEOMETRY_SHADER = 0x8DD9
GL_GEOMETRY_VERTICES_OUT = 0x8916
GL_GEOMETRY_INPUT_TYPE = 0x8917
GL_GEOMETRY_OUTPUT_TYPE = 0x8918
GL_MAX_GEOMETRY_UNIFORM_COMPONENTS = 0x8DDF
GL_MAX_GEOMETRY_OUTPUT_VERTICES = 0x8DE0
GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS = 0x8DE1
GL_MAX_VERTEX_OUTPUT_COMPONENTS = 0x9122
GL_MAX_GEOMETRY_INPUT_COMPONENTS = 0x9123
GL_MAX_GEOMETRY_OUTPUT_COMPONENTS = 0x9124
GL_MAX_FRAGMENT_INPUT_COMPONENTS = 0x9125
GL_CONTEXT_PROFILE_MASK = 0x9126
GL_DEPTH_CLAMP = 0x864F
GL_QUADS_FOLLOW_PROVOKING_VERTEX_CONVENTION = 0x8E4C
GL_FIRST_VERTEX_CONVENTION = 0x8E4D
GL_LAST_VERTEX_CONVENTION = 0x8E4E
GL_PROVOKING_VERTEX = 0x8E4F
GL_TEXTURE_CUBE_MAP_SEAMLESS = 0x884F
GL_MAX_SERVER_WAIT_TIMEOUT = 0x9111
GL_OBJECT_TYPE = 0x9112
GL_SYNC_CONDITION = 0x9113
GL_SYNC_STATUS = 0x9114
GL_SYNC_FLAGS = 0x9115
GL_SYNC_FENCE = 0x9116
GL_SYNC_GPU_COMMANDS_COMPLETE = 0x9117
GL_UNSIGNALED = 0x9118
GL_SIGNALED = 0x9119
GL_ALREADY_SIGNALED = 0x911A
GL_TIMEOUT_EXPIRED = 0x911B
GL_CONDITION_SATISFIED = 0x911C
GL_WAIT_FAILED = 0x911D
GL_TIMEOUT_IGNORED = 0xFFFFFFFFFFFFFFFF
GL_SYNC_FLUSH_COMMANDS_BIT = 0x00000001
GL_SAMPLE_POSITION = 0x8E50
GL_SAMPLE_MASK = 0x8E51
GL_SAMPLE_MASK_VALUE = 0x8E52
GL_MAX_SAMPLE_MASK_WORDS = 0x8E59
GL_TEXTURE_2D_MULTISAMPLE = 0x9100
GL_PROXY_TEXTURE_2D_MULTISAMPLE = 0x9101
GL_TEXTURE_2D_MULTISAMPLE_ARRAY = 0x9102
GL_PROXY_TEXTURE_2D_MULTISAMPLE_ARRAY = 0x9103
GL_TEXTURE_BINDING_2D_MULTISAMPLE = 0x9104
GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY = 0x9105
GL_TEXTURE_SAMPLES = 0x9106
GL_TEXTURE_FIXED_SAMPLE_LOCATIONS = 0x9107
GL_SAMPLER_2D_MULTISAMPLE = 0x9108
GL_INT_SAMPLER_2D_MULTISAMPLE = 0x9109
GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE = 0x910A
GL_SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910B
GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910C
GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910D
GL_MAX_COLOR_TEXTURE_SAMPLES = 0x910E
GL_MAX_DEPTH_TEXTURE_SAMPLES = 0x910F
GL_MAX_INTEGER_SAMPLES = 0x9110
glDrawElementsBaseVertex = _gl.glDrawElementsBaseVertex
glDrawElementsBaseVertex.restype = None
glDrawElementsBaseVertex.argtypes = (GLenum, GLsizei, GLenum, POINTER(None), GLint,)

glDrawRangeElementsBaseVertex = _gl.glDrawRangeElementsBaseVertex
glDrawRangeElementsBaseVertex.restype = None
glDrawRangeElementsBaseVertex.argtypes = (GLenum, GLuint, GLuint, GLsizei, GLenum, POINTER(None), GLint,)

glDrawElementsInstancedBaseVertex = _gl.glDrawElementsInstancedBaseVertex
glDrawElementsInstancedBaseVertex.restype = None
glDrawElementsInstancedBaseVertex.argtypes = (GLenum, GLsizei, GLenum, POINTER(None), GLsizei, GLint,)

glMultiDrawElementsBaseVertex = _gl.glMultiDrawElementsBaseVertex
glMultiDrawElementsBaseVertex.restype = None
glMultiDrawElementsBaseVertex.argtypes = (GLenum, POINTER(GLsizei), GLenum, POINTER(POINTER(None)), GLsizei, POINTER(GLint),)

glProvokingVertex = _gl.glProvokingVertex
glProvokingVertex.restype = None
glProvokingVertex.argtypes = (GLenum,)

glFenceSync = _gl.glFenceSync
glFenceSync.restype = GLsync
glFenceSync.argtypes = (GLenum, GLbitfield,)

glIsSync = _gl.glIsSync
glIsSync.restype = GLboolean
glIsSync.argtypes = (GLsync,)

glDeleteSync = _gl.glDeleteSync
glDeleteSync.restype = None
glDeleteSync.argtypes = (GLsync,)

glClientWaitSync = _gl.glClientWaitSync
glClientWaitSync.restype = GLenum
glClientWaitSync.argtypes = (GLsync, GLbitfield, GLuint64,)

glWaitSync = _gl.glWaitSync
glWaitSync.restype = None
glWaitSync.argtypes = (GLsync, GLbitfield, GLuint64,)

glGetInteger64v = _gl.glGetInteger64v
glGetInteger64v.restype = None
glGetInteger64v.argtypes = (GLenum, POINTER(GLint64),)

glGetSynciv = _gl.glGetSynciv
glGetSynciv.restype = None
glGetSynciv.argtypes = (GLsync, GLenum, GLsizei, POINTER(GLsizei), POINTER(GLint),)

glGetInteger64i_v = _gl.glGetInteger64i_v
glGetInteger64i_v.restype = None
glGetInteger64i_v.argtypes = (GLenum, GLuint, POINTER(GLint64),)

glGetBufferParameteri64v = _gl.glGetBufferParameteri64v
glGetBufferParameteri64v.restype = None
glGetBufferParameteri64v.argtypes = (GLenum, GLenum, POINTER(GLint64),)

glFramebufferTexture = _gl.glFramebufferTexture
glFramebufferTexture.restype = None
glFramebufferTexture.argtypes = (GLenum, GLenum, GLuint, GLint,)

glTexImage2DMultisample = _gl.glTexImage2DMultisample
glTexImage2DMultisample.restype = None
glTexImage2DMultisample.argtypes = (GLenum, GLsizei, GLenum, GLsizei, GLsizei, GLboolean,)

glTexImage3DMultisample = _gl.glTexImage3DMultisample
glTexImage3DMultisample.restype = None
glTexImage3DMultisample.argtypes = (GLenum, GLsizei, GLenum, GLsizei, GLsizei, GLsizei, GLboolean,)

glGetMultisamplefv = _gl.glGetMultisamplefv
glGetMultisamplefv.restype = None
glGetMultisamplefv.argtypes = (GLenum, GLuint, POINTER(GLfloat),)

glSampleMaski = _gl.glSampleMaski
glSampleMaski.restype = None
glSampleMaski.argtypes = (GLuint, GLbitfield,)

GL_VERSION_3_3 = 1
GL_VERTEX_ATTRIB_ARRAY_DIVISOR = 0x88FE
GL_SRC1_COLOR = 0x88F9
GL_ONE_MINUS_SRC1_COLOR = 0x88FA
GL_ONE_MINUS_SRC1_ALPHA = 0x88FB
GL_MAX_DUAL_SOURCE_DRAW_BUFFERS = 0x88FC
GL_ANY_SAMPLES_PASSED = 0x8C2F
GL_SAMPLER_BINDING = 0x8919
GL_RGB10_A2UI = 0x906F
GL_TEXTURE_SWIZZLE_R = 0x8E42
GL_TEXTURE_SWIZZLE_G = 0x8E43
GL_TEXTURE_SWIZZLE_B = 0x8E44
GL_TEXTURE_SWIZZLE_A = 0x8E45
GL_TEXTURE_SWIZZLE_RGBA = 0x8E46
GL_TIME_ELAPSED = 0x88BF
GL_TIMESTAMP = 0x8E28
GL_INT_2_10_10_10_REV = 0x8D9F
glBindFragDataLocationIndexed = _gl.glBindFragDataLocationIndexed
glBindFragDataLocationIndexed.restype = None
glBindFragDataLocationIndexed.argtypes = (GLuint, GLuint, GLuint, STRING,)

glGetFragDataIndex = _gl.glGetFragDataIndex
glGetFragDataIndex.restype = GLint
glGetFragDataIndex.argtypes = (GLuint, STRING,)

glGenSamplers = _gl.glGenSamplers
glGenSamplers.restype = None
glGenSamplers.argtypes = (GLsizei, POINTER(GLuint),)

glDeleteSamplers = _gl.glDeleteSamplers
glDeleteSamplers.restype = None
glDeleteSamplers.argtypes = (GLsizei, POINTER(GLuint),)

glIsSampler = _gl.glIsSampler
glIsSampler.restype = GLboolean
glIsSampler.argtypes = (GLuint,)

glBindSampler = _gl.glBindSampler
glBindSampler.restype = None
glBindSampler.argtypes = (GLuint, GLuint,)

glSamplerParameteri = _gl.glSamplerParameteri
glSamplerParameteri.restype = None
glSamplerParameteri.argtypes = (GLuint, GLenum, GLint,)

glSamplerParameteriv = _gl.glSamplerParameteriv
glSamplerParameteriv.restype = None
glSamplerParameteriv.argtypes = (GLuint, GLenum, POINTER(GLint),)

glSamplerParameterf = _gl.glSamplerParameterf
glSamplerParameterf.restype = None
glSamplerParameterf.argtypes = (GLuint, GLenum, GLfloat,)

glSamplerParameterfv = _gl.glSamplerParameterfv
glSamplerParameterfv.restype = None
glSamplerParameterfv.argtypes = (GLuint, GLenum, POINTER(GLfloat),)

glSamplerParameterIiv = _gl.glSamplerParameterIiv
glSamplerParameterIiv.restype = None
glSamplerParameterIiv.argtypes = (GLuint, GLenum, POINTER(GLint),)

glSamplerParameterIuiv = _gl.glSamplerParameterIuiv
glSamplerParameterIuiv.restype = None
glSamplerParameterIuiv.argtypes = (GLuint, GLenum, POINTER(GLuint),)

glGetSamplerParameteriv = _gl.glGetSamplerParameteriv
glGetSamplerParameteriv.restype = None
glGetSamplerParameteriv.argtypes = (GLuint, GLenum, POINTER(GLint),)

glGetSamplerParameterIiv = _gl.glGetSamplerParameterIiv
glGetSamplerParameterIiv.restype = None
glGetSamplerParameterIiv.argtypes = (GLuint, GLenum, POINTER(GLint),)

glGetSamplerParameterfv = _gl.glGetSamplerParameterfv
glGetSamplerParameterfv.restype = None
glGetSamplerParameterfv.argtypes = (GLuint, GLenum, POINTER(GLfloat),)

glGetSamplerParameterIuiv = _gl.glGetSamplerParameterIuiv
glGetSamplerParameterIuiv.restype = None
glGetSamplerParameterIuiv.argtypes = (GLuint, GLenum, POINTER(GLuint),)

glQueryCounter = _gl.glQueryCounter
glQueryCounter.restype = None
glQueryCounter.argtypes = (GLuint, GLenum,)

glGetQueryObjecti64v = _gl.glGetQueryObjecti64v
glGetQueryObjecti64v.restype = None
glGetQueryObjecti64v.argtypes = (GLuint, GLenum, POINTER(GLint64),)

glGetQueryObjectui64v = _gl.glGetQueryObjectui64v
glGetQueryObjectui64v.restype = None
glGetQueryObjectui64v.argtypes = (GLuint, GLenum, POINTER(GLuint64),)

glVertexAttribDivisor = _gl.glVertexAttribDivisor
glVertexAttribDivisor.restype = None
glVertexAttribDivisor.argtypes = (GLuint, GLuint,)

glVertexAttribP1ui = _gl.glVertexAttribP1ui
glVertexAttribP1ui.restype = None
glVertexAttribP1ui.argtypes = (GLuint, GLenum, GLboolean, GLuint,)

glVertexAttribP1uiv = _gl.glVertexAttribP1uiv
glVertexAttribP1uiv.restype = None
glVertexAttribP1uiv.argtypes = (GLuint, GLenum, GLboolean, POINTER(GLuint),)

glVertexAttribP2ui = _gl.glVertexAttribP2ui
glVertexAttribP2ui.restype = None
glVertexAttribP2ui.argtypes = (GLuint, GLenum, GLboolean, GLuint,)

glVertexAttribP2uiv = _gl.glVertexAttribP2uiv
glVertexAttribP2uiv.restype = None
glVertexAttribP2uiv.argtypes = (GLuint, GLenum, GLboolean, POINTER(GLuint),)

glVertexAttribP3ui = _gl.glVertexAttribP3ui
glVertexAttribP3ui.restype = None
glVertexAttribP3ui.argtypes = (GLuint, GLenum, GLboolean, GLuint,)

glVertexAttribP3uiv = _gl.glVertexAttribP3uiv
glVertexAttribP3uiv.restype = None
glVertexAttribP3uiv.argtypes = (GLuint, GLenum, GLboolean, POINTER(GLuint),)

glVertexAttribP4ui = _gl.glVertexAttribP4ui
glVertexAttribP4ui.restype = None
glVertexAttribP4ui.argtypes = (GLuint, GLenum, GLboolean, GLuint,)

glVertexAttribP4uiv = _gl.glVertexAttribP4uiv
glVertexAttribP4uiv.restype = None
glVertexAttribP4uiv.argtypes = (GLuint, GLenum, GLboolean, POINTER(GLuint),)

GL_VERSION_4_0 = 1
GL_SAMPLE_SHADING = 0x8C36
GL_MIN_SAMPLE_SHADING_VALUE = 0x8C37
GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET = 0x8E5E
GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET = 0x8E5F
GL_TEXTURE_CUBE_MAP_ARRAY = 0x9009
GL_TEXTURE_BINDING_CUBE_MAP_ARRAY = 0x900A
GL_PROXY_TEXTURE_CUBE_MAP_ARRAY = 0x900B
GL_SAMPLER_CUBE_MAP_ARRAY = 0x900C
GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW = 0x900D
GL_INT_SAMPLER_CUBE_MAP_ARRAY = 0x900E
GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY = 0x900F
GL_DRAW_INDIRECT_BUFFER = 0x8F3F
GL_DRAW_INDIRECT_BUFFER_BINDING = 0x8F43
GL_GEOMETRY_SHADER_INVOCATIONS = 0x887F
GL_MAX_GEOMETRY_SHADER_INVOCATIONS = 0x8E5A
GL_MIN_FRAGMENT_INTERPOLATION_OFFSET = 0x8E5B
GL_MAX_FRAGMENT_INTERPOLATION_OFFSET = 0x8E5C
GL_FRAGMENT_INTERPOLATION_OFFSET_BITS = 0x8E5D
GL_MAX_VERTEX_STREAMS = 0x8E71
GL_DOUBLE_VEC2 = 0x8FFC
GL_DOUBLE_VEC3 = 0x8FFD
GL_DOUBLE_VEC4 = 0x8FFE
GL_DOUBLE_MAT2 = 0x8F46
GL_DOUBLE_MAT3 = 0x8F47
GL_DOUBLE_MAT4 = 0x8F48
GL_DOUBLE_MAT2x3 = 0x8F49
GL_DOUBLE_MAT2x4 = 0x8F4A
GL_DOUBLE_MAT3x2 = 0x8F4B
GL_DOUBLE_MAT3x4 = 0x8F4C
GL_DOUBLE_MAT4x2 = 0x8F4D
GL_DOUBLE_MAT4x3 = 0x8F4E
GL_ACTIVE_SUBROUTINES = 0x8DE5
GL_ACTIVE_SUBROUTINE_UNIFORMS = 0x8DE6
GL_ACTIVE_SUBROUTINE_UNIFORM_LOCATIONS = 0x8E47
GL_ACTIVE_SUBROUTINE_MAX_LENGTH = 0x8E48
GL_ACTIVE_SUBROUTINE_UNIFORM_MAX_LENGTH = 0x8E49
GL_MAX_SUBROUTINES = 0x8DE7
GL_MAX_SUBROUTINE_UNIFORM_LOCATIONS = 0x8DE8
GL_NUM_COMPATIBLE_SUBROUTINES = 0x8E4A
GL_COMPATIBLE_SUBROUTINES = 0x8E4B
GL_PATCHES = 0x000E
GL_PATCH_VERTICES = 0x8E72
GL_PATCH_DEFAULT_INNER_LEVEL = 0x8E73
GL_PATCH_DEFAULT_OUTER_LEVEL = 0x8E74
GL_TESS_CONTROL_OUTPUT_VERTICES = 0x8E75
GL_TESS_GEN_MODE = 0x8E76
GL_TESS_GEN_SPACING = 0x8E77
GL_TESS_GEN_VERTEX_ORDER = 0x8E78
GL_TESS_GEN_POINT_MODE = 0x8E79
GL_ISOLINES = 0x8E7A
GL_FRACTIONAL_ODD = 0x8E7B
GL_FRACTIONAL_EVEN = 0x8E7C
GL_MAX_PATCH_VERTICES = 0x8E7D
GL_MAX_TESS_GEN_LEVEL = 0x8E7E
GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS = 0x8E7F
GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS = 0x8E80
GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS = 0x8E81
GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS = 0x8E82
GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS = 0x8E83
GL_MAX_TESS_PATCH_COMPONENTS = 0x8E84
GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS = 0x8E85
GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS = 0x8E86
GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS = 0x8E89
GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS = 0x8E8A
GL_MAX_TESS_CONTROL_INPUT_COMPONENTS = 0x886C
GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS = 0x886D
GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS = 0x8E1E
GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS = 0x8E1F
GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_CONTROL_SHADER = 0x84F0
GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_EVALUATION_SHADER = 0x84F1
GL_TESS_EVALUATION_SHADER = 0x8E87
GL_TESS_CONTROL_SHADER = 0x8E88
GL_TRANSFORM_FEEDBACK = 0x8E22
GL_TRANSFORM_FEEDBACK_BUFFER_PAUSED = 0x8E23
GL_TRANSFORM_FEEDBACK_BUFFER_ACTIVE = 0x8E24
GL_TRANSFORM_FEEDBACK_BINDING = 0x8E25
GL_MAX_TRANSFORM_FEEDBACK_BUFFERS = 0x8E70
glMinSampleShading = _gl.glMinSampleShading
glMinSampleShading.restype = None
glMinSampleShading.argtypes = (GLfloat,)

glBlendEquationi = _gl.glBlendEquationi
glBlendEquationi.restype = None
glBlendEquationi.argtypes = (GLuint, GLenum,)

glBlendEquationSeparatei = _gl.glBlendEquationSeparatei
glBlendEquationSeparatei.restype = None
glBlendEquationSeparatei.argtypes = (GLuint, GLenum, GLenum,)

glBlendFunci = _gl.glBlendFunci
glBlendFunci.restype = None
glBlendFunci.argtypes = (GLuint, GLenum, GLenum,)

glBlendFuncSeparatei = _gl.glBlendFuncSeparatei
glBlendFuncSeparatei.restype = None
glBlendFuncSeparatei.argtypes = (GLuint, GLenum, GLenum, GLenum, GLenum,)

glDrawArraysIndirect = _gl.glDrawArraysIndirect
glDrawArraysIndirect.restype = None
glDrawArraysIndirect.argtypes = (GLenum, POINTER(None),)

glDrawElementsIndirect = _gl.glDrawElementsIndirect
glDrawElementsIndirect.restype = None
glDrawElementsIndirect.argtypes = (GLenum, GLenum, POINTER(None),)

glUniform1d = _gl.glUniform1d
glUniform1d.restype = None
glUniform1d.argtypes = (GLint, GLdouble,)

glUniform2d = _gl.glUniform2d
glUniform2d.restype = None
glUniform2d.argtypes = (GLint, GLdouble, GLdouble,)

glUniform3d = _gl.glUniform3d
glUniform3d.restype = None
glUniform3d.argtypes = (GLint, GLdouble, GLdouble, GLdouble,)

glUniform4d = _gl.glUniform4d
glUniform4d.restype = None
glUniform4d.argtypes = (GLint, GLdouble, GLdouble, GLdouble, GLdouble,)

glUniform1dv = _gl.glUniform1dv
glUniform1dv.restype = None
glUniform1dv.argtypes = (GLint, GLsizei, POINTER(GLdouble),)

glUniform2dv = _gl.glUniform2dv
glUniform2dv.restype = None
glUniform2dv.argtypes = (GLint, GLsizei, POINTER(GLdouble),)

glUniform3dv = _gl.glUniform3dv
glUniform3dv.restype = None
glUniform3dv.argtypes = (GLint, GLsizei, POINTER(GLdouble),)

glUniform4dv = _gl.glUniform4dv
glUniform4dv.restype = None
glUniform4dv.argtypes = (GLint, GLsizei, POINTER(GLdouble),)

glUniformMatrix2dv = _gl.glUniformMatrix2dv
glUniformMatrix2dv.restype = None
glUniformMatrix2dv.argtypes = (GLint, GLsizei, GLboolean, POINTER(GLdouble),)

glUniformMatrix3dv = _gl.glUniformMatrix3dv
glUniformMatrix3dv.restype = None
glUniformMatrix3dv.argtypes = (GLint, GLsizei, GLboolean, POINTER(GLdouble),)

glUniformMatrix4dv = _gl.glUniformMatrix4dv
glUniformMatrix4dv.restype = None
glUniformMatrix4dv.argtypes = (GLint, GLsizei, GLboolean, POINTER(GLdouble),)

glUniformMatrix2x3dv = _gl.glUniformMatrix2x3dv
glUniformMatrix2x3dv.restype = None
glUniformMatrix2x3dv.argtypes = (GLint, GLsizei, GLboolean, POINTER(GLdouble),)

glUniformMatrix2x4dv = _gl.glUniformMatrix2x4dv
glUniformMatrix2x4dv.restype = None
glUniformMatrix2x4dv.argtypes = (GLint, GLsizei, GLboolean, POINTER(GLdouble),)

glUniformMatrix3x2dv = _gl.glUniformMatrix3x2dv
glUniformMatrix3x2dv.restype = None
glUniformMatrix3x2dv.argtypes = (GLint, GLsizei, GLboolean, POINTER(GLdouble),)

glUniformMatrix3x4dv = _gl.glUniformMatrix3x4dv
glUniformMatrix3x4dv.restype = None
glUniformMatrix3x4dv.argtypes = (GLint, GLsizei, GLboolean, POINTER(GLdouble),)

glUniformMatrix4x2dv = _gl.glUniformMatrix4x2dv
glUniformMatrix4x2dv.restype = None
glUniformMatrix4x2dv.argtypes = (GLint, GLsizei, GLboolean, POINTER(GLdouble),)

glUniformMatrix4x3dv = _gl.glUniformMatrix4x3dv
glUniformMatrix4x3dv.restype = None
glUniformMatrix4x3dv.argtypes = (GLint, GLsizei, GLboolean, POINTER(GLdouble),)

glGetUniformdv = _gl.glGetUniformdv
glGetUniformdv.restype = None
glGetUniformdv.argtypes = (GLuint, GLint, POINTER(GLdouble),)

glGetSubroutineUniformLocation = _gl.glGetSubroutineUniformLocation
glGetSubroutineUniformLocation.restype = GLint
glGetSubroutineUniformLocation.argtypes = (GLuint, GLenum, STRING,)

glGetSubroutineIndex = _gl.glGetSubroutineIndex
glGetSubroutineIndex.restype = GLuint
glGetSubroutineIndex.argtypes = (GLuint, GLenum, STRING,)

glGetActiveSubroutineUniformiv = _gl.glGetActiveSubroutineUniformiv
glGetActiveSubroutineUniformiv.restype = None
glGetActiveSubroutineUniformiv.argtypes = (GLuint, GLenum, GLuint, GLenum, POINTER(GLint),)

glGetActiveSubroutineUniformName = _gl.glGetActiveSubroutineUniformName
glGetActiveSubroutineUniformName.restype = None
glGetActiveSubroutineUniformName.argtypes = (GLuint, GLenum, GLuint, GLsizei, POINTER(GLsizei), STRING,)

glGetActiveSubroutineName = _gl.glGetActiveSubroutineName
glGetActiveSubroutineName.restype = None
glGetActiveSubroutineName.argtypes = (GLuint, GLenum, GLuint, GLsizei, POINTER(GLsizei), STRING,)

glUniformSubroutinesuiv = _gl.glUniformSubroutinesuiv
glUniformSubroutinesuiv.restype = None
glUniformSubroutinesuiv.argtypes = (GLenum, GLsizei, POINTER(GLuint),)

glGetUniformSubroutineuiv = _gl.glGetUniformSubroutineuiv
glGetUniformSubroutineuiv.restype = None
glGetUniformSubroutineuiv.argtypes = (GLenum, GLint, POINTER(GLuint),)

glGetProgramStageiv = _gl.glGetProgramStageiv
glGetProgramStageiv.restype = None
glGetProgramStageiv.argtypes = (GLuint, GLenum, GLenum, POINTER(GLint),)

glPatchParameteri = _gl.glPatchParameteri
glPatchParameteri.restype = None
glPatchParameteri.argtypes = (GLenum, GLint,)

glPatchParameterfv = _gl.glPatchParameterfv
glPatchParameterfv.restype = None
glPatchParameterfv.argtypes = (GLenum, POINTER(GLfloat),)

glBindTransformFeedback = _gl.glBindTransformFeedback
glBindTransformFeedback.restype = None
glBindTransformFeedback.argtypes = (GLenum, GLuint,)

glDeleteTransformFeedbacks = _gl.glDeleteTransformFeedbacks
glDeleteTransformFeedbacks.restype = None
glDeleteTransformFeedbacks.argtypes = (GLsizei, POINTER(GLuint),)

glGenTransformFeedbacks = _gl.glGenTransformFeedbacks
glGenTransformFeedbacks.restype = None
glGenTransformFeedbacks.argtypes = (GLsizei, POINTER(GLuint),)

glIsTransformFeedback = _gl.glIsTransformFeedback
glIsTransformFeedback.restype = GLboolean
glIsTransformFeedback.argtypes = (GLuint,)

glPauseTransformFeedback = _gl.glPauseTransformFeedback
glPauseTransformFeedback.restype = None
glPauseTransformFeedback.argtypes = ()

glResumeTransformFeedback = _gl.glResumeTransformFeedback
glResumeTransformFeedback.restype = None
glResumeTransformFeedback.argtypes = ()

glDrawTransformFeedback = _gl.glDrawTransformFeedback
glDrawTransformFeedback.restype = None
glDrawTransformFeedback.argtypes = (GLenum, GLuint,)

glDrawTransformFeedbackStream = _gl.glDrawTransformFeedbackStream
glDrawTransformFeedbackStream.restype = None
glDrawTransformFeedbackStream.argtypes = (GLenum, GLuint, GLuint,)

glBeginQueryIndexed = _gl.glBeginQueryIndexed
glBeginQueryIndexed.restype = None
glBeginQueryIndexed.argtypes = (GLenum, GLuint, GLuint,)

glEndQueryIndexed = _gl.glEndQueryIndexed
glEndQueryIndexed.restype = None
glEndQueryIndexed.argtypes = (GLenum, GLuint,)

glGetQueryIndexediv = _gl.glGetQueryIndexediv
glGetQueryIndexediv.restype = None
glGetQueryIndexediv.argtypes = (GLenum, GLuint, GLenum, POINTER(GLint),)

GL_VERSION_4_1 = 1
GL_FIXED = 0x140C
GL_IMPLEMENTATION_COLOR_READ_TYPE = 0x8B9A
GL_IMPLEMENTATION_COLOR_READ_FORMAT = 0x8B9B
GL_LOW_FLOAT = 0x8DF0
GL_MEDIUM_FLOAT = 0x8DF1
GL_HIGH_FLOAT = 0x8DF2
GL_LOW_INT = 0x8DF3
GL_MEDIUM_INT = 0x8DF4
GL_HIGH_INT = 0x8DF5
GL_SHADER_COMPILER = 0x8DFA
GL_SHADER_BINARY_FORMATS = 0x8DF8
GL_NUM_SHADER_BINARY_FORMATS = 0x8DF9
GL_MAX_VERTEX_UNIFORM_VECTORS = 0x8DFB
GL_MAX_VARYING_VECTORS = 0x8DFC
GL_MAX_FRAGMENT_UNIFORM_VECTORS = 0x8DFD
GL_RGB565 = 0x8D62
GL_PROGRAM_BINARY_RETRIEVABLE_HINT = 0x8257
GL_PROGRAM_BINARY_LENGTH = 0x8741
GL_NUM_PROGRAM_BINARY_FORMATS = 0x87FE
GL_PROGRAM_BINARY_FORMATS = 0x87FF
GL_VERTEX_SHADER_BIT = 0x00000001
GL_FRAGMENT_SHADER_BIT = 0x00000002
GL_GEOMETRY_SHADER_BIT = 0x00000004
GL_TESS_CONTROL_SHADER_BIT = 0x00000008
GL_TESS_EVALUATION_SHADER_BIT = 0x00000010
GL_ALL_SHADER_BITS = 0xFFFFFFFF
GL_PROGRAM_SEPARABLE = 0x8258
GL_ACTIVE_PROGRAM = 0x8259
GL_PROGRAM_PIPELINE_BINDING = 0x825A
GL_MAX_VIEWPORTS = 0x825B
GL_VIEWPORT_SUBPIXEL_BITS = 0x825C
GL_VIEWPORT_BOUNDS_RANGE = 0x825D
GL_LAYER_PROVOKING_VERTEX = 0x825E
GL_VIEWPORT_INDEX_PROVOKING_VERTEX = 0x825F
GL_UNDEFINED_VERTEX = 0x8260
glReleaseShaderCompiler = _gl.glReleaseShaderCompiler
glReleaseShaderCompiler.restype = None
glReleaseShaderCompiler.argtypes = ()

glShaderBinary = _gl.glShaderBinary
glShaderBinary.restype = None
glShaderBinary.argtypes = (GLsizei, POINTER(GLuint), GLenum, POINTER(None), GLsizei,)

glGetShaderPrecisionFormat = _gl.glGetShaderPrecisionFormat
glGetShaderPrecisionFormat.restype = None
glGetShaderPrecisionFormat.argtypes = (GLenum, GLenum, POINTER(GLint), POINTER(GLint),)

glDepthRangef = _gl.glDepthRangef
glDepthRangef.restype = None
glDepthRangef.argtypes = (GLfloat, GLfloat,)

glClearDepthf = _gl.glClearDepthf
glClearDepthf.restype = None
glClearDepthf.argtypes = (GLfloat,)

glGetProgramBinary = _gl.glGetProgramBinary
glGetProgramBinary.restype = None
glGetProgramBinary.argtypes = (GLuint, GLsizei, POINTER(GLsizei), POINTER(GLenum), POINTER(None),)

glProgramBinary = _gl.glProgramBinary
glProgramBinary.restype = None
glProgramBinary.argtypes = (GLuint, GLenum, POINTER(None), GLsizei,)

glProgramParameteri = _gl.glProgramParameteri
glProgramParameteri.restype = None
glProgramParameteri.argtypes = (GLuint, GLenum, GLint,)

glUseProgramStages = _gl.glUseProgramStages
glUseProgramStages.restype = None
glUseProgramStages.argtypes = (GLuint, GLbitfield, GLuint,)

glActiveShaderProgram = _gl.glActiveShaderProgram
glActiveShaderProgram.restype = None
glActiveShaderProgram.argtypes = (GLuint, GLuint,)

glCreateShaderProgramv = _gl.glCreateShaderProgramv
glCreateShaderProgramv.restype = GLuint
glCreateShaderProgramv.argtypes = (GLenum, GLsizei, POINTER(STRING),)

glBindProgramPipeline = _gl.glBindProgramPipeline
glBindProgramPipeline.restype = None
glBindProgramPipeline.argtypes = (GLuint,)

glDeleteProgramPipelines = _gl.glDeleteProgramPipelines
glDeleteProgramPipelines.restype = None
glDeleteProgramPipelines.argtypes = (GLsizei, POINTER(GLuint),)

glGenProgramPipelines = _gl.glGenProgramPipelines
glGenProgramPipelines.restype = None
glGenProgramPipelines.argtypes = (GLsizei, POINTER(GLuint),)

glIsProgramPipeline = _gl.glIsProgramPipeline
glIsProgramPipeline.restype = GLboolean
glIsProgramPipeline.argtypes = (GLuint,)

glGetProgramPipelineiv = _gl.glGetProgramPipelineiv
glGetProgramPipelineiv.restype = None
glGetProgramPipelineiv.argtypes = (GLuint, GLenum, POINTER(GLint),)

glProgramUniform1i = _gl.glProgramUniform1i
glProgramUniform1i.restype = None
glProgramUniform1i.argtypes = (GLuint, GLint, GLint,)

glProgramUniform1iv = _gl.glProgramUniform1iv
glProgramUniform1iv.restype = None
glProgramUniform1iv.argtypes = (GLuint, GLint, GLsizei, POINTER(GLint),)

glProgramUniform1f = _gl.glProgramUniform1f
glProgramUniform1f.restype = None
glProgramUniform1f.argtypes = (GLuint, GLint, GLfloat,)

glProgramUniform1fv = _gl.glProgramUniform1fv
glProgramUniform1fv.restype = None
glProgramUniform1fv.argtypes = (GLuint, GLint, GLsizei, POINTER(GLfloat),)

glProgramUniform1d = _gl.glProgramUniform1d
glProgramUniform1d.restype = None
glProgramUniform1d.argtypes = (GLuint, GLint, GLdouble,)

glProgramUniform1dv = _gl.glProgramUniform1dv
glProgramUniform1dv.restype = None
glProgramUniform1dv.argtypes = (GLuint, GLint, GLsizei, POINTER(GLdouble),)

glProgramUniform1ui = _gl.glProgramUniform1ui
glProgramUniform1ui.restype = None
glProgramUniform1ui.argtypes = (GLuint, GLint, GLuint,)

glProgramUniform1uiv = _gl.glProgramUniform1uiv
glProgramUniform1uiv.restype = None
glProgramUniform1uiv.argtypes = (GLuint, GLint, GLsizei, POINTER(GLuint),)

glProgramUniform2i = _gl.glProgramUniform2i
glProgramUniform2i.restype = None
glProgramUniform2i.argtypes = (GLuint, GLint, GLint, GLint,)

glProgramUniform2iv = _gl.glProgramUniform2iv
glProgramUniform2iv.restype = None
glProgramUniform2iv.argtypes = (GLuint, GLint, GLsizei, POINTER(GLint),)

glProgramUniform2f = _gl.glProgramUniform2f
glProgramUniform2f.restype = None
glProgramUniform2f.argtypes = (GLuint, GLint, GLfloat, GLfloat,)

glProgramUniform2fv = _gl.glProgramUniform2fv
glProgramUniform2fv.restype = None
glProgramUniform2fv.argtypes = (GLuint, GLint, GLsizei, POINTER(GLfloat),)

glProgramUniform2d = _gl.glProgramUniform2d
glProgramUniform2d.restype = None
glProgramUniform2d.argtypes = (GLuint, GLint, GLdouble, GLdouble,)

glProgramUniform2dv = _gl.glProgramUniform2dv
glProgramUniform2dv.restype = None
glProgramUniform2dv.argtypes = (GLuint, GLint, GLsizei, POINTER(GLdouble),)

glProgramUniform2ui = _gl.glProgramUniform2ui
glProgramUniform2ui.restype = None
glProgramUniform2ui.argtypes = (GLuint, GLint, GLuint, GLuint,)

glProgramUniform2uiv = _gl.glProgramUniform2uiv
glProgramUniform2uiv.restype = None
glProgramUniform2uiv.argtypes = (GLuint, GLint, GLsizei, POINTER(GLuint),)

glProgramUniform3i = _gl.glProgramUniform3i
glProgramUniform3i.restype = None
glProgramUniform3i.argtypes = (GLuint, GLint, GLint, GLint, GLint,)

glProgramUniform3iv = _gl.glProgramUniform3iv
glProgramUniform3iv.restype = None
glProgramUniform3iv.argtypes = (GLuint, GLint, GLsizei, POINTER(GLint),)

glProgramUniform3f = _gl.glProgramUniform3f
glProgramUniform3f.restype = None
glProgramUniform3f.argtypes = (GLuint, GLint, GLfloat, GLfloat, GLfloat,)

glProgramUniform3fv = _gl.glProgramUniform3fv
glProgramUniform3fv.restype = None
glProgramUniform3fv.argtypes = (GLuint, GLint, GLsizei, POINTER(GLfloat),)

glProgramUniform3d = _gl.glProgramUniform3d
glProgramUniform3d.restype = None
glProgramUniform3d.argtypes = (GLuint, GLint, GLdouble, GLdouble, GLdouble,)

glProgramUniform3dv = _gl.glProgramUniform3dv
glProgramUniform3dv.restype = None
glProgramUniform3dv.argtypes = (GLuint, GLint, GLsizei, POINTER(GLdouble),)

glProgramUniform3ui = _gl.glProgramUniform3ui
glProgramUniform3ui.restype = None
glProgramUniform3ui.argtypes = (GLuint, GLint, GLuint, GLuint, GLuint,)

glProgramUniform3uiv = _gl.glProgramUniform3uiv
glProgramUniform3uiv.restype = None
glProgramUniform3uiv.argtypes = (GLuint, GLint, GLsizei, POINTER(GLuint),)

glProgramUniform4i = _gl.glProgramUniform4i
glProgramUniform4i.restype = None
glProgramUniform4i.argtypes = (GLuint, GLint, GLint, GLint, GLint, GLint,)

glProgramUniform4iv = _gl.glProgramUniform4iv
glProgramUniform4iv.restype = None
glProgramUniform4iv.argtypes = (GLuint, GLint, GLsizei, POINTER(GLint),)

glProgramUniform4f = _gl.glProgramUniform4f
glProgramUniform4f.restype = None
glProgramUniform4f.argtypes = (GLuint, GLint, GLfloat, GLfloat, GLfloat, GLfloat,)

glProgramUniform4fv = _gl.glProgramUniform4fv
glProgramUniform4fv.restype = None
glProgramUniform4fv.argtypes = (GLuint, GLint, GLsizei, POINTER(GLfloat),)

glProgramUniform4d = _gl.glProgramUniform4d
glProgramUniform4d.restype = None
glProgramUniform4d.argtypes = (GLuint, GLint, GLdouble, GLdouble, GLdouble, GLdouble,)

glProgramUniform4dv = _gl.glProgramUniform4dv
glProgramUniform4dv.restype = None
glProgramUniform4dv.argtypes = (GLuint, GLint, GLsizei, POINTER(GLdouble),)

glProgramUniform4ui = _gl.glProgramUniform4ui
glProgramUniform4ui.restype = None
glProgramUniform4ui.argtypes = (GLuint, GLint, GLuint, GLuint, GLuint, GLuint,)

glProgramUniform4uiv = _gl.glProgramUniform4uiv
glProgramUniform4uiv.restype = None
glProgramUniform4uiv.argtypes = (GLuint, GLint, GLsizei, POINTER(GLuint),)

glProgramUniformMatrix2fv = _gl.glProgramUniformMatrix2fv
glProgramUniformMatrix2fv.restype = None
glProgramUniformMatrix2fv.argtypes = (GLuint, GLint, GLsizei, GLboolean, POINTER(GLfloat),)

glProgramUniformMatrix3fv = _gl.glProgramUniformMatrix3fv
glProgramUniformMatrix3fv.restype = None
glProgramUniformMatrix3fv.argtypes = (GLuint, GLint, GLsizei, GLboolean, POINTER(GLfloat),)

glProgramUniformMatrix4fv = _gl.glProgramUniformMatrix4fv
glProgramUniformMatrix4fv.restype = None
glProgramUniformMatrix4fv.argtypes = (GLuint, GLint, GLsizei, GLboolean, POINTER(GLfloat),)

glProgramUniformMatrix2dv = _gl.glProgramUniformMatrix2dv
glProgramUniformMatrix2dv.restype = None
glProgramUniformMatrix2dv.argtypes = (GLuint, GLint, GLsizei, GLboolean, POINTER(GLdouble),)

glProgramUniformMatrix3dv = _gl.glProgramUniformMatrix3dv
glProgramUniformMatrix3dv.restype = None
glProgramUniformMatrix3dv.argtypes = (GLuint, GLint, GLsizei, GLboolean, POINTER(GLdouble),)

glProgramUniformMatrix4dv = _gl.glProgramUniformMatrix4dv
glProgramUniformMatrix4dv.restype = None
glProgramUniformMatrix4dv.argtypes = (GLuint, GLint, GLsizei, GLboolean, POINTER(GLdouble),)

glProgramUniformMatrix2x3fv = _gl.glProgramUniformMatrix2x3fv
glProgramUniformMatrix2x3fv.restype = None
glProgramUniformMatrix2x3fv.argtypes = (GLuint, GLint, GLsizei, GLboolean, POINTER(GLfloat),)

glProgramUniformMatrix3x2fv = _gl.glProgramUniformMatrix3x2fv
glProgramUniformMatrix3x2fv.restype = None
glProgramUniformMatrix3x2fv.argtypes = (GLuint, GLint, GLsizei, GLboolean, POINTER(GLfloat),)

glProgramUniformMatrix2x4fv = _gl.glProgramUniformMatrix2x4fv
glProgramUniformMatrix2x4fv.restype = None
glProgramUniformMatrix2x4fv.argtypes = (GLuint, GLint, GLsizei, GLboolean, POINTER(GLfloat),)

glProgramUniformMatrix4x2fv = _gl.glProgramUniformMatrix4x2fv
glProgramUniformMatrix4x2fv.restype = None
glProgramUniformMatrix4x2fv.argtypes = (GLuint, GLint, GLsizei, GLboolean, POINTER(GLfloat),)

glProgramUniformMatrix3x4fv = _gl.glProgramUniformMatrix3x4fv
glProgramUniformMatrix3x4fv.restype = None
glProgramUniformMatrix3x4fv.argtypes = (GLuint, GLint, GLsizei, GLboolean, POINTER(GLfloat),)

glProgramUniformMatrix4x3fv = _gl.glProgramUniformMatrix4x3fv
glProgramUniformMatrix4x3fv.restype = None
glProgramUniformMatrix4x3fv.argtypes = (GLuint, GLint, GLsizei, GLboolean, POINTER(GLfloat),)

glProgramUniformMatrix2x3dv = _gl.glProgramUniformMatrix2x3dv
glProgramUniformMatrix2x3dv.restype = None
glProgramUniformMatrix2x3dv.argtypes = (GLuint, GLint, GLsizei, GLboolean, POINTER(GLdouble),)

glProgramUniformMatrix3x2dv = _gl.glProgramUniformMatrix3x2dv
glProgramUniformMatrix3x2dv.restype = None
glProgramUniformMatrix3x2dv.argtypes = (GLuint, GLint, GLsizei, GLboolean, POINTER(GLdouble),)

glProgramUniformMatrix2x4dv = _gl.glProgramUniformMatrix2x4dv
glProgramUniformMatrix2x4dv.restype = None
glProgramUniformMatrix2x4dv.argtypes = (GLuint, GLint, GLsizei, GLboolean, POINTER(GLdouble),)

glProgramUniformMatrix4x2dv = _gl.glProgramUniformMatrix4x2dv
glProgramUniformMatrix4x2dv.restype = None
glProgramUniformMatrix4x2dv.argtypes = (GLuint, GLint, GLsizei, GLboolean, POINTER(GLdouble),)

glProgramUniformMatrix3x4dv = _gl.glProgramUniformMatrix3x4dv
glProgramUniformMatrix3x4dv.restype = None
glProgramUniformMatrix3x4dv.argtypes = (GLuint, GLint, GLsizei, GLboolean, POINTER(GLdouble),)

glProgramUniformMatrix4x3dv = _gl.glProgramUniformMatrix4x3dv
glProgramUniformMatrix4x3dv.restype = None
glProgramUniformMatrix4x3dv.argtypes = (GLuint, GLint, GLsizei, GLboolean, POINTER(GLdouble),)

glValidateProgramPipeline = _gl.glValidateProgramPipeline
glValidateProgramPipeline.restype = None
glValidateProgramPipeline.argtypes = (GLuint,)

glGetProgramPipelineInfoLog = _gl.glGetProgramPipelineInfoLog
glGetProgramPipelineInfoLog.restype = None
glGetProgramPipelineInfoLog.argtypes = (GLuint, GLsizei, POINTER(GLsizei), STRING,)

glVertexAttribL1d = _gl.glVertexAttribL1d
glVertexAttribL1d.restype = None
glVertexAttribL1d.argtypes = (GLuint, GLdouble,)

glVertexAttribL2d = _gl.glVertexAttribL2d
glVertexAttribL2d.restype = None
glVertexAttribL2d.argtypes = (GLuint, GLdouble, GLdouble,)

glVertexAttribL3d = _gl.glVertexAttribL3d
glVertexAttribL3d.restype = None
glVertexAttribL3d.argtypes = (GLuint, GLdouble, GLdouble, GLdouble,)

glVertexAttribL4d = _gl.glVertexAttribL4d
glVertexAttribL4d.restype = None
glVertexAttribL4d.argtypes = (GLuint, GLdouble, GLdouble, GLdouble, GLdouble,)

glVertexAttribL1dv = _gl.glVertexAttribL1dv
glVertexAttribL1dv.restype = None
glVertexAttribL1dv.argtypes = (GLuint, POINTER(GLdouble),)

glVertexAttribL2dv = _gl.glVertexAttribL2dv
glVertexAttribL2dv.restype = None
glVertexAttribL2dv.argtypes = (GLuint, POINTER(GLdouble),)

glVertexAttribL3dv = _gl.glVertexAttribL3dv
glVertexAttribL3dv.restype = None
glVertexAttribL3dv.argtypes = (GLuint, POINTER(GLdouble),)

glVertexAttribL4dv = _gl.glVertexAttribL4dv
glVertexAttribL4dv.restype = None
glVertexAttribL4dv.argtypes = (GLuint, POINTER(GLdouble),)

glVertexAttribLPointer = _gl.glVertexAttribLPointer
glVertexAttribLPointer.restype = None
glVertexAttribLPointer.argtypes = (GLuint, GLint, GLenum, GLsizei, POINTER(None),)

glGetVertexAttribLdv = _gl.glGetVertexAttribLdv
glGetVertexAttribLdv.restype = None
glGetVertexAttribLdv.argtypes = (GLuint, GLenum, POINTER(GLdouble),)

glViewportArrayv = _gl.glViewportArrayv
glViewportArrayv.restype = None
glViewportArrayv.argtypes = (GLuint, GLsizei, POINTER(GLfloat),)

glViewportIndexedf = _gl.glViewportIndexedf
glViewportIndexedf.restype = None
glViewportIndexedf.argtypes = (GLuint, GLfloat, GLfloat, GLfloat, GLfloat,)

glViewportIndexedfv = _gl.glViewportIndexedfv
glViewportIndexedfv.restype = None
glViewportIndexedfv.argtypes = (GLuint, POINTER(GLfloat),)

glScissorArrayv = _gl.glScissorArrayv
glScissorArrayv.restype = None
glScissorArrayv.argtypes = (GLuint, GLsizei, POINTER(GLint),)

glScissorIndexed = _gl.glScissorIndexed
glScissorIndexed.restype = None
glScissorIndexed.argtypes = (GLuint, GLint, GLint, GLsizei, GLsizei,)

glScissorIndexedv = _gl.glScissorIndexedv
glScissorIndexedv.restype = None
glScissorIndexedv.argtypes = (GLuint, POINTER(GLint),)

glDepthRangeArrayv = _gl.glDepthRangeArrayv
glDepthRangeArrayv.restype = None
glDepthRangeArrayv.argtypes = (GLuint, GLsizei, POINTER(GLdouble),)

glDepthRangeIndexed = _gl.glDepthRangeIndexed
glDepthRangeIndexed.restype = None
glDepthRangeIndexed.argtypes = (GLuint, GLdouble, GLdouble,)

glGetFloati_v = _gl.glGetFloati_v
glGetFloati_v.restype = None
glGetFloati_v.argtypes = (GLenum, GLuint, POINTER(GLfloat),)

glGetDoublei_v = _gl.glGetDoublei_v
glGetDoublei_v.restype = None
glGetDoublei_v.argtypes = (GLenum, GLuint, POINTER(GLdouble),)

GL_VERSION_4_2 = 1
GL_COPY_READ_BUFFER_BINDING = 0x8F36
GL_COPY_WRITE_BUFFER_BINDING = 0x8F37
GL_TRANSFORM_FEEDBACK_ACTIVE = 0x8E24
GL_TRANSFORM_FEEDBACK_PAUSED = 0x8E23
GL_UNPACK_COMPRESSED_BLOCK_WIDTH = 0x9127
GL_UNPACK_COMPRESSED_BLOCK_HEIGHT = 0x9128
GL_UNPACK_COMPRESSED_BLOCK_DEPTH = 0x9129
GL_UNPACK_COMPRESSED_BLOCK_SIZE = 0x912A
GL_PACK_COMPRESSED_BLOCK_WIDTH = 0x912B
GL_PACK_COMPRESSED_BLOCK_HEIGHT = 0x912C
GL_PACK_COMPRESSED_BLOCK_DEPTH = 0x912D
GL_PACK_COMPRESSED_BLOCK_SIZE = 0x912E
GL_NUM_SAMPLE_COUNTS = 0x9380
GL_MIN_MAP_BUFFER_ALIGNMENT = 0x90BC
GL_ATOMIC_COUNTER_BUFFER = 0x92C0
GL_ATOMIC_COUNTER_BUFFER_BINDING = 0x92C1
GL_ATOMIC_COUNTER_BUFFER_START = 0x92C2
GL_ATOMIC_COUNTER_BUFFER_SIZE = 0x92C3
GL_ATOMIC_COUNTER_BUFFER_DATA_SIZE = 0x92C4
GL_ATOMIC_COUNTER_BUFFER_ACTIVE_ATOMIC_COUNTERS = 0x92C5
GL_ATOMIC_COUNTER_BUFFER_ACTIVE_ATOMIC_COUNTER_INDICES = 0x92C6
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_VERTEX_SHADER = 0x92C7
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TESS_CONTROL_SHADER = 0x92C8
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TESS_EVALUATION_SHADER = 0x92C9
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_GEOMETRY_SHADER = 0x92CA
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_FRAGMENT_SHADER = 0x92CB
GL_MAX_VERTEX_ATOMIC_COUNTER_BUFFERS = 0x92CC
GL_MAX_TESS_CONTROL_ATOMIC_COUNTER_BUFFERS = 0x92CD
GL_MAX_TESS_EVALUATION_ATOMIC_COUNTER_BUFFERS = 0x92CE
GL_MAX_GEOMETRY_ATOMIC_COUNTER_BUFFERS = 0x92CF
GL_MAX_FRAGMENT_ATOMIC_COUNTER_BUFFERS = 0x92D0
GL_MAX_COMBINED_ATOMIC_COUNTER_BUFFERS = 0x92D1
GL_MAX_VERTEX_ATOMIC_COUNTERS = 0x92D2
GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS = 0x92D3
GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS = 0x92D4
GL_MAX_GEOMETRY_ATOMIC_COUNTERS = 0x92D5
GL_MAX_FRAGMENT_ATOMIC_COUNTERS = 0x92D6
GL_MAX_COMBINED_ATOMIC_COUNTERS = 0x92D7
GL_MAX_ATOMIC_COUNTER_BUFFER_SIZE = 0x92D8
GL_MAX_ATOMIC_COUNTER_BUFFER_BINDINGS = 0x92DC
GL_ACTIVE_ATOMIC_COUNTER_BUFFERS = 0x92D9
GL_UNIFORM_ATOMIC_COUNTER_BUFFER_INDEX = 0x92DA
GL_UNSIGNED_INT_ATOMIC_COUNTER = 0x92DB
GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT = 0x00000001
GL_ELEMENT_ARRAY_BARRIER_BIT = 0x00000002
GL_UNIFORM_BARRIER_BIT = 0x00000004
GL_TEXTURE_FETCH_BARRIER_BIT = 0x00000008
GL_SHADER_IMAGE_ACCESS_BARRIER_BIT = 0x00000020
GL_COMMAND_BARRIER_BIT = 0x00000040
GL_PIXEL_BUFFER_BARRIER_BIT = 0x00000080
GL_TEXTURE_UPDATE_BARRIER_BIT = 0x00000100
GL_BUFFER_UPDATE_BARRIER_BIT = 0x00000200
GL_FRAMEBUFFER_BARRIER_BIT = 0x00000400
GL_TRANSFORM_FEEDBACK_BARRIER_BIT = 0x00000800
GL_ATOMIC_COUNTER_BARRIER_BIT = 0x00001000
GL_ALL_BARRIER_BITS = 0xFFFFFFFF
GL_MAX_IMAGE_UNITS = 0x8F38
GL_MAX_COMBINED_IMAGE_UNITS_AND_FRAGMENT_OUTPUTS = 0x8F39
GL_IMAGE_BINDING_NAME = 0x8F3A
GL_IMAGE_BINDING_LEVEL = 0x8F3B
GL_IMAGE_BINDING_LAYERED = 0x8F3C
GL_IMAGE_BINDING_LAYER = 0x8F3D
GL_IMAGE_BINDING_ACCESS = 0x8F3E
GL_IMAGE_1D = 0x904C
GL_IMAGE_2D = 0x904D
GL_IMAGE_3D = 0x904E
GL_IMAGE_2D_RECT = 0x904F
GL_IMAGE_CUBE = 0x9050
GL_IMAGE_BUFFER = 0x9051
GL_IMAGE_1D_ARRAY = 0x9052
GL_IMAGE_2D_ARRAY = 0x9053
GL_IMAGE_CUBE_MAP_ARRAY = 0x9054
GL_IMAGE_2D_MULTISAMPLE = 0x9055
GL_IMAGE_2D_MULTISAMPLE_ARRAY = 0x9056
GL_INT_IMAGE_1D = 0x9057
GL_INT_IMAGE_2D = 0x9058
GL_INT_IMAGE_3D = 0x9059
GL_INT_IMAGE_2D_RECT = 0x905A
GL_INT_IMAGE_CUBE = 0x905B
GL_INT_IMAGE_BUFFER = 0x905C
GL_INT_IMAGE_1D_ARRAY = 0x905D
GL_INT_IMAGE_2D_ARRAY = 0x905E
GL_INT_IMAGE_CUBE_MAP_ARRAY = 0x905F
GL_INT_IMAGE_2D_MULTISAMPLE = 0x9060
GL_INT_IMAGE_2D_MULTISAMPLE_ARRAY = 0x9061
GL_UNSIGNED_INT_IMAGE_1D = 0x9062
GL_UNSIGNED_INT_IMAGE_2D = 0x9063
GL_UNSIGNED_INT_IMAGE_3D = 0x9064
GL_UNSIGNED_INT_IMAGE_2D_RECT = 0x9065
GL_UNSIGNED_INT_IMAGE_CUBE = 0x9066
GL_UNSIGNED_INT_IMAGE_BUFFER = 0x9067
GL_UNSIGNED_INT_IMAGE_1D_ARRAY = 0x9068
GL_UNSIGNED_INT_IMAGE_2D_ARRAY = 0x9069
GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY = 0x906A
GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE = 0x906B
GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_ARRAY = 0x906C
GL_MAX_IMAGE_SAMPLES = 0x906D
GL_IMAGE_BINDING_FORMAT = 0x906E
GL_IMAGE_FORMAT_COMPATIBILITY_TYPE = 0x90C7
GL_IMAGE_FORMAT_COMPATIBILITY_BY_SIZE = 0x90C8
GL_IMAGE_FORMAT_COMPATIBILITY_BY_CLASS = 0x90C9
GL_MAX_VERTEX_IMAGE_UNIFORMS = 0x90CA
GL_MAX_TESS_CONTROL_IMAGE_UNIFORMS = 0x90CB
GL_MAX_TESS_EVALUATION_IMAGE_UNIFORMS = 0x90CC
GL_MAX_GEOMETRY_IMAGE_UNIFORMS = 0x90CD
GL_MAX_FRAGMENT_IMAGE_UNIFORMS = 0x90CE
GL_MAX_COMBINED_IMAGE_UNIFORMS = 0x90CF
GL_COMPRESSED_RGBA_BPTC_UNORM = 0x8E8C
GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM = 0x8E8D
GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT = 0x8E8E
GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT = 0x8E8F
GL_TEXTURE_IMMUTABLE_FORMAT = 0x912F
glDrawArraysInstancedBaseInstance = _gl.glDrawArraysInstancedBaseInstance
glDrawArraysInstancedBaseInstance.restype = None
glDrawArraysInstancedBaseInstance.argtypes = (GLenum, GLint, GLsizei, GLsizei, GLuint,)

glDrawElementsInstancedBaseInstance = _gl.glDrawElementsInstancedBaseInstance
glDrawElementsInstancedBaseInstance.restype = None
glDrawElementsInstancedBaseInstance.argtypes = (GLenum, GLsizei, GLenum, POINTER(None), GLsizei, GLuint,)

glDrawElementsInstancedBaseVertexBaseInstance = _gl.glDrawElementsInstancedBaseVertexBaseInstance
glDrawElementsInstancedBaseVertexBaseInstance.restype = None
glDrawElementsInstancedBaseVertexBaseInstance.argtypes = (GLenum, GLsizei, GLenum, POINTER(None), GLsizei, GLint, GLuint,)

glGetInternalformativ = _gl.glGetInternalformativ
glGetInternalformativ.restype = None
glGetInternalformativ.argtypes = (GLenum, GLenum, GLenum, GLsizei, POINTER(GLint),)

glGetActiveAtomicCounterBufferiv = _gl.glGetActiveAtomicCounterBufferiv
glGetActiveAtomicCounterBufferiv.restype = None
glGetActiveAtomicCounterBufferiv.argtypes = (GLuint, GLuint, GLenum, POINTER(GLint),)

glBindImageTexture = _gl.glBindImageTexture
glBindImageTexture.restype = None
glBindImageTexture.argtypes = (GLuint, GLuint, GLint, GLboolean, GLint, GLenum, GLenum,)

glMemoryBarrier = _gl.glMemoryBarrier
glMemoryBarrier.restype = None
glMemoryBarrier.argtypes = (GLbitfield,)

glTexStorage1D = _gl.glTexStorage1D
glTexStorage1D.restype = None
glTexStorage1D.argtypes = (GLenum, GLsizei, GLenum, GLsizei,)

glTexStorage2D = _gl.glTexStorage2D
glTexStorage2D.restype = None
glTexStorage2D.argtypes = (GLenum, GLsizei, GLenum, GLsizei, GLsizei,)

glTexStorage3D = _gl.glTexStorage3D
glTexStorage3D.restype = None
glTexStorage3D.argtypes = (GLenum, GLsizei, GLenum, GLsizei, GLsizei, GLsizei,)

glDrawTransformFeedbackInstanced = _gl.glDrawTransformFeedbackInstanced
glDrawTransformFeedbackInstanced.restype = None
glDrawTransformFeedbackInstanced.argtypes = (GLenum, GLuint, GLsizei,)

glDrawTransformFeedbackStreamInstanced = _gl.glDrawTransformFeedbackStreamInstanced
glDrawTransformFeedbackStreamInstanced.restype = None
glDrawTransformFeedbackStreamInstanced.argtypes = (GLenum, GLuint, GLuint, GLsizei,)

GL_VERSION_4_3 = 1
GL_NUM_SHADING_LANGUAGE_VERSIONS = 0x82E9
GL_VERTEX_ATTRIB_ARRAY_LONG = 0x874E
GL_COMPRESSED_RGB8_ETC2 = 0x9274
GL_COMPRESSED_SRGB8_ETC2 = 0x9275
GL_COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2 = 0x9276
GL_COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2 = 0x9277
GL_COMPRESSED_RGBA8_ETC2_EAC = 0x9278
GL_COMPRESSED_SRGB8_ALPHA8_ETC2_EAC = 0x9279
GL_COMPRESSED_R11_EAC = 0x9270
GL_COMPRESSED_SIGNED_R11_EAC = 0x9271
GL_COMPRESSED_RG11_EAC = 0x9272
GL_COMPRESSED_SIGNED_RG11_EAC = 0x9273
GL_PRIMITIVE_RESTART_FIXED_INDEX = 0x8D69
GL_ANY_SAMPLES_PASSED_CONSERVATIVE = 0x8D6A
GL_MAX_ELEMENT_INDEX = 0x8D6B
GL_COMPUTE_SHADER = 0x91B9
GL_MAX_COMPUTE_UNIFORM_BLOCKS = 0x91BB
GL_MAX_COMPUTE_TEXTURE_IMAGE_UNITS = 0x91BC
GL_MAX_COMPUTE_IMAGE_UNIFORMS = 0x91BD
GL_MAX_COMPUTE_SHARED_MEMORY_SIZE = 0x8262
GL_MAX_COMPUTE_UNIFORM_COMPONENTS = 0x8263
GL_MAX_COMPUTE_ATOMIC_COUNTER_BUFFERS = 0x8264
GL_MAX_COMPUTE_ATOMIC_COUNTERS = 0x8265
GL_MAX_COMBINED_COMPUTE_UNIFORM_COMPONENTS = 0x8266
GL_MAX_COMPUTE_WORK_GROUP_INVOCATIONS = 0x90EB
GL_MAX_COMPUTE_WORK_GROUP_COUNT = 0x91BE
GL_MAX_COMPUTE_WORK_GROUP_SIZE = 0x91BF
GL_COMPUTE_WORK_GROUP_SIZE = 0x8267
GL_UNIFORM_BLOCK_REFERENCED_BY_COMPUTE_SHADER = 0x90EC
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_COMPUTE_SHADER = 0x90ED
GL_DISPATCH_INDIRECT_BUFFER = 0x90EE
GL_DISPATCH_INDIRECT_BUFFER_BINDING = 0x90EF
GL_COMPUTE_SHADER_BIT = 0x00000020
GL_DEBUG_OUTPUT_SYNCHRONOUS = 0x8242
GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH = 0x8243
GL_DEBUG_CALLBACK_FUNCTION = 0x8244
GL_DEBUG_CALLBACK_USER_PARAM = 0x8245
GL_DEBUG_SOURCE_API = 0x8246
GL_DEBUG_SOURCE_WINDOW_SYSTEM = 0x8247
GL_DEBUG_SOURCE_SHADER_COMPILER = 0x8248
GL_DEBUG_SOURCE_THIRD_PARTY = 0x8249
GL_DEBUG_SOURCE_APPLICATION = 0x824A
GL_DEBUG_SOURCE_OTHER = 0x824B
GL_DEBUG_TYPE_ERROR = 0x824C
GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR = 0x824D
GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR = 0x824E
GL_DEBUG_TYPE_PORTABILITY = 0x824F
GL_DEBUG_TYPE_PERFORMANCE = 0x8250
GL_DEBUG_TYPE_OTHER = 0x8251
GL_MAX_DEBUG_MESSAGE_LENGTH = 0x9143
GL_MAX_DEBUG_LOGGED_MESSAGES = 0x9144
GL_DEBUG_LOGGED_MESSAGES = 0x9145
GL_DEBUG_SEVERITY_HIGH = 0x9146
GL_DEBUG_SEVERITY_MEDIUM = 0x9147
GL_DEBUG_SEVERITY_LOW = 0x9148
GL_DEBUG_TYPE_MARKER = 0x8268
GL_DEBUG_TYPE_PUSH_GROUP = 0x8269
GL_DEBUG_TYPE_POP_GROUP = 0x826A
GL_DEBUG_SEVERITY_NOTIFICATION = 0x826B
GL_MAX_DEBUG_GROUP_STACK_DEPTH = 0x826C
GL_DEBUG_GROUP_STACK_DEPTH = 0x826D
GL_BUFFER = 0x82E0
GL_SHADER = 0x82E1
GL_PROGRAM = 0x82E2
GL_QUERY = 0x82E3
GL_PROGRAM_PIPELINE = 0x82E4
GL_SAMPLER = 0x82E6
GL_MAX_LABEL_LENGTH = 0x82E8
GL_DEBUG_OUTPUT = 0x92E0
GL_CONTEXT_FLAG_DEBUG_BIT = 0x00000002
GL_MAX_UNIFORM_LOCATIONS = 0x826E
GL_FRAMEBUFFER_DEFAULT_WIDTH = 0x9310
GL_FRAMEBUFFER_DEFAULT_HEIGHT = 0x9311
GL_FRAMEBUFFER_DEFAULT_LAYERS = 0x9312
GL_FRAMEBUFFER_DEFAULT_SAMPLES = 0x9313
GL_FRAMEBUFFER_DEFAULT_FIXED_SAMPLE_LOCATIONS = 0x9314
GL_MAX_FRAMEBUFFER_WIDTH = 0x9315
GL_MAX_FRAMEBUFFER_HEIGHT = 0x9316
GL_MAX_FRAMEBUFFER_LAYERS = 0x9317
GL_MAX_FRAMEBUFFER_SAMPLES = 0x9318
GL_INTERNALFORMAT_SUPPORTED = 0x826F
GL_INTERNALFORMAT_PREFERRED = 0x8270
GL_INTERNALFORMAT_RED_SIZE = 0x8271
GL_INTERNALFORMAT_GREEN_SIZE = 0x8272
GL_INTERNALFORMAT_BLUE_SIZE = 0x8273
GL_INTERNALFORMAT_ALPHA_SIZE = 0x8274
GL_INTERNALFORMAT_DEPTH_SIZE = 0x8275
GL_INTERNALFORMAT_STENCIL_SIZE = 0x8276
GL_INTERNALFORMAT_SHARED_SIZE = 0x8277
GL_INTERNALFORMAT_RED_TYPE = 0x8278
GL_INTERNALFORMAT_GREEN_TYPE = 0x8279
GL_INTERNALFORMAT_BLUE_TYPE = 0x827A
GL_INTERNALFORMAT_ALPHA_TYPE = 0x827B
GL_INTERNALFORMAT_DEPTH_TYPE = 0x827C
GL_INTERNALFORMAT_STENCIL_TYPE = 0x827D
GL_MAX_WIDTH = 0x827E
GL_MAX_HEIGHT = 0x827F
GL_MAX_DEPTH = 0x8280
GL_MAX_LAYERS = 0x8281
GL_MAX_COMBINED_DIMENSIONS = 0x8282
GL_COLOR_COMPONENTS = 0x8283
GL_DEPTH_COMPONENTS = 0x8284
GL_STENCIL_COMPONENTS = 0x8285
GL_COLOR_RENDERABLE = 0x8286
GL_DEPTH_RENDERABLE = 0x8287
GL_STENCIL_RENDERABLE = 0x8288
GL_FRAMEBUFFER_RENDERABLE = 0x8289
GL_FRAMEBUFFER_RENDERABLE_LAYERED = 0x828A
GL_FRAMEBUFFER_BLEND = 0x828B
GL_READ_PIXELS = 0x828C
GL_READ_PIXELS_FORMAT = 0x828D
GL_READ_PIXELS_TYPE = 0x828E
GL_TEXTURE_IMAGE_FORMAT = 0x828F
GL_TEXTURE_IMAGE_TYPE = 0x8290
GL_GET_TEXTURE_IMAGE_FORMAT = 0x8291
GL_GET_TEXTURE_IMAGE_TYPE = 0x8292
GL_MIPMAP = 0x8293
GL_MANUAL_GENERATE_MIPMAP = 0x8294
GL_AUTO_GENERATE_MIPMAP = 0x8295
GL_COLOR_ENCODING = 0x8296
GL_SRGB_READ = 0x8297
GL_SRGB_WRITE = 0x8298
GL_FILTER = 0x829A
GL_VERTEX_TEXTURE = 0x829B
GL_TESS_CONTROL_TEXTURE = 0x829C
GL_TESS_EVALUATION_TEXTURE = 0x829D
GL_GEOMETRY_TEXTURE = 0x829E
GL_FRAGMENT_TEXTURE = 0x829F
GL_COMPUTE_TEXTURE = 0x82A0
GL_TEXTURE_SHADOW = 0x82A1
GL_TEXTURE_GATHER = 0x82A2
GL_TEXTURE_GATHER_SHADOW = 0x82A3
GL_SHADER_IMAGE_LOAD = 0x82A4
GL_SHADER_IMAGE_STORE = 0x82A5
GL_SHADER_IMAGE_ATOMIC = 0x82A6
GL_IMAGE_TEXEL_SIZE = 0x82A7
GL_IMAGE_COMPATIBILITY_CLASS = 0x82A8
GL_IMAGE_PIXEL_FORMAT = 0x82A9
GL_IMAGE_PIXEL_TYPE = 0x82AA
GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_TEST = 0x82AC
GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_TEST = 0x82AD
GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_WRITE = 0x82AE
GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_WRITE = 0x82AF
GL_TEXTURE_COMPRESSED_BLOCK_WIDTH = 0x82B1
GL_TEXTURE_COMPRESSED_BLOCK_HEIGHT = 0x82B2
GL_TEXTURE_COMPRESSED_BLOCK_SIZE = 0x82B3
GL_CLEAR_BUFFER = 0x82B4
GL_TEXTURE_VIEW = 0x82B5
GL_VIEW_COMPATIBILITY_CLASS = 0x82B6
GL_FULL_SUPPORT = 0x82B7
GL_CAVEAT_SUPPORT = 0x82B8
GL_IMAGE_CLASS_4_X_32 = 0x82B9
GL_IMAGE_CLASS_2_X_32 = 0x82BA
GL_IMAGE_CLASS_1_X_32 = 0x82BB
GL_IMAGE_CLASS_4_X_16 = 0x82BC
GL_IMAGE_CLASS_2_X_16 = 0x82BD
GL_IMAGE_CLASS_1_X_16 = 0x82BE
GL_IMAGE_CLASS_4_X_8 = 0x82BF
GL_IMAGE_CLASS_2_X_8 = 0x82C0
GL_IMAGE_CLASS_1_X_8 = 0x82C1
GL_IMAGE_CLASS_11_11_10 = 0x82C2
GL_IMAGE_CLASS_10_10_10_2 = 0x82C3
GL_VIEW_CLASS_128_BITS = 0x82C4
GL_VIEW_CLASS_96_BITS = 0x82C5
GL_VIEW_CLASS_64_BITS = 0x82C6
GL_VIEW_CLASS_48_BITS = 0x82C7
GL_VIEW_CLASS_32_BITS = 0x82C8
GL_VIEW_CLASS_24_BITS = 0x82C9
GL_VIEW_CLASS_16_BITS = 0x82CA
GL_VIEW_CLASS_8_BITS = 0x82CB
GL_VIEW_CLASS_S3TC_DXT1_RGB = 0x82CC
GL_VIEW_CLASS_S3TC_DXT1_RGBA = 0x82CD
GL_VIEW_CLASS_S3TC_DXT3_RGBA = 0x82CE
GL_VIEW_CLASS_S3TC_DXT5_RGBA = 0x82CF
GL_VIEW_CLASS_RGTC1_RED = 0x82D0
GL_VIEW_CLASS_RGTC2_RG = 0x82D1
GL_VIEW_CLASS_BPTC_UNORM = 0x82D2
GL_VIEW_CLASS_BPTC_FLOAT = 0x82D3
GL_UNIFORM = 0x92E1
GL_UNIFORM_BLOCK = 0x92E2
GL_PROGRAM_INPUT = 0x92E3
GL_PROGRAM_OUTPUT = 0x92E4
GL_BUFFER_VARIABLE = 0x92E5
GL_SHADER_STORAGE_BLOCK = 0x92E6
GL_VERTEX_SUBROUTINE = 0x92E8
GL_TESS_CONTROL_SUBROUTINE = 0x92E9
GL_TESS_EVALUATION_SUBROUTINE = 0x92EA
GL_GEOMETRY_SUBROUTINE = 0x92EB
GL_FRAGMENT_SUBROUTINE = 0x92EC
GL_COMPUTE_SUBROUTINE = 0x92ED
GL_VERTEX_SUBROUTINE_UNIFORM = 0x92EE
GL_TESS_CONTROL_SUBROUTINE_UNIFORM = 0x92EF
GL_TESS_EVALUATION_SUBROUTINE_UNIFORM = 0x92F0
GL_GEOMETRY_SUBROUTINE_UNIFORM = 0x92F1
GL_FRAGMENT_SUBROUTINE_UNIFORM = 0x92F2
GL_COMPUTE_SUBROUTINE_UNIFORM = 0x92F3
GL_TRANSFORM_FEEDBACK_VARYING = 0x92F4
GL_ACTIVE_RESOURCES = 0x92F5
GL_MAX_NAME_LENGTH = 0x92F6
GL_MAX_NUM_ACTIVE_VARIABLES = 0x92F7
GL_MAX_NUM_COMPATIBLE_SUBROUTINES = 0x92F8
GL_NAME_LENGTH = 0x92F9
GL_TYPE = 0x92FA
GL_ARRAY_SIZE = 0x92FB
GL_OFFSET = 0x92FC
GL_BLOCK_INDEX = 0x92FD
GL_ARRAY_STRIDE = 0x92FE
GL_MATRIX_STRIDE = 0x92FF
GL_IS_ROW_MAJOR = 0x9300
GL_ATOMIC_COUNTER_BUFFER_INDEX = 0x9301
GL_BUFFER_BINDING = 0x9302
GL_BUFFER_DATA_SIZE = 0x9303
GL_NUM_ACTIVE_VARIABLES = 0x9304
GL_ACTIVE_VARIABLES = 0x9305
GL_REFERENCED_BY_VERTEX_SHADER = 0x9306
GL_REFERENCED_BY_TESS_CONTROL_SHADER = 0x9307
GL_REFERENCED_BY_TESS_EVALUATION_SHADER = 0x9308
GL_REFERENCED_BY_GEOMETRY_SHADER = 0x9309
GL_REFERENCED_BY_FRAGMENT_SHADER = 0x930A
GL_REFERENCED_BY_COMPUTE_SHADER = 0x930B
GL_TOP_LEVEL_ARRAY_SIZE = 0x930C
GL_TOP_LEVEL_ARRAY_STRIDE = 0x930D
GL_LOCATION = 0x930E
GL_LOCATION_INDEX = 0x930F
GL_IS_PER_PATCH = 0x92E7
GL_SHADER_STORAGE_BUFFER = 0x90D2
GL_SHADER_STORAGE_BUFFER_BINDING = 0x90D3
GL_SHADER_STORAGE_BUFFER_START = 0x90D4
GL_SHADER_STORAGE_BUFFER_SIZE = 0x90D5
GL_MAX_VERTEX_SHADER_STORAGE_BLOCKS = 0x90D6
GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS = 0x90D7
GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS = 0x90D8
GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS = 0x90D9
GL_MAX_FRAGMENT_SHADER_STORAGE_BLOCKS = 0x90DA
GL_MAX_COMPUTE_SHADER_STORAGE_BLOCKS = 0x90DB
GL_MAX_COMBINED_SHADER_STORAGE_BLOCKS = 0x90DC
GL_MAX_SHADER_STORAGE_BUFFER_BINDINGS = 0x90DD
GL_MAX_SHADER_STORAGE_BLOCK_SIZE = 0x90DE
GL_SHADER_STORAGE_BUFFER_OFFSET_ALIGNMENT = 0x90DF
GL_SHADER_STORAGE_BARRIER_BIT = 0x00002000
GL_MAX_COMBINED_SHADER_OUTPUT_RESOURCES = 0x8F39
GL_DEPTH_STENCIL_TEXTURE_MODE = 0x90EA
GL_TEXTURE_BUFFER_OFFSET = 0x919D
GL_TEXTURE_BUFFER_SIZE = 0x919E
GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT = 0x919F
GL_TEXTURE_VIEW_MIN_LEVEL = 0x82DB
GL_TEXTURE_VIEW_NUM_LEVELS = 0x82DC
GL_TEXTURE_VIEW_MIN_LAYER = 0x82DD
GL_TEXTURE_VIEW_NUM_LAYERS = 0x82DE
GL_TEXTURE_IMMUTABLE_LEVELS = 0x82DF
GL_VERTEX_ATTRIB_BINDING = 0x82D4
GL_VERTEX_ATTRIB_RELATIVE_OFFSET = 0x82D5
GL_VERTEX_BINDING_DIVISOR = 0x82D6
GL_VERTEX_BINDING_OFFSET = 0x82D7
GL_VERTEX_BINDING_STRIDE = 0x82D8
GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET = 0x82D9
GL_MAX_VERTEX_ATTRIB_BINDINGS = 0x82DA
GL_VERTEX_BINDING_BUFFER = 0x8F4F
glClearBufferData = _gl.glClearBufferData
glClearBufferData.restype = None
glClearBufferData.argtypes = (GLenum, GLenum, GLenum, GLenum, POINTER(None),)

glClearBufferSubData = _gl.glClearBufferSubData
glClearBufferSubData.restype = None
glClearBufferSubData.argtypes = (GLenum, GLenum, GLintptr, GLsizeiptr, GLenum, GLenum, POINTER(None),)

glDispatchCompute = _gl.glDispatchCompute
glDispatchCompute.restype = None
glDispatchCompute.argtypes = (GLuint, GLuint, GLuint,)

glDispatchComputeIndirect = _gl.glDispatchComputeIndirect
glDispatchComputeIndirect.restype = None
glDispatchComputeIndirect.argtypes = (GLintptr,)

glCopyImageSubData = _gl.glCopyImageSubData
glCopyImageSubData.restype = None
glCopyImageSubData.argtypes = (GLuint, GLenum, GLint, GLint, GLint, GLint, GLuint, GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei,)

glFramebufferParameteri = _gl.glFramebufferParameteri
glFramebufferParameteri.restype = None
glFramebufferParameteri.argtypes = (GLenum, GLenum, GLint,)

glGetFramebufferParameteriv = _gl.glGetFramebufferParameteriv
glGetFramebufferParameteriv.restype = None
glGetFramebufferParameteriv.argtypes = (GLenum, GLenum, POINTER(GLint),)

glGetInternalformati64v = _gl.glGetInternalformati64v
glGetInternalformati64v.restype = None
glGetInternalformati64v.argtypes = (GLenum, GLenum, GLenum, GLsizei, POINTER(GLint64),)

glInvalidateTexSubImage = _gl.glInvalidateTexSubImage
glInvalidateTexSubImage.restype = None
glInvalidateTexSubImage.argtypes = (GLuint, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei,)

glInvalidateTexImage = _gl.glInvalidateTexImage
glInvalidateTexImage.restype = None
glInvalidateTexImage.argtypes = (GLuint, GLint,)

glInvalidateBufferSubData = _gl.glInvalidateBufferSubData
glInvalidateBufferSubData.restype = None
glInvalidateBufferSubData.argtypes = (GLuint, GLintptr, GLsizeiptr,)

glInvalidateBufferData = _gl.glInvalidateBufferData
glInvalidateBufferData.restype = None
glInvalidateBufferData.argtypes = (GLuint,)

glInvalidateFramebuffer = _gl.glInvalidateFramebuffer
glInvalidateFramebuffer.restype = None
glInvalidateFramebuffer.argtypes = (GLenum, GLsizei, POINTER(GLenum),)

glInvalidateSubFramebuffer = _gl.glInvalidateSubFramebuffer
glInvalidateSubFramebuffer.restype = None
glInvalidateSubFramebuffer.argtypes = (GLenum, GLsizei, POINTER(GLenum), GLint, GLint, GLsizei, GLsizei,)

glMultiDrawArraysIndirect = _gl.glMultiDrawArraysIndirect
glMultiDrawArraysIndirect.restype = None
glMultiDrawArraysIndirect.argtypes = (GLenum, POINTER(None), GLsizei, GLsizei,)

glMultiDrawElementsIndirect = _gl.glMultiDrawElementsIndirect
glMultiDrawElementsIndirect.restype = None
glMultiDrawElementsIndirect.argtypes = (GLenum, GLenum, POINTER(None), GLsizei, GLsizei,)

glGetProgramInterfaceiv = _gl.glGetProgramInterfaceiv
glGetProgramInterfaceiv.restype = None
glGetProgramInterfaceiv.argtypes = (GLuint, GLenum, GLenum, POINTER(GLint),)

glGetProgramResourceIndex = _gl.glGetProgramResourceIndex
glGetProgramResourceIndex.restype = GLuint
glGetProgramResourceIndex.argtypes = (GLuint, GLenum, STRING,)

glGetProgramResourceName = _gl.glGetProgramResourceName
glGetProgramResourceName.restype = None
glGetProgramResourceName.argtypes = (GLuint, GLenum, GLuint, GLsizei, POINTER(GLsizei), STRING,)

glGetProgramResourceiv = _gl.glGetProgramResourceiv
glGetProgramResourceiv.restype = None
glGetProgramResourceiv.argtypes = (GLuint, GLenum, GLuint, GLsizei, POINTER(GLenum), GLsizei, POINTER(GLsizei), POINTER(GLint),)

glGetProgramResourceLocation = _gl.glGetProgramResourceLocation
glGetProgramResourceLocation.restype = GLint
glGetProgramResourceLocation.argtypes = (GLuint, GLenum, STRING,)

glGetProgramResourceLocationIndex = _gl.glGetProgramResourceLocationIndex
glGetProgramResourceLocationIndex.restype = GLint
glGetProgramResourceLocationIndex.argtypes = (GLuint, GLenum, STRING,)

glShaderStorageBlockBinding = _gl.glShaderStorageBlockBinding
glShaderStorageBlockBinding.restype = None
glShaderStorageBlockBinding.argtypes = (GLuint, GLuint, GLuint,)

glTexBufferRange = _gl.glTexBufferRange
glTexBufferRange.restype = None
glTexBufferRange.argtypes = (GLenum, GLenum, GLuint, GLintptr, GLsizeiptr,)

glTexStorage2DMultisample = _gl.glTexStorage2DMultisample
glTexStorage2DMultisample.restype = None
glTexStorage2DMultisample.argtypes = (GLenum, GLsizei, GLenum, GLsizei, GLsizei, GLboolean,)

glTexStorage3DMultisample = _gl.glTexStorage3DMultisample
glTexStorage3DMultisample.restype = None
glTexStorage3DMultisample.argtypes = (GLenum, GLsizei, GLenum, GLsizei, GLsizei, GLsizei, GLboolean,)

glTextureView = _gl.glTextureView
glTextureView.restype = None
glTextureView.argtypes = (GLuint, GLenum, GLuint, GLenum, GLuint, GLuint, GLuint, GLuint,)

glBindVertexBuffer = _gl.glBindVertexBuffer
glBindVertexBuffer.restype = None
glBindVertexBuffer.argtypes = (GLuint, GLuint, GLintptr, GLsizei,)

glVertexAttribFormat = _gl.glVertexAttribFormat
glVertexAttribFormat.restype = None
glVertexAttribFormat.argtypes = (GLuint, GLint, GLenum, GLboolean, GLuint,)

glVertexAttribIFormat = _gl.glVertexAttribIFormat
glVertexAttribIFormat.restype = None
glVertexAttribIFormat.argtypes = (GLuint, GLint, GLenum, GLuint,)

glVertexAttribLFormat = _gl.glVertexAttribLFormat
glVertexAttribLFormat.restype = None
glVertexAttribLFormat.argtypes = (GLuint, GLint, GLenum, GLuint,)

glVertexAttribBinding = _gl.glVertexAttribBinding
glVertexAttribBinding.restype = None
glVertexAttribBinding.argtypes = (GLuint, GLuint,)

glVertexBindingDivisor = _gl.glVertexBindingDivisor
glVertexBindingDivisor.restype = None
glVertexBindingDivisor.argtypes = (GLuint, GLuint,)

glDebugMessageControl = _gl.glDebugMessageControl
glDebugMessageControl.restype = None
glDebugMessageControl.argtypes = (GLenum, GLenum, GLenum, GLsizei, POINTER(GLuint), GLboolean,)

glDebugMessageInsert = _gl.glDebugMessageInsert
glDebugMessageInsert.restype = None
glDebugMessageInsert.argtypes = (GLenum, GLenum, GLuint, GLenum, GLsizei, STRING,)

glDebugMessageCallback = _gl.glDebugMessageCallback
glDebugMessageCallback.restype = None
glDebugMessageCallback.argtypes = (GLDEBUGPROC, POINTER(None),)

glGetDebugMessageLog = _gl.glGetDebugMessageLog
glGetDebugMessageLog.restype = GLuint
glGetDebugMessageLog.argtypes = (GLuint, GLsizei, POINTER(GLenum), POINTER(GLenum), POINTER(GLuint), POINTER(GLenum), POINTER(GLsizei), STRING,)

glPushDebugGroup = _gl.glPushDebugGroup
glPushDebugGroup.restype = None
glPushDebugGroup.argtypes = (GLenum, GLuint, GLsizei, STRING,)

glPopDebugGroup = _gl.glPopDebugGroup
glPopDebugGroup.restype = None
glPopDebugGroup.argtypes = ()

glObjectLabel = _gl.glObjectLabel
glObjectLabel.restype = None
glObjectLabel.argtypes = (GLenum, GLuint, GLsizei, STRING,)

glGetObjectLabel = _gl.glGetObjectLabel
glGetObjectLabel.restype = None
glGetObjectLabel.argtypes = (GLenum, GLuint, GLsizei, POINTER(GLsizei), STRING,)

glObjectPtrLabel = _gl.glObjectPtrLabel
glObjectPtrLabel.restype = None
glObjectPtrLabel.argtypes = (POINTER(None), GLsizei, STRING,)

glGetObjectPtrLabel = _gl.glGetObjectPtrLabel
glGetObjectPtrLabel.restype = None
glGetObjectPtrLabel.argtypes = (POINTER(None), GLsizei, POINTER(GLsizei), STRING,)

GL_VERSION_4_4 = 1
GL_MAX_VERTEX_ATTRIB_STRIDE = 0x82E5
GL_PRIMITIVE_RESTART_FOR_PATCHES_SUPPORTED = 0x8221
GL_TEXTURE_BUFFER_BINDING = 0x8C2A
GL_MAP_PERSISTENT_BIT = 0x0040
GL_MAP_COHERENT_BIT = 0x0080
GL_DYNAMIC_STORAGE_BIT = 0x0100
GL_CLIENT_STORAGE_BIT = 0x0200
GL_CLIENT_MAPPED_BUFFER_BARRIER_BIT = 0x00004000
GL_BUFFER_IMMUTABLE_STORAGE = 0x821F
GL_BUFFER_STORAGE_FLAGS = 0x8220
GL_CLEAR_TEXTURE = 0x9365
GL_LOCATION_COMPONENT = 0x934A
GL_TRANSFORM_FEEDBACK_BUFFER_INDEX = 0x934B
GL_TRANSFORM_FEEDBACK_BUFFER_STRIDE = 0x934C
GL_QUERY_BUFFER = 0x9192
GL_QUERY_BUFFER_BARRIER_BIT = 0x00008000
GL_QUERY_BUFFER_BINDING = 0x9193
GL_QUERY_RESULT_NO_WAIT = 0x9194
GL_MIRROR_CLAMP_TO_EDGE = 0x8743
glBufferStorage = _gl.glBufferStorage
glBufferStorage.restype = None
glBufferStorage.argtypes = (GLenum, GLsizeiptr, POINTER(None), GLbitfield,)

glClearTexImage = _gl.glClearTexImage
glClearTexImage.restype = None
glClearTexImage.argtypes = (GLuint, GLint, GLenum, GLenum, POINTER(None),)

glClearTexSubImage = _gl.glClearTexSubImage
glClearTexSubImage.restype = None
glClearTexSubImage.argtypes = (GLuint, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLenum, POINTER(None),)

glBindBuffersBase = _gl.glBindBuffersBase
glBindBuffersBase.restype = None
glBindBuffersBase.argtypes = (GLenum, GLuint, GLsizei, POINTER(GLuint),)

glBindBuffersRange = _gl.glBindBuffersRange
glBindBuffersRange.restype = None
glBindBuffersRange.argtypes = (GLenum, GLuint, GLsizei, POINTER(GLuint), POINTER(GLintptr), POINTER(GLsizeiptr),)

glBindTextures = _gl.glBindTextures
glBindTextures.restype = None
glBindTextures.argtypes = (GLuint, GLsizei, POINTER(GLuint),)

glBindSamplers = _gl.glBindSamplers
glBindSamplers.restype = None
glBindSamplers.argtypes = (GLuint, GLsizei, POINTER(GLuint),)

glBindImageTextures = _gl.glBindImageTextures
glBindImageTextures.restype = None
glBindImageTextures.argtypes = (GLuint, GLsizei, POINTER(GLuint),)

glBindVertexBuffers = _gl.glBindVertexBuffers
glBindVertexBuffers.restype = None
glBindVertexBuffers.argtypes = (GLuint, GLsizei, POINTER(GLuint), POINTER(GLintptr), POINTER(GLsizei),)

GL_VERSION_4_5 = 1
GL_CONTEXT_LOST = 0x0507
GL_NEGATIVE_ONE_TO_ONE = 0x935E
GL_ZERO_TO_ONE = 0x935F
GL_CLIP_ORIGIN = 0x935C
GL_CLIP_DEPTH_MODE = 0x935D
GL_QUERY_WAIT_INVERTED = 0x8E17
GL_QUERY_NO_WAIT_INVERTED = 0x8E18
GL_QUERY_BY_REGION_WAIT_INVERTED = 0x8E19
GL_QUERY_BY_REGION_NO_WAIT_INVERTED = 0x8E1A
GL_MAX_CULL_DISTANCES = 0x82F9
GL_MAX_COMBINED_CLIP_AND_CULL_DISTANCES = 0x82FA
GL_TEXTURE_TARGET = 0x1006
GL_QUERY_TARGET = 0x82EA
GL_GUILTY_CONTEXT_RESET = 0x8253
GL_INNOCENT_CONTEXT_RESET = 0x8254
GL_UNKNOWN_CONTEXT_RESET = 0x8255
GL_RESET_NOTIFICATION_STRATEGY = 0x8256
GL_LOSE_CONTEXT_ON_RESET = 0x8252
GL_NO_RESET_NOTIFICATION = 0x8261
GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT = 0x00000004
GL_CONTEXT_RELEASE_BEHAVIOR = 0x82FB
GL_CONTEXT_RELEASE_BEHAVIOR_FLUSH = 0x82FC
glClipControl = _gl.glClipControl
glClipControl.restype = None
glClipControl.argtypes = (GLenum, GLenum,)

glCreateTransformFeedbacks = _gl.glCreateTransformFeedbacks
glCreateTransformFeedbacks.restype = None
glCreateTransformFeedbacks.argtypes = (GLsizei, POINTER(GLuint),)

glTransformFeedbackBufferBase = _gl.glTransformFeedbackBufferBase
glTransformFeedbackBufferBase.restype = None
glTransformFeedbackBufferBase.argtypes = (GLuint, GLuint, GLuint,)

glTransformFeedbackBufferRange = _gl.glTransformFeedbackBufferRange
glTransformFeedbackBufferRange.restype = None
glTransformFeedbackBufferRange.argtypes = (GLuint, GLuint, GLuint, GLintptr, GLsizeiptr,)

glGetTransformFeedbackiv = _gl.glGetTransformFeedbackiv
glGetTransformFeedbackiv.restype = None
glGetTransformFeedbackiv.argtypes = (GLuint, GLenum, POINTER(GLint),)

glGetTransformFeedbacki_v = _gl.glGetTransformFeedbacki_v
glGetTransformFeedbacki_v.restype = None
glGetTransformFeedbacki_v.argtypes = (GLuint, GLenum, GLuint, POINTER(GLint),)

glGetTransformFeedbacki64_v = _gl.glGetTransformFeedbacki64_v
glGetTransformFeedbacki64_v.restype = None
glGetTransformFeedbacki64_v.argtypes = (GLuint, GLenum, GLuint, POINTER(GLint64),)

glCreateBuffers = _gl.glCreateBuffers
glCreateBuffers.restype = None
glCreateBuffers.argtypes = (GLsizei, POINTER(GLuint),)

glNamedBufferStorage = _gl.glNamedBufferStorage
glNamedBufferStorage.restype = None
glNamedBufferStorage.argtypes = (GLuint, GLsizeiptr, POINTER(None), GLbitfield,)

glNamedBufferData = _gl.glNamedBufferData
glNamedBufferData.restype = None
glNamedBufferData.argtypes = (GLuint, GLsizeiptr, POINTER(None), GLenum,)

glNamedBufferSubData = _gl.glNamedBufferSubData
glNamedBufferSubData.restype = None
glNamedBufferSubData.argtypes = (GLuint, GLintptr, GLsizeiptr, POINTER(None),)

glCopyNamedBufferSubData = _gl.glCopyNamedBufferSubData
glCopyNamedBufferSubData.restype = None
glCopyNamedBufferSubData.argtypes = (GLuint, GLuint, GLintptr, GLintptr, GLsizeiptr,)

glClearNamedBufferData = _gl.glClearNamedBufferData
glClearNamedBufferData.restype = None
glClearNamedBufferData.argtypes = (GLuint, GLenum, GLenum, GLenum, POINTER(None),)

glClearNamedBufferSubData = _gl.glClearNamedBufferSubData
glClearNamedBufferSubData.restype = None
glClearNamedBufferSubData.argtypes = (GLuint, GLenum, GLintptr, GLsizeiptr, GLenum, GLenum, POINTER(None),)

glMapNamedBuffer = _gl.glMapNamedBuffer
glMapNamedBuffer.restype = POINTER(None)
glMapNamedBuffer.argtypes = (GLuint, GLenum,)

glMapNamedBufferRange = _gl.glMapNamedBufferRange
glMapNamedBufferRange.restype = POINTER(None)
glMapNamedBufferRange.argtypes = (GLuint, GLintptr, GLsizeiptr, GLbitfield,)

glUnmapNamedBuffer = _gl.glUnmapNamedBuffer
glUnmapNamedBuffer.restype = GLboolean
glUnmapNamedBuffer.argtypes = (GLuint,)

glFlushMappedNamedBufferRange = _gl.glFlushMappedNamedBufferRange
glFlushMappedNamedBufferRange.restype = None
glFlushMappedNamedBufferRange.argtypes = (GLuint, GLintptr, GLsizeiptr,)

glGetNamedBufferParameteriv = _gl.glGetNamedBufferParameteriv
glGetNamedBufferParameteriv.restype = None
glGetNamedBufferParameteriv.argtypes = (GLuint, GLenum, POINTER(GLint),)

glGetNamedBufferParameteri64v = _gl.glGetNamedBufferParameteri64v
glGetNamedBufferParameteri64v.restype = None
glGetNamedBufferParameteri64v.argtypes = (GLuint, GLenum, POINTER(GLint64),)

glGetNamedBufferPointerv = _gl.glGetNamedBufferPointerv
glGetNamedBufferPointerv.restype = None
glGetNamedBufferPointerv.argtypes = (GLuint, GLenum, POINTER(POINTER(None)),)

glGetNamedBufferSubData = _gl.glGetNamedBufferSubData
glGetNamedBufferSubData.restype = None
glGetNamedBufferSubData.argtypes = (GLuint, GLintptr, GLsizeiptr, POINTER(None),)

glCreateFramebuffers = _gl.glCreateFramebuffers
glCreateFramebuffers.restype = None
glCreateFramebuffers.argtypes = (GLsizei, POINTER(GLuint),)

glNamedFramebufferRenderbuffer = _gl.glNamedFramebufferRenderbuffer
glNamedFramebufferRenderbuffer.restype = None
glNamedFramebufferRenderbuffer.argtypes = (GLuint, GLenum, GLenum, GLuint,)

glNamedFramebufferParameteri = _gl.glNamedFramebufferParameteri
glNamedFramebufferParameteri.restype = None
glNamedFramebufferParameteri.argtypes = (GLuint, GLenum, GLint,)

glNamedFramebufferTexture = _gl.glNamedFramebufferTexture
glNamedFramebufferTexture.restype = None
glNamedFramebufferTexture.argtypes = (GLuint, GLenum, GLuint, GLint,)

glNamedFramebufferTextureLayer = _gl.glNamedFramebufferTextureLayer
glNamedFramebufferTextureLayer.restype = None
glNamedFramebufferTextureLayer.argtypes = (GLuint, GLenum, GLuint, GLint, GLint,)

glNamedFramebufferDrawBuffer = _gl.glNamedFramebufferDrawBuffer
glNamedFramebufferDrawBuffer.restype = None
glNamedFramebufferDrawBuffer.argtypes = (GLuint, GLenum,)

glNamedFramebufferDrawBuffers = _gl.glNamedFramebufferDrawBuffers
glNamedFramebufferDrawBuffers.restype = None
glNamedFramebufferDrawBuffers.argtypes = (GLuint, GLsizei, POINTER(GLenum),)

glNamedFramebufferReadBuffer = _gl.glNamedFramebufferReadBuffer
glNamedFramebufferReadBuffer.restype = None
glNamedFramebufferReadBuffer.argtypes = (GLuint, GLenum,)

glInvalidateNamedFramebufferData = _gl.glInvalidateNamedFramebufferData
glInvalidateNamedFramebufferData.restype = None
glInvalidateNamedFramebufferData.argtypes = (GLuint, GLsizei, POINTER(GLenum),)

glInvalidateNamedFramebufferSubData = _gl.glInvalidateNamedFramebufferSubData
glInvalidateNamedFramebufferSubData.restype = None
glInvalidateNamedFramebufferSubData.argtypes = (GLuint, GLsizei, POINTER(GLenum), GLint, GLint, GLsizei, GLsizei,)

glClearNamedFramebufferiv = _gl.glClearNamedFramebufferiv
glClearNamedFramebufferiv.restype = None
glClearNamedFramebufferiv.argtypes = (GLuint, GLenum, GLint, POINTER(GLint),)

glClearNamedFramebufferuiv = _gl.glClearNamedFramebufferuiv
glClearNamedFramebufferuiv.restype = None
glClearNamedFramebufferuiv.argtypes = (GLuint, GLenum, GLint, POINTER(GLuint),)

glClearNamedFramebufferfv = _gl.glClearNamedFramebufferfv
glClearNamedFramebufferfv.restype = None
glClearNamedFramebufferfv.argtypes = (GLuint, GLenum, GLint, POINTER(GLfloat),)

glClearNamedFramebufferfi = _gl.glClearNamedFramebufferfi
glClearNamedFramebufferfi.restype = None
glClearNamedFramebufferfi.argtypes = (GLuint, GLenum, GLint, GLfloat, GLint,)

glBlitNamedFramebuffer = _gl.glBlitNamedFramebuffer
glBlitNamedFramebuffer.restype = None
glBlitNamedFramebuffer.argtypes = (GLuint, GLuint, GLint, GLint, GLint, GLint, GLint, GLint, GLint, GLint, GLbitfield, GLenum,)

glCheckNamedFramebufferStatus = _gl.glCheckNamedFramebufferStatus
glCheckNamedFramebufferStatus.restype = GLenum
glCheckNamedFramebufferStatus.argtypes = (GLuint, GLenum,)

glGetNamedFramebufferParameteriv = _gl.glGetNamedFramebufferParameteriv
glGetNamedFramebufferParameteriv.restype = None
glGetNamedFramebufferParameteriv.argtypes = (GLuint, GLenum, POINTER(GLint),)

glGetNamedFramebufferAttachmentParameteriv = _gl.glGetNamedFramebufferAttachmentParameteriv
glGetNamedFramebufferAttachmentParameteriv.restype = None
glGetNamedFramebufferAttachmentParameteriv.argtypes = (GLuint, GLenum, GLenum, POINTER(GLint),)

glCreateRenderbuffers = _gl.glCreateRenderbuffers
glCreateRenderbuffers.restype = None
glCreateRenderbuffers.argtypes = (GLsizei, POINTER(GLuint),)

glNamedRenderbufferStorage = _gl.glNamedRenderbufferStorage
glNamedRenderbufferStorage.restype = None
glNamedRenderbufferStorage.argtypes = (GLuint, GLenum, GLsizei, GLsizei,)

glNamedRenderbufferStorageMultisample = _gl.glNamedRenderbufferStorageMultisample
glNamedRenderbufferStorageMultisample.restype = None
glNamedRenderbufferStorageMultisample.argtypes = (GLuint, GLsizei, GLenum, GLsizei, GLsizei,)

glGetNamedRenderbufferParameteriv = _gl.glGetNamedRenderbufferParameteriv
glGetNamedRenderbufferParameteriv.restype = None
glGetNamedRenderbufferParameteriv.argtypes = (GLuint, GLenum, POINTER(GLint),)

glCreateTextures = _gl.glCreateTextures
glCreateTextures.restype = None
glCreateTextures.argtypes = (GLenum, GLsizei, POINTER(GLuint),)

glTextureBuffer = _gl.glTextureBuffer
glTextureBuffer.restype = None
glTextureBuffer.argtypes = (GLuint, GLenum, GLuint,)

glTextureBufferRange = _gl.glTextureBufferRange
glTextureBufferRange.restype = None
glTextureBufferRange.argtypes = (GLuint, GLenum, GLuint, GLintptr, GLsizeiptr,)

glTextureStorage1D = _gl.glTextureStorage1D
glTextureStorage1D.restype = None
glTextureStorage1D.argtypes = (GLuint, GLsizei, GLenum, GLsizei,)

glTextureStorage2D = _gl.glTextureStorage2D
glTextureStorage2D.restype = None
glTextureStorage2D.argtypes = (GLuint, GLsizei, GLenum, GLsizei, GLsizei,)

glTextureStorage3D = _gl.glTextureStorage3D
glTextureStorage3D.restype = None
glTextureStorage3D.argtypes = (GLuint, GLsizei, GLenum, GLsizei, GLsizei, GLsizei,)

glTextureStorage2DMultisample = _gl.glTextureStorage2DMultisample
glTextureStorage2DMultisample.restype = None
glTextureStorage2DMultisample.argtypes = (GLuint, GLsizei, GLenum, GLsizei, GLsizei, GLboolean,)

glTextureStorage3DMultisample = _gl.glTextureStorage3DMultisample
glTextureStorage3DMultisample.restype = None
glTextureStorage3DMultisample.argtypes = (GLuint, GLsizei, GLenum, GLsizei, GLsizei, GLsizei, GLboolean,)

glTextureSubImage1D = _gl.glTextureSubImage1D
glTextureSubImage1D.restype = None
glTextureSubImage1D.argtypes = (GLuint, GLint, GLint, GLsizei, GLenum, GLenum, POINTER(None),)

glTextureSubImage2D = _gl.glTextureSubImage2D
glTextureSubImage2D.restype = None
glTextureSubImage2D.argtypes = (GLuint, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, POINTER(None),)

glTextureSubImage3D = _gl.glTextureSubImage3D
glTextureSubImage3D.restype = None
glTextureSubImage3D.argtypes = (GLuint, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLenum, POINTER(None),)

glCompressedTextureSubImage1D = _gl.glCompressedTextureSubImage1D
glCompressedTextureSubImage1D.restype = None
glCompressedTextureSubImage1D.argtypes = (GLuint, GLint, GLint, GLsizei, GLenum, GLsizei, POINTER(None),)

glCompressedTextureSubImage2D = _gl.glCompressedTextureSubImage2D
glCompressedTextureSubImage2D.restype = None
glCompressedTextureSubImage2D.argtypes = (GLuint, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLsizei, POINTER(None),)

glCompressedTextureSubImage3D = _gl.glCompressedTextureSubImage3D
glCompressedTextureSubImage3D.restype = None
glCompressedTextureSubImage3D.argtypes = (GLuint, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLsizei, POINTER(None),)

glCopyTextureSubImage1D = _gl.glCopyTextureSubImage1D
glCopyTextureSubImage1D.restype = None
glCopyTextureSubImage1D.argtypes = (GLuint, GLint, GLint, GLint, GLint, GLsizei,)

glCopyTextureSubImage2D = _gl.glCopyTextureSubImage2D
glCopyTextureSubImage2D.restype = None
glCopyTextureSubImage2D.argtypes = (GLuint, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei,)

glCopyTextureSubImage3D = _gl.glCopyTextureSubImage3D
glCopyTextureSubImage3D.restype = None
glCopyTextureSubImage3D.argtypes = (GLuint, GLint, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei,)

glTextureParameterf = _gl.glTextureParameterf
glTextureParameterf.restype = None
glTextureParameterf.argtypes = (GLuint, GLenum, GLfloat,)

glTextureParameterfv = _gl.glTextureParameterfv
glTextureParameterfv.restype = None
glTextureParameterfv.argtypes = (GLuint, GLenum, POINTER(GLfloat),)

glTextureParameteri = _gl.glTextureParameteri
glTextureParameteri.restype = None
glTextureParameteri.argtypes = (GLuint, GLenum, GLint,)

glTextureParameterIiv = _gl.glTextureParameterIiv
glTextureParameterIiv.restype = None
glTextureParameterIiv.argtypes = (GLuint, GLenum, POINTER(GLint),)

glTextureParameterIuiv = _gl.glTextureParameterIuiv
glTextureParameterIuiv.restype = None
glTextureParameterIuiv.argtypes = (GLuint, GLenum, POINTER(GLuint),)

glTextureParameteriv = _gl.glTextureParameteriv
glTextureParameteriv.restype = None
glTextureParameteriv.argtypes = (GLuint, GLenum, POINTER(GLint),)

glGenerateTextureMipmap = _gl.glGenerateTextureMipmap
glGenerateTextureMipmap.restype = None
glGenerateTextureMipmap.argtypes = (GLuint,)

glBindTextureUnit = _gl.glBindTextureUnit
glBindTextureUnit.restype = None
glBindTextureUnit.argtypes = (GLuint, GLuint,)

glGetTextureImage = _gl.glGetTextureImage
glGetTextureImage.restype = None
glGetTextureImage.argtypes = (GLuint, GLint, GLenum, GLenum, GLsizei, POINTER(None),)

glGetCompressedTextureImage = _gl.glGetCompressedTextureImage
glGetCompressedTextureImage.restype = None
glGetCompressedTextureImage.argtypes = (GLuint, GLint, GLsizei, POINTER(None),)

glGetTextureLevelParameterfv = _gl.glGetTextureLevelParameterfv
glGetTextureLevelParameterfv.restype = None
glGetTextureLevelParameterfv.argtypes = (GLuint, GLint, GLenum, POINTER(GLfloat),)

glGetTextureLevelParameteriv = _gl.glGetTextureLevelParameteriv
glGetTextureLevelParameteriv.restype = None
glGetTextureLevelParameteriv.argtypes = (GLuint, GLint, GLenum, POINTER(GLint),)

glGetTextureParameterfv = _gl.glGetTextureParameterfv
glGetTextureParameterfv.restype = None
glGetTextureParameterfv.argtypes = (GLuint, GLenum, POINTER(GLfloat),)

glGetTextureParameterIiv = _gl.glGetTextureParameterIiv
glGetTextureParameterIiv.restype = None
glGetTextureParameterIiv.argtypes = (GLuint, GLenum, POINTER(GLint),)

glGetTextureParameterIuiv = _gl.glGetTextureParameterIuiv
glGetTextureParameterIuiv.restype = None
glGetTextureParameterIuiv.argtypes = (GLuint, GLenum, POINTER(GLuint),)

glGetTextureParameteriv = _gl.glGetTextureParameteriv
glGetTextureParameteriv.restype = None
glGetTextureParameteriv.argtypes = (GLuint, GLenum, POINTER(GLint),)

glCreateVertexArrays = _gl.glCreateVertexArrays
glCreateVertexArrays.restype = None
glCreateVertexArrays.argtypes = (GLsizei, POINTER(GLuint),)

glDisableVertexArrayAttrib = _gl.glDisableVertexArrayAttrib
glDisableVertexArrayAttrib.restype = None
glDisableVertexArrayAttrib.argtypes = (GLuint, GLuint,)

glEnableVertexArrayAttrib = _gl.glEnableVertexArrayAttrib
glEnableVertexArrayAttrib.restype = None
glEnableVertexArrayAttrib.argtypes = (GLuint, GLuint,)

glVertexArrayElementBuffer = _gl.glVertexArrayElementBuffer
glVertexArrayElementBuffer.restype = None
glVertexArrayElementBuffer.argtypes = (GLuint, GLuint,)

glVertexArrayVertexBuffer = _gl.glVertexArrayVertexBuffer
glVertexArrayVertexBuffer.restype = None
glVertexArrayVertexBuffer.argtypes = (GLuint, GLuint, GLuint, GLintptr, GLsizei,)

glVertexArrayVertexBuffers = _gl.glVertexArrayVertexBuffers
glVertexArrayVertexBuffers.restype = None
glVertexArrayVertexBuffers.argtypes = (GLuint, GLuint, GLsizei, POINTER(GLuint), POINTER(GLintptr), POINTER(GLsizei),)

glVertexArrayAttribBinding = _gl.glVertexArrayAttribBinding
glVertexArrayAttribBinding.restype = None
glVertexArrayAttribBinding.argtypes = (GLuint, GLuint, GLuint,)

glVertexArrayAttribFormat = _gl.glVertexArrayAttribFormat
glVertexArrayAttribFormat.restype = None
glVertexArrayAttribFormat.argtypes = (GLuint, GLuint, GLint, GLenum, GLboolean, GLuint,)

glVertexArrayAttribIFormat = _gl.glVertexArrayAttribIFormat
glVertexArrayAttribIFormat.restype = None
glVertexArrayAttribIFormat.argtypes = (GLuint, GLuint, GLint, GLenum, GLuint,)

glVertexArrayAttribLFormat = _gl.glVertexArrayAttribLFormat
glVertexArrayAttribLFormat.restype = None
glVertexArrayAttribLFormat.argtypes = (GLuint, GLuint, GLint, GLenum, GLuint,)

glVertexArrayBindingDivisor = _gl.glVertexArrayBindingDivisor
glVertexArrayBindingDivisor.restype = None
glVertexArrayBindingDivisor.argtypes = (GLuint, GLuint, GLuint,)

glGetVertexArrayiv = _gl.glGetVertexArrayiv
glGetVertexArrayiv.restype = None
glGetVertexArrayiv.argtypes = (GLuint, GLenum, POINTER(GLint),)

glGetVertexArrayIndexediv = _gl.glGetVertexArrayIndexediv
glGetVertexArrayIndexediv.restype = None
glGetVertexArrayIndexediv.argtypes = (GLuint, GLuint, GLenum, POINTER(GLint),)

glGetVertexArrayIndexed64iv = _gl.glGetVertexArrayIndexed64iv
glGetVertexArrayIndexed64iv.restype = None
glGetVertexArrayIndexed64iv.argtypes = (GLuint, GLuint, GLenum, POINTER(GLint64),)

glCreateSamplers = _gl.glCreateSamplers
glCreateSamplers.restype = None
glCreateSamplers.argtypes = (GLsizei, POINTER(GLuint),)

glCreateProgramPipelines = _gl.glCreateProgramPipelines
glCreateProgramPipelines.restype = None
glCreateProgramPipelines.argtypes = (GLsizei, POINTER(GLuint),)

glCreateQueries = _gl.glCreateQueries
glCreateQueries.restype = None
glCreateQueries.argtypes = (GLenum, GLsizei, POINTER(GLuint),)

glGetQueryBufferObjecti64v = _gl.glGetQueryBufferObjecti64v
glGetQueryBufferObjecti64v.restype = None
glGetQueryBufferObjecti64v.argtypes = (GLuint, GLuint, GLenum, GLintptr,)

glGetQueryBufferObjectiv = _gl.glGetQueryBufferObjectiv
glGetQueryBufferObjectiv.restype = None
glGetQueryBufferObjectiv.argtypes = (GLuint, GLuint, GLenum, GLintptr,)

glGetQueryBufferObjectui64v = _gl.glGetQueryBufferObjectui64v
glGetQueryBufferObjectui64v.restype = None
glGetQueryBufferObjectui64v.argtypes = (GLuint, GLuint, GLenum, GLintptr,)

glGetQueryBufferObjectuiv = _gl.glGetQueryBufferObjectuiv
glGetQueryBufferObjectuiv.restype = None
glGetQueryBufferObjectuiv.argtypes = (GLuint, GLuint, GLenum, GLintptr,)

glMemoryBarrierByRegion = _gl.glMemoryBarrierByRegion
glMemoryBarrierByRegion.restype = None
glMemoryBarrierByRegion.argtypes = (GLbitfield,)

glGetTextureSubImage = _gl.glGetTextureSubImage
glGetTextureSubImage.restype = None
glGetTextureSubImage.argtypes = (GLuint, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLenum, GLsizei, POINTER(None),)

glGetCompressedTextureSubImage = _gl.glGetCompressedTextureSubImage
glGetCompressedTextureSubImage.restype = None
glGetCompressedTextureSubImage.argtypes = (GLuint, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLsizei, POINTER(None),)

glGetGraphicsResetStatus = _gl.glGetGraphicsResetStatus
glGetGraphicsResetStatus.restype = GLenum
glGetGraphicsResetStatus.argtypes = ()

glGetnCompressedTexImage = _gl.glGetnCompressedTexImage
glGetnCompressedTexImage.restype = None
glGetnCompressedTexImage.argtypes = (GLenum, GLint, GLsizei, POINTER(None),)

glGetnTexImage = _gl.glGetnTexImage
glGetnTexImage.restype = None
glGetnTexImage.argtypes = (GLenum, GLint, GLenum, GLenum, GLsizei, POINTER(None),)

glGetnUniformdv = _gl.glGetnUniformdv
glGetnUniformdv.restype = None
glGetnUniformdv.argtypes = (GLuint, GLint, GLsizei, POINTER(GLdouble),)

glGetnUniformfv = _gl.glGetnUniformfv
glGetnUniformfv.restype = None
glGetnUniformfv.argtypes = (GLuint, GLint, GLsizei, POINTER(GLfloat),)

glGetnUniformiv = _gl.glGetnUniformiv
glGetnUniformiv.restype = None
glGetnUniformiv.argtypes = (GLuint, GLint, GLsizei, POINTER(GLint),)

glGetnUniformuiv = _gl.glGetnUniformuiv
glGetnUniformuiv.restype = None
glGetnUniformuiv.argtypes = (GLuint, GLint, GLsizei, POINTER(GLuint),)

glReadnPixels = _gl.glReadnPixels
glReadnPixels.restype = None
glReadnPixels.argtypes = (GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, GLsizei, POINTER(None),)

glTextureBarrier = _gl.glTextureBarrier
glTextureBarrier.restype = None
glTextureBarrier.argtypes = ()

GL_ARB_ES2_compatibility = 1
GL_ARB_ES3_1_compatibility = 1
GL_ARB_ES3_compatibility = 1
GL_ARB_arrays_of_arrays = 1
GL_ARB_base_instance = 1
GL_ARB_bindless_texture = 1
GL_UNSIGNED_INT64_ARB = 0x140F
# XXX Skipping
# GLAPI GLuint64 APIENTRY glGetTextureHandleARB (GLuint texture);
# XXX Skipping
# GLAPI GLuint64 APIENTRY glGetTextureSamplerHandleARB (GLuint texture, GLuint sampler);
# XXX Skipping
# GLAPI void APIENTRY glMakeTextureHandleResidentARB (GLuint64 handle);
# XXX Skipping
# GLAPI void APIENTRY glMakeTextureHandleNonResidentARB (GLuint64 handle);
# XXX Skipping
# GLAPI GLuint64 APIENTRY glGetImageHandleARB (GLuint texture, GLint level, GLboolean layered, GLint layer, GLenum format);
# XXX Skipping
# GLAPI void APIENTRY glMakeImageHandleResidentARB (GLuint64 handle, GLenum access);
# XXX Skipping
# GLAPI void APIENTRY glMakeImageHandleNonResidentARB (GLuint64 handle);
# XXX Skipping
# GLAPI void APIENTRY glUniformHandleui64ARB (GLint location, GLuint64 value);
# XXX Skipping
# GLAPI void APIENTRY glUniformHandleui64vARB (GLint location, GLsizei count, const GLuint64 *value);
# XXX Skipping
# GLAPI void APIENTRY glProgramUniformHandleui64ARB (GLuint program, GLint location, GLuint64 value);
# XXX Skipping
# GLAPI void APIENTRY glProgramUniformHandleui64vARB (GLuint program, GLint location, GLsizei count, const GLuint64 *values);
# XXX Skipping
# GLAPI GLboolean APIENTRY glIsTextureHandleResidentARB (GLuint64 handle);
# XXX Skipping
# GLAPI GLboolean APIENTRY glIsImageHandleResidentARB (GLuint64 handle);
# XXX Skipping
# GLAPI void APIENTRY glVertexAttribL1ui64ARB (GLuint index, GLuint64EXT x);
# XXX Skipping
# GLAPI void APIENTRY glVertexAttribL1ui64vARB (GLuint index, const GLuint64EXT *v);
# XXX Skipping
# GLAPI void APIENTRY glGetVertexAttribLui64vARB (GLuint index, GLenum pname, GLuint64EXT *params);
GL_ARB_blend_func_extended = 1
GL_ARB_buffer_storage = 1
GL_ARB_cl_event = 1
GL_SYNC_CL_EVENT_ARB = 0x8240
GL_SYNC_CL_EVENT_COMPLETE_ARB = 0x8241
# XXX Skipping
# GLAPI GLsync APIENTRY glCreateSyncFromCLeventARB (struct _cl_context *context, struct _cl_event *event, GLbitfield flags);
GL_ARB_clear_buffer_object = 1
GL_ARB_clear_texture = 1
GL_ARB_clip_control = 1
GL_ARB_compressed_texture_pixel_storage = 1
GL_ARB_compute_shader = 1
GL_ARB_compute_variable_group_size = 1
GL_MAX_COMPUTE_VARIABLE_GROUP_INVOCATIONS_ARB = 0x9344
GL_MAX_COMPUTE_FIXED_GROUP_INVOCATIONS_ARB = 0x90EB
GL_MAX_COMPUTE_VARIABLE_GROUP_SIZE_ARB = 0x9345
GL_MAX_COMPUTE_FIXED_GROUP_SIZE_ARB = 0x91BF
# XXX Skipping
# GLAPI void APIENTRY glDispatchComputeGroupSizeARB (GLuint num_groups_x, GLuint num_groups_y, GLuint num_groups_z, GLuint group_size_x, GLuint group_size_y, GLuint group_size_z);
GL_ARB_conditional_render_inverted = 1
GL_ARB_conservative_depth = 1
GL_ARB_copy_buffer = 1
GL_ARB_copy_image = 1
GL_ARB_cull_distance = 1
GL_ARB_debug_output = 1
GL_DEBUG_OUTPUT_SYNCHRONOUS_ARB = 0x8242
GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH_ARB = 0x8243
GL_DEBUG_CALLBACK_FUNCTION_ARB = 0x8244
GL_DEBUG_CALLBACK_USER_PARAM_ARB = 0x8245
GL_DEBUG_SOURCE_API_ARB = 0x8246
GL_DEBUG_SOURCE_WINDOW_SYSTEM_ARB = 0x8247
GL_DEBUG_SOURCE_SHADER_COMPILER_ARB = 0x8248
GL_DEBUG_SOURCE_THIRD_PARTY_ARB = 0x8249
GL_DEBUG_SOURCE_APPLICATION_ARB = 0x824A
GL_DEBUG_SOURCE_OTHER_ARB = 0x824B
GL_DEBUG_TYPE_ERROR_ARB = 0x824C
GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR_ARB = 0x824D
GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR_ARB = 0x824E
GL_DEBUG_TYPE_PORTABILITY_ARB = 0x824F
GL_DEBUG_TYPE_PERFORMANCE_ARB = 0x8250
GL_DEBUG_TYPE_OTHER_ARB = 0x8251
GL_MAX_DEBUG_MESSAGE_LENGTH_ARB = 0x9143
GL_MAX_DEBUG_LOGGED_MESSAGES_ARB = 0x9144
GL_DEBUG_LOGGED_MESSAGES_ARB = 0x9145
GL_DEBUG_SEVERITY_HIGH_ARB = 0x9146
GL_DEBUG_SEVERITY_MEDIUM_ARB = 0x9147
GL_DEBUG_SEVERITY_LOW_ARB = 0x9148
# XXX Skipping
# GLAPI void APIENTRY glDebugMessageControlARB (GLenum source, GLenum type, GLenum severity, GLsizei count, const GLuint *ids, GLboolean enabled);
# XXX Skipping
# GLAPI void APIENTRY glDebugMessageInsertARB (GLenum source, GLenum type, GLuint id, GLenum severity, GLsizei length, const GLchar *buf);
# XXX Skipping
# GLAPI void APIENTRY glDebugMessageCallbackARB (GLDEBUGPROCARB callback, const void *userParam);
# XXX Skipping
# GLAPI GLuint APIENTRY glGetDebugMessageLogARB (GLuint count, GLsizei bufSize, GLenum *sources, GLenum *types, GLuint *ids, GLenum *severities, GLsizei *lengths, GLchar *messageLog);
GL_ARB_depth_buffer_float = 1
GL_ARB_depth_clamp = 1
GL_ARB_derivative_control = 1
GL_ARB_direct_state_access = 1
GL_ARB_draw_buffers_blend = 1
# XXX Skipping
# GLAPI void APIENTRY glBlendEquationiARB (GLuint buf, GLenum mode);
# XXX Skipping
# GLAPI void APIENTRY glBlendEquationSeparateiARB (GLuint buf, GLenum modeRGB, GLenum modeAlpha);
# XXX Skipping
# GLAPI void APIENTRY glBlendFunciARB (GLuint buf, GLenum src, GLenum dst);
# XXX Skipping
# GLAPI void APIENTRY glBlendFuncSeparateiARB (GLuint buf, GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha);
GL_ARB_draw_elements_base_vertex = 1
GL_ARB_draw_indirect = 1
GL_ARB_enhanced_layouts = 1
GL_ARB_explicit_attrib_location = 1
GL_ARB_explicit_uniform_location = 1
GL_ARB_fragment_coord_conventions = 1
GL_ARB_fragment_layer_viewport = 1
GL_ARB_framebuffer_no_attachments = 1
GL_ARB_framebuffer_object = 1
GL_ARB_framebuffer_sRGB = 1
GL_ARB_get_program_binary = 1
GL_ARB_get_texture_sub_image = 1
GL_ARB_gpu_shader5 = 1
GL_ARB_gpu_shader_fp64 = 1
GL_ARB_half_float_vertex = 1
GL_ARB_imaging = 1
GL_BLEND_COLOR = 0x8005
GL_BLEND_EQUATION = 0x8009
GL_ARB_indirect_parameters = 1
GL_PARAMETER_BUFFER_ARB = 0x80EE
GL_PARAMETER_BUFFER_BINDING_ARB = 0x80EF
# XXX Skipping
# GLAPI void APIENTRY glMultiDrawArraysIndirectCountARB (GLenum mode, GLintptr indirect, GLintptr drawcount, GLsizei maxdrawcount, GLsizei stride);
# XXX Skipping
# GLAPI void APIENTRY glMultiDrawElementsIndirectCountARB (GLenum mode, GLenum type, GLintptr indirect, GLintptr drawcount, GLsizei maxdrawcount, GLsizei stride);
GL_ARB_internalformat_query = 1
GL_ARB_internalformat_query2 = 1
GL_SRGB_DECODE_ARB = 0x8299
GL_ARB_invalidate_subdata = 1
GL_ARB_map_buffer_alignment = 1
GL_ARB_map_buffer_range = 1
GL_ARB_multi_bind = 1
GL_ARB_multi_draw_indirect = 1
GL_ARB_occlusion_query2 = 1
GL_ARB_pipeline_statistics_query = 1
GL_VERTICES_SUBMITTED_ARB = 0x82EE
GL_PRIMITIVES_SUBMITTED_ARB = 0x82EF
GL_VERTEX_SHADER_INVOCATIONS_ARB = 0x82F0
GL_TESS_CONTROL_SHADER_PATCHES_ARB = 0x82F1
GL_TESS_EVALUATION_SHADER_INVOCATIONS_ARB = 0x82F2
GL_GEOMETRY_SHADER_PRIMITIVES_EMITTED_ARB = 0x82F3
GL_FRAGMENT_SHADER_INVOCATIONS_ARB = 0x82F4
GL_COMPUTE_SHADER_INVOCATIONS_ARB = 0x82F5
GL_CLIPPING_INPUT_PRIMITIVES_ARB = 0x82F6
GL_CLIPPING_OUTPUT_PRIMITIVES_ARB = 0x82F7
GL_ARB_program_interface_query = 1
GL_ARB_provoking_vertex = 1
GL_ARB_query_buffer_object = 1
GL_ARB_robust_buffer_access_behavior = 1
GL_ARB_robustness = 1
GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT_ARB = 0x00000004
GL_LOSE_CONTEXT_ON_RESET_ARB = 0x8252
GL_GUILTY_CONTEXT_RESET_ARB = 0x8253
GL_INNOCENT_CONTEXT_RESET_ARB = 0x8254
GL_UNKNOWN_CONTEXT_RESET_ARB = 0x8255
GL_RESET_NOTIFICATION_STRATEGY_ARB = 0x8256
GL_NO_RESET_NOTIFICATION_ARB = 0x8261
# XXX Skipping
# GLAPI GLenum APIENTRY glGetGraphicsResetStatusARB (void);
# XXX Skipping
# GLAPI void APIENTRY glGetnTexImageARB (GLenum target, GLint level, GLenum format, GLenum type, GLsizei bufSize, void *img);
# XXX Skipping
# GLAPI void APIENTRY glReadnPixelsARB (GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLsizei bufSize, void *data);
# XXX Skipping
# GLAPI void APIENTRY glGetnCompressedTexImageARB (GLenum target, GLint lod, GLsizei bufSize, void *img);
# XXX Skipping
# GLAPI void APIENTRY glGetnUniformfvARB (GLuint program, GLint location, GLsizei bufSize, GLfloat *params);
# XXX Skipping
# GLAPI void APIENTRY glGetnUniformivARB (GLuint program, GLint location, GLsizei bufSize, GLint *params);
# XXX Skipping
# GLAPI void APIENTRY glGetnUniformuivARB (GLuint program, GLint location, GLsizei bufSize, GLuint *params);
# XXX Skipping
# GLAPI void APIENTRY glGetnUniformdvARB (GLuint program, GLint location, GLsizei bufSize, GLdouble *params);
GL_ARB_robustness_isolation = 1
GL_ARB_sample_shading = 1
GL_SAMPLE_SHADING_ARB = 0x8C36
GL_MIN_SAMPLE_SHADING_VALUE_ARB = 0x8C37
# XXX Skipping
# GLAPI void APIENTRY glMinSampleShadingARB (GLfloat value);
GL_ARB_sampler_objects = 1
GL_ARB_seamless_cube_map = 1
GL_ARB_seamless_cubemap_per_texture = 1
GL_ARB_separate_shader_objects = 1
GL_ARB_shader_atomic_counters = 1
GL_ARB_shader_bit_encoding = 1
GL_ARB_shader_draw_parameters = 1
GL_ARB_shader_group_vote = 1
GL_ARB_shader_image_load_store = 1
GL_ARB_shader_image_size = 1
GL_ARB_shader_precision = 1
GL_ARB_shader_stencil_export = 1
GL_ARB_shader_storage_buffer_object = 1
GL_ARB_shader_subroutine = 1
GL_ARB_shader_texture_image_samples = 1
GL_ARB_shading_language_420pack = 1
GL_ARB_shading_language_include = 1
GL_SHADER_INCLUDE_ARB = 0x8DAE
GL_NAMED_STRING_LENGTH_ARB = 0x8DE9
GL_NAMED_STRING_TYPE_ARB = 0x8DEA
# XXX Skipping
# GLAPI void APIENTRY glNamedStringARB (GLenum type, GLint namelen, const GLchar *name, GLint stringlen, const GLchar *string);
# XXX Skipping
# GLAPI void APIENTRY glDeleteNamedStringARB (GLint namelen, const GLchar *name);
# XXX Skipping
# GLAPI void APIENTRY glCompileShaderIncludeARB (GLuint shader, GLsizei count, const GLchar *const*path, const GLint *length);
# XXX Skipping
# GLAPI GLboolean APIENTRY glIsNamedStringARB (GLint namelen, const GLchar *name);
# XXX Skipping
# GLAPI void APIENTRY glGetNamedStringARB (GLint namelen, const GLchar *name, GLsizei bufSize, GLint *stringlen, GLchar *string);
# XXX Skipping
# GLAPI void APIENTRY glGetNamedStringivARB (GLint namelen, const GLchar *name, GLenum pname, GLint *params);
GL_ARB_shading_language_packing = 1
GL_ARB_sparse_buffer = 1
GL_SPARSE_STORAGE_BIT_ARB = 0x0400
GL_SPARSE_BUFFER_PAGE_SIZE_ARB = 0x82F8
# XXX Skipping
# GLAPI void APIENTRY glBufferPageCommitmentARB (GLenum target, GLintptr offset, GLsizeiptr size, GLboolean commit);
glNamedBufferPageCommitmentEXT = _gl.glNamedBufferPageCommitmentEXT
glNamedBufferPageCommitmentEXT.restype = None
glNamedBufferPageCommitmentEXT.argtypes = (GLuint, GLintptr, GLsizeiptr, GLboolean,)

# XXX Skipping
# GLAPI void APIENTRY glNamedBufferPageCommitmentARB (GLuint buffer, GLintptr offset, GLsizeiptr size, GLboolean commit);
GL_ARB_sparse_texture = 1
GL_TEXTURE_SPARSE_ARB = 0x91A6
GL_VIRTUAL_PAGE_SIZE_INDEX_ARB = 0x91A7
GL_NUM_SPARSE_LEVELS_ARB = 0x91AA
GL_NUM_VIRTUAL_PAGE_SIZES_ARB = 0x91A8
GL_VIRTUAL_PAGE_SIZE_X_ARB = 0x9195
GL_VIRTUAL_PAGE_SIZE_Y_ARB = 0x9196
GL_VIRTUAL_PAGE_SIZE_Z_ARB = 0x9197
GL_MAX_SPARSE_TEXTURE_SIZE_ARB = 0x9198
GL_MAX_SPARSE_3D_TEXTURE_SIZE_ARB = 0x9199
GL_MAX_SPARSE_ARRAY_TEXTURE_LAYERS_ARB = 0x919A
GL_SPARSE_TEXTURE_FULL_ARRAY_CUBE_MIPMAPS_ARB = 0x91A9
# XXX Skipping
# GLAPI void APIENTRY glTexPageCommitmentARB (GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLboolean commit);
GL_ARB_stencil_texturing = 1
GL_ARB_sync = 1
GL_ARB_tessellation_shader = 1
GL_ARB_texture_barrier = 1
GL_ARB_texture_buffer_object_rgb32 = 1
GL_ARB_texture_buffer_range = 1
GL_ARB_texture_compression_bptc = 1
GL_COMPRESSED_RGBA_BPTC_UNORM_ARB = 0x8E8C
GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM_ARB = 0x8E8D
GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT_ARB = 0x8E8E
GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_ARB = 0x8E8F
GL_ARB_texture_compression_rgtc = 1
GL_ARB_texture_cube_map_array = 1
GL_TEXTURE_CUBE_MAP_ARRAY_ARB = 0x9009
GL_TEXTURE_BINDING_CUBE_MAP_ARRAY_ARB = 0x900A
GL_PROXY_TEXTURE_CUBE_MAP_ARRAY_ARB = 0x900B
GL_SAMPLER_CUBE_MAP_ARRAY_ARB = 0x900C
GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW_ARB = 0x900D
GL_INT_SAMPLER_CUBE_MAP_ARRAY_ARB = 0x900E
GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY_ARB = 0x900F
GL_ARB_texture_gather = 1
GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET_ARB = 0x8E5E
GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET_ARB = 0x8E5F
GL_MAX_PROGRAM_TEXTURE_GATHER_COMPONENTS_ARB = 0x8F9F
GL_ARB_texture_mirror_clamp_to_edge = 1
GL_ARB_texture_multisample = 1
GL_ARB_texture_query_levels = 1
GL_ARB_texture_query_lod = 1
GL_ARB_texture_rg = 1
GL_ARB_texture_rgb10_a2ui = 1
GL_ARB_texture_stencil8 = 1
GL_ARB_texture_storage = 1
GL_ARB_texture_storage_multisample = 1
GL_ARB_texture_swizzle = 1
GL_ARB_texture_view = 1
GL_ARB_timer_query = 1
GL_ARB_transform_feedback2 = 1
GL_ARB_transform_feedback3 = 1
GL_ARB_transform_feedback_instanced = 1
GL_ARB_transform_feedback_overflow_query = 1
GL_TRANSFORM_FEEDBACK_OVERFLOW_ARB = 0x82EC
GL_TRANSFORM_FEEDBACK_STREAM_OVERFLOW_ARB = 0x82ED
GL_ARB_uniform_buffer_object = 1
GL_ARB_vertex_array_bgra = 1
GL_ARB_vertex_array_object = 1
GL_ARB_vertex_attrib_64bit = 1
GL_ARB_vertex_attrib_binding = 1
GL_ARB_vertex_type_10f_11f_11f_rev = 1
GL_ARB_vertex_type_2_10_10_10_rev = 1
GL_ARB_viewport_array = 1
GL_KHR_context_flush_control = 1
GL_KHR_debug = 1
GL_KHR_no_error = 1
GL_CONTEXT_FLAG_NO_ERROR_BIT_KHR = 0x00000008
GL_KHR_robust_buffer_access_behavior = 1
GL_KHR_robustness = 1
GL_CONTEXT_ROBUST_ACCESS = 0x90F3
GL_KHR_texture_compression_astc_hdr = 1
GL_COMPRESSED_RGBA_ASTC_4x4_KHR = 0x93B0
GL_COMPRESSED_RGBA_ASTC_5x4_KHR = 0x93B1
GL_COMPRESSED_RGBA_ASTC_5x5_KHR = 0x93B2
GL_COMPRESSED_RGBA_ASTC_6x5_KHR = 0x93B3
GL_COMPRESSED_RGBA_ASTC_6x6_KHR = 0x93B4
GL_COMPRESSED_RGBA_ASTC_8x5_KHR = 0x93B5
GL_COMPRESSED_RGBA_ASTC_8x6_KHR = 0x93B6
GL_COMPRESSED_RGBA_ASTC_8x8_KHR = 0x93B7
GL_COMPRESSED_RGBA_ASTC_10x5_KHR = 0x93B8
GL_COMPRESSED_RGBA_ASTC_10x6_KHR = 0x93B9
GL_COMPRESSED_RGBA_ASTC_10x8_KHR = 0x93BA
GL_COMPRESSED_RGBA_ASTC_10x10_KHR = 0x93BB
GL_COMPRESSED_RGBA_ASTC_12x10_KHR = 0x93BC
GL_COMPRESSED_RGBA_ASTC_12x12_KHR = 0x93BD
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_4x4_KHR = 0x93D0
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x4_KHR = 0x93D1
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x5_KHR = 0x93D2
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x5_KHR = 0x93D3
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x6_KHR = 0x93D4
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x5_KHR = 0x93D5
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x6_KHR = 0x93D6
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x8_KHR = 0x93D7
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x5_KHR = 0x93D8
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x6_KHR = 0x93D9
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x8_KHR = 0x93DA
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x10_KHR = 0x93DB
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x10_KHR = 0x93DC
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x12_KHR = 0x93DD
GL_KHR_texture_compression_astc_ldr = 1
GL_KHR_texture_compression_astc_sliced_3d = 1
del _gl
