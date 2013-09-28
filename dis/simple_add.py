import dis


def add(a, b):
    c = a + b
    return c


print """
def add(a, b):"
    c = a + b
    return c
"""

print "Bytecode of 'add' function:"
dis.dis(add)

print "Bytecode Explanation:"
print "  Load 'a' argument into local stack"
print "  Load 'b' argument into local stack"
print "  Pop 'a' and 'b' from the stack, add together, place result on top of stack"
print "  Store the top of the stack into local variable 'c'"
print "  Load local variable 'c' onto top of the stack"
print "  Return the top of the stack to the caller"
print ""

print "Bytecode Reference:"
print "  LOAD_FAST - Pushes a reference into the local stack"
print "  BINARY_ADD - Add the top two elements from the local stack"
print "  STORE_FAST - Put the top of the stack into local variable"
print "  RETURN_VALUE - Returns the top of the local stack to the caller"
print ""
