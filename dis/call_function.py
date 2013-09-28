import dis
import time


def print_time():
    now = time.time()
    print now

print """
import time

def print_time():
    now = time.time()
    print now
"""

print "Bytecode of 'print_time' function:"
dis.dis(print_time)
print ""

print "Explanation:"
print "  Load the global called 'time' onto top of the stack"
print "  Load the attribute 'time' of element at top of stack and store that attribute ontop of stack"
print "  Pop and call the function at the top of the stack and store the return of function ontop of stack"
print "  Store the top of the stack into variable 'now'"
print "  Load the variable 'now' onto the top of the stack"
print "  Print the element at the top of the stack"
print "  Print a newline"
print "  Load None onto top of stack"
print "  Return the top of the stack to the caller"
print ""

print "Bytecode Reference:"
print "  LOAD_GLOBAL - Load the global item onto the top of the stack"
print "  LOAD_ATTR - Replaces the top of the stack with an attribute of the element at top of the stack"
print "  CALL_FUNCTION - Call the function at the top of the stack"
print "  STORE_FAST - Put the top of the stack into local variable"
print "  LOAD_FAST - Put the local variable on top of the stack"
print "  PRINT_ITEM - Print the element at the top of the stack"
print "  PRINT_NEWLINE - Print a newline"
print "  LOAD_CONST - Load a constant on top of the stack"
print "  RETURN_VALUE - Return the top of the stack to the caller"
print ""
