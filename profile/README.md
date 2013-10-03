profile
=======

[Python Profiling](http://docs.python.org/2/library/profile.html)

There are built in Python profilers to choose from `cProfile` and `profile`, both do
relatively the same thing except that `cProfile` is a C extension and `profile` is
pure Python. Meaning usually `cProfile` will have lower overhead when profiling your application.

## Running a script with profiling

```bash
python -m cProfile sample.py
   153 function calls in 5.049 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    5.049    5.049 sample.py:1(<module>)
        1    0.001    0.001    5.048    5.048 sample.py:13(parent)
       50    0.001    0.000    5.047    0.101 sample.py:4(i_am_slow)
       50    0.000    0.000    0.000    0.000 sample.py:9(i_am_fast)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       50    5.046    0.101    5.046    0.101 {time.sleep}
```


## Output Stats
There exists a built in module [pstats](http://docs.python.org/2/library/profile.html#module-pstats) which is useful for manipulating the
outputted stats from `cProfile` or `profile` commands.

For example, it can be used to load outputted stats and sort the results.

```bash
python -m cProfile -o stats.out sample.py
python sort_stats.py
Thu Oct  3 11:06:47 2013    stats.out

         153 function calls in 5.043 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    5.043    5.043 sample.py:1(<module>)
        1    0.001    0.001    5.043    5.043 sample.py:13(parent)
       50    0.001    0.000    5.042    0.101 sample.py:4(i_am_slow)
       50    5.041    0.101    5.041    0.101 {time.sleep}
       50    0.000    0.000    0.000    0.000 sample.py:9(i_am_fast)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```
