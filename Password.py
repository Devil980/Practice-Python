import random
import string

def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password_to_file(password, identifier, filename="passwords.txt"):
    with open(filename, "a") as file:
        file.write(f"Generated password ({identifier}): {password}\n")

# Generate and print a password
password = generate_password()
# print("Generated Password:", password)

# Save the password to a file with a unique identifier
identifier = input("In which name do you wanna save the password: ")
save_password_to_file(password, identifier)
print(f"Password saved to 'passwords.txt' with identifier: {identifier}")