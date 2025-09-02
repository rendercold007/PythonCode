import random
import string


def check_strength (password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    if len(password) >= 12 and has_upper and has_lower and has_digit and has_symbol:
        return "Strong"
    elif len(password) >=8 and has_upper and has_lower and has_digit:
        return "Medium"
    else:
        return "Weak"
    
def generate_password(l, use_symbols):
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation

    password = ""
    for i in range(l):
        password += random.choice(characters)
    return password


print("PASSWORD GENERATOR")
print("-" * 23)

l = int(input("Enter the length of password: "))
ct = int(input("How many passwords to generate: "))
include_symbols = input("Include symbols? (y/n): ").lower() == "y"

print("\n Your passwords: ")
for i in range(ct):
    password = generate_password(l, include_symbols)
    strength = check_strength(password)
    print(f"  {password} [{strength}]")    