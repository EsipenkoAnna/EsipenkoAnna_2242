import functools

def wrapper(cube_func):
    @functools.wraps(cube_func)
    def _wrapper(*args):
        list_log_args = [f'{cube_func.__name__}({el}: {type(el)})' for el in args]
        list_results = [cube_func(el) for el in args]
        print(list_log_args)
        return list_results
    return _wrapper

@wrapper
def calc_cube(x):
    return x ** 3

a = calc_cube(1, 5, 10)