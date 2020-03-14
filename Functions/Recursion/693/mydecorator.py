from time import perf_counter as clock

def decorator_stopwatch(fn):
    def wrapper(*args, **kwargs):
        t1 = clock()
        result = fn(*args, **kwargs)
        t2 = clock()-t1
        print(f'time: {t2:f}s -- {fn.__name__}') 
        return result
    return wrapper