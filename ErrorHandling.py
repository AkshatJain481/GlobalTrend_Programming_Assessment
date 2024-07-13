def divide_numbers():
    try:
        dividend = float(input("Enter the dividend: "))
        divisor = float(input("Enter the divisor: "))

        result = dividend / divisor
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Please enter valid numeric values for dividend and divisor."


result = divide_numbers()
print(result)
