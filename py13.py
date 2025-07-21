import time
from functools import wraps

# Decorator definition
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Function '{func.__name__}' started at {time.ctime(start_time)}")
        print(f"Arguments: args={args}, kwargs={kwargs}")
        
        result = func(*args, **kwargs)

        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Function '{func.__name__}' ended at {time.ctime(end_time)}")
        print(f"Execution time: {execution_time:.4f} seconds\n")
        
        return result

    return wrapper

# Apply decorator to first function
@log_execution
def add(a, b):
    time.sleep(1)  # Simulate delay
    return a + b

# Apply decorator to second function
@log_execution
def greet(name):
    time.sleep(0.5)  # Simulate delay
    return f"Hello, {name}!"

# Demonstration
sum_result = add(5, 7)
print("Sum:", sum_result)

greeting = greet("Asha")
print("Greeting:", greeting)
