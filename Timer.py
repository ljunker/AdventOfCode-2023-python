import time


def timer(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time() - t1
        print(f'{func.__name__} ran in {t2} seconds')

    return wrapper
