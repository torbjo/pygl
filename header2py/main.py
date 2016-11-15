
def output_define (name, value):
    print (name, '=', value)


def output_function (name, rtype, arglist):
    #arglist = [a for a in arglist if a is not None]  # filter out empty args
    print ('{} = _gl.{}'.format (name, name))
    print ('{}.restype = {}'.format (name, 'None' if rtype=='void' else rtype))
    if arglist == [None]:
        print ('{}.argtypes = ()'.format (name))
    else:
        print ('{}.argtypes = ({},)'.format (name, ', '.join(arglist)))
    print()


# Convert from C type to Python ctypes type.
# Note: Does not handle all cases. Only stuff used in glcorearb.h
def c_type_to_python (arg):
    if arg.strip() == 'void':   # xxx only for return types
        return None
        #return 'None'
    oarg = arg  # debug
    pc = arg.count('*')     # ptrcnt
    arg = arg.replace ('*', '')
    arg = arg.replace ('const', '').strip()

    #assert len(arg.split()) == 2
    #type_, name = arg.split()

    nparts = len (arg.split())
    if nparts == 2:
        type_, _ = arg.split()
    elif nparts == 1:
        type_ = arg
    else:
        assert False

    #print ('XXX', type_, '\t', arg, '\t', oarg)

    if type_ == 'void':
        type_ = 'None'

    if pc == 1:
        type_ = 'POINTER(%s)' % type_
    elif pc == 2:
        type_ = 'POINTER(POINTER(%s))' % type_
    elif pc > 2:
        assert False

    # @todo better: just replace 'void' with None
#    if pc == 1:
#        if arg.startswith ('void'):     # 'void '?
#            type_ = 'c_void_p'
#        else:
#            type_ = 'POINTER(%s)' % type_
#    elif pc == 2:
#        type_ = 'POINTER(POINTER(%s))' % type_
#    elif pc > 2:
#        assert False

    return type_



def parse_function (line):
    # GLAPI void APIENTRY glDepthRange (GLdouble near, GLdouble far);
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
        if line.startswith ('GLAPI'):
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
