import time
import functools

def measure_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        arg_str = ', '.join(repr(arg) for arg in args)
        kwargs_str = ', '.join(f"{key}={value!r}" for key, value in kwargs.items())
        args_str = ', '.join(filter(None, [arg_str, kwargs_str]))
        print(f"Execution time for '{func.__name__}({args_str})': {execution_time:.6f} seconds")
        return result
    return wrapper

# Example function that performs a computationally expensive task
@measure_execution_time
def compute_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

@measure_execution_time
def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

# Example usage with user input
def main():
    # Example with compute_factorial function
    try:
        n = int(input("Enter a number to compute factorial: "))
        result_factorial = compute_factorial(n)
        print(f"{n}! = {result_factorial}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

    # Example with divide_numbers function
    try:
        a = float(input("Enter a dividend: "))
        b = float(input("Enter a divisor: "))
        result_division = divide_numbers(a, b)
        print(f"Result of division: {result_division}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")

if __name__ == "__main__":
    main()
