import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character types selected")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Password length should be greater than 0.")
                continue
            
            use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
            use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
            use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
            use_special = input("Include special characters? (yes/no): ").lower() == 'yes'
            
            password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
            print(f"Generated Password: {password}")
        
        except ValueError as e:
            print(e)

        repeat = input("Do you want to generate another password? (yes/no): ").lower()
        if repeat != 'yes':
            break

if __name__ == "__main__":
    main()
