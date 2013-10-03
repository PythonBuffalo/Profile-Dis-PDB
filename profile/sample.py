import time


def i_am_slow(n):
    time.sleep(0.1)
    return n - 1


def i_am_fast(n):
    return n - 1


def parent(total):
    for n in xrange(total):
        if n % 2 == 0:
            i_am_slow(n)
        else:
            i_am_fast(n)


parent(100)
