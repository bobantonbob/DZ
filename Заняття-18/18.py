import time

def speed_test(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання {function.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper


@speed_test
def my_function(time):
