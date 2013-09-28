pdd
===

[PDB](http://docs.python.org/2/library/pdb.html) is a built in Python module
used for debugging your python code execution.

## simple_code.py
For this example we will run `pdb` from the command line:
```bash
python -m pdb simple_code.py
```

This will run `pdb` directly and cause it to take control of the script at the beginning of the script.

When executed you are given the `(Pdb)` prompt which means you are running the debugger and can begin
interacting with the code.

`Pdb` is simply a Python shell, meaning we can run arbitrary Python code interactively, try running `print "hello"`, this code runs in the same code as where `Pdb` currently is, meaning we can interactively inspect and interact with the local variables in the code we are debugging.

Some useful commands:
* `h` - HELP!, shows available commands
* `l` - show where in the source code you are
* `n` - execute the current line and move to the next
* `s` - step into a function call on the current line (using `n` would execute the function but not allow you to walk through the code of that function)
* `b <line>` - set a breakpoint at the provided <line>
* `j <line>` - jump to the provided <line> skipping all other lines in between
* `whatis <variable>` - same as calling `type(<variable>)`
* `restart` - restart the script from the beginning


## set_trace.py
For this example, the code doesn't do what we expect, so we can simply add:
```python
import pdb
pdb.set_trace()
```

or also just `import pdb; pdb.set_trace()` in the code where we want the debugging
to start up and take over execution of the code.

For this example try the following:
1. `l` - show the surrounding code of where you currently are
2. `s` - step into the `recursive` function
3. `n` - move one line further in the `recursive` function
4. `a` - show the argument list for the `recursive` function
5. `print locals()` - print all local variables
6. `n` - move to the next execution line, notice it skips the body of the if statement because the if evaluates to `False`
7. `n` - move to the next execution line, we expect this to skip the body of the if since `5` is not even (hint: this is where our bug is located)
8. `l` - to see where we are in the code, which in this case we are in the body of the if we didn't expect to be in

BUG FOUND! oops, it is `if n % 2 == 0:` not `if n % 2:`

You can now either run `c` to tell the debugger to continue execution until the end of the script,
run `q` to just simply quit the debugger and the script or you can run `s` to step into the next call
to `recursive` and step through the next iteration of the function.
