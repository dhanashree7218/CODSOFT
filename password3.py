import random
import string

def generate_password():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Password length must be greater than zero.")
            return
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    print(f"Generated Password: {password}")

generate_password()
