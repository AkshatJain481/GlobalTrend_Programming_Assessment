import random
import string

def generate_random_password(length=12):
    """
    Generate a random password with specified length.

    Parameters:
    - length (int): Length of the password (default is 12).

    Returns:
    - str: Randomly generated password.
    """
    # Define characters to choose from for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password using random.choices (Python 3.6+)
    password = ''.join(random.choices(characters, k=length))
    
    return password

try:
    password_length = int(input("Enter the length of the password: "))
    if password_length <= 0:
        raise ValueError("Password length must be a positive integer.")
    
    password = generate_random_password(password_length)
    print(f"Generated Password: {password}")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"Error: {str(e)}")
