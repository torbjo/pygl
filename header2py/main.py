r""" Converts OpenGL C header to Python (using ctypes).

Note: This *not* a C parser. It only implements enough to parse
the OpenGL headers from the Kronos group.

For a generic tool to convert C headers to Python, check out:
https://github.com/trolldbois/ctypeslib
"""


def output_define (name, value):
    print (name, '=', value)


def output_function (name, rtype, arglist):
    #arglist = [a for a in arglist if a is not None]  # filter out empty args
    print ('{} = _gl.{}'.format (name, name))
    print ('{}.restype = {}'.format (name, 'None' if rtype=='void' else rtype))
    if arglist == ['None']:
        print ('{}.argtypes = ()'.format (name))
    else:
        print ('{}.argtypes = ({},)'.format (name, ', '.join(arglist)))
    print()


def c_type_to_python (arg):
    '''Convert from C type to Python ctypes type. Note: Does not handle
    all cases, only types used in glcorearb.h'''
#    oldarg = arg  # debug
    ptrcnt = arg.count('*')     # pointer indirection count
    arg = arg.replace ('*', '')
    arg = arg.replace ('const', '').strip()

    nparts = len (arg.split())
    if nparts == 2:
        type_, _ = arg.split()
    elif nparts == 1:
        type_ = arg
    else:
        assert False

    #print ('!!!', type_, '\t', arg, '\t', oldarg)

    if type_ == 'void':
        type_ = 'None'  # ctypes uses None for void

    if ptrcnt == 1:
        if type_ == 'GLchar':
            type_ = 'STRING'
        else:
            type_ = 'POINTER(%s)' % type_
    elif ptrcnt == 2:
        if type_ == 'GLchar':
            type_ = 'POINTER(STRING)'
        else:
            type_ = 'POINTER(POINTER(%s))' % type_
    elif ptrcnt > 2:
        assert False    # more than 2 levels of indirection is not used

    return type_



def parse_function (line):
    # Input: GLAPI void APIENTRY glDepthRange (GLdouble near, GLdouble far);
    l = line[5:-1]      # skip GLAPI and final semicolon
    i = l.index ('APIENTRY')
    rtype = l[0:i].strip()
    rtype = c_type_to_python (rtype)
    name, args = l[i+9:].split (maxsplit=1)  # i+9 => skip APIENTRY
    if name.endswith ('ARB'):   # tmp hack
        return
#    print ('# ' + name)
    arglist = [c_type_to_python(arg) for arg in args[1:-2].split(',')]
    #do_func (name, rtype, arglist)
    return name, rtype, arglist



def parse_define (line):
    _, name, value = line.split()
    value = value.rstrip ('u')
    if value.endswith ('ull'):
        value = value[:-3]
    return (name, value)



def main (fp):
    for line in fp.readlines():
        if line.startswith ('GLAPI '):
            func = parse_function (line)
            if func:
                output_function (*func)
            else:
                print ('# XXX Skipping')
                print ('#', line.rstrip())
        elif line.startswith ('#define GL_'):
            output_define (*parse_define (line))



if __name__ == '__main__':
    import sys
    main (sys.stdin)
