import re

def password_strength(password):
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password)
    uppercase_criteria = re.search(r'[A-Z]', password)
    digit_criteria = re.search(r'\d', password)
    special_criteria = re.search(r'[\W_]', password)
    
    criteria_met = [length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_criteria]
    strength = sum(bool(criterion) for criterion in criteria_met)
    
    if strength == 5:
        return "Very Strong"
    elif strength == 4:
        return "Strong"
    elif strength == 3:
        return "Moderate"
    else:
        return "Weak"

def main():
    password = input("Enter your password: ")
    strength = password_strength(password)
    print(f"Your password is {strength}.")

if __name__ == "__main__":
    main()
