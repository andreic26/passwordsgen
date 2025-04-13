from random import choice

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
similar_symbols = "il1Lo0O"

chars = ""


def boolean_input(prompt):
    while True:
        value = input(prompt + " (y/n): ").strip().lower()
        if value == "y":
            return True
        elif value == "n":
            return False


password_count = int(input("Number of passwords to be generated: "))
password_length = int(input("Password length: "))

digits_need = boolean_input("Include numbers?\n")

uppercase = boolean_input("Include uppercase characters?\n")

lowercase = boolean_input("Include lowercase characters?\n")

special = boolean_input("Include special symbols?\n")

similar = boolean_input("Exclude similar characters?\n")

if digits_need:
    chars += digits
if uppercase:
    chars += uppercase_letters
if lowercase:
    chars += lowercase_letters
if special:
    chars += punctuation
if similar:
    chars = "".join([c for c in chars if c not in similar_symbols])


def generate_password(length, chars, count):

    password = ""

    for _ in range(count):
        password = ""
        for _ in range(length):
            password += choice(chars)

        print(password)


generate_password(password_length, chars, password_count)
