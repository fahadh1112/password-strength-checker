import re

password = input("Enter your password: ")

score = 0

# Length
if len(password) >= 8:
    score += 1
else:
    print("Password too short")

# Uppercase
if re.search(r"[A-Z]", password):
    score += 1
else:
    print("Add uppercase letter")

# Lowercase
if re.search(r"[a-z]", password):
    score += 1
else:
    print("Add lowercase letter")

# Number
if re.search(r"\d", password):
    score += 1
else:
    print("Add number")

# Special character
if re.search(r"[!@#$%^&*]", password):
    score += 1
else:
    print("Add special character")

# Final Result
if score == 5:
    print("Strong Password")
elif score >= 3:
    print("Medium Password")
else:
    print("Weak Password")