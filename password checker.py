import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r"[A-Z]", password))
    lowercase_criteria = bool(re.search(r"[a-z]", password))
    digit_criteria = bool(re.search(r"\d", password))
    special_char_criteria = bool(re.search(r"[!@#$%^&*()-+=]", password))

    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_char_criteria:
        return "Strong"
    elif length_criteria and (uppercase_criteria or lowercase_criteria) and digit_criteria:
        return "Moderate"
    else:
        return "Weak"

password = input("Enter your password: ")
strength = assess_password_strength(password)
print("Password strength:", strength)
