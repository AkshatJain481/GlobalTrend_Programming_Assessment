def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


try:
    n = int(input("Enter the value of n to compute the nth Fibonacci number: "))
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")

except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"Error occurred: {e}")
