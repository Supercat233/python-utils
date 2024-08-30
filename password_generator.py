import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    password = generate_password(length)
    print("Generated password:", password)
