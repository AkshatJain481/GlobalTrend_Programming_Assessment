def perform_arithmetic_operation(a, b, operator):
    """
    Perform arithmetic operation based on operator.

    Parameters:
    - a (float or int): First operand.
    - b (float or int): Second operand.
    - operator (str): Arithmetic operator ('+', '-', '*', '/').

    Returns:
    - float or int: Result of the arithmetic operation.
    """
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b
    else:
        raise ValueError("Invalid operator. Please use '+', '-', '*', or '/'.")


try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    op = input("Enter the operator (+, -, *, /): ")

    result = perform_arithmetic_operation(a, b, op)
    print(f"Result of {a} {op} {b} = {result}")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"Error: {str(e)}")
