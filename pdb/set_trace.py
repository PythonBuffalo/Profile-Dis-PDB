def recursive(n):
    if n <= 0:
        return 0
    if n % 2:
        return n + recursive(n - 2)
    else:
        return n + recursive(n - 1)


# we expect 11, but get 9... something is wrong here
# use pdb.set_trace() to add a breakpoint and start up pdb
import pdb
pdb.set_trace()
print recursive(5)
