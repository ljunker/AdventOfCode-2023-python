import time


def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{func.__name__} ran in {t2} seconds')

    return wrapper
