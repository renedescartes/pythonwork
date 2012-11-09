import time

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap

def find(f, seq):
    """Return first item in sequence where f(item) == True."""
    #http://tomayko.com/writings/cleanest-python-find-in-list-function
    for item in seq:
        if f(item):
            return item
    return None