def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before call")
        result = func(*args, **kwargs)
        print("After call")
        return result
    return wrapper

@my_decorator

def add(a, b):
    "Our add function"
    return a + b

print add(1, 3)
