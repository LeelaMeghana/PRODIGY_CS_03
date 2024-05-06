import re

def assess_password_strength(password):
    
    length_score = len(password) >= 8  # Length check
    
    uppercase_score = bool(re.search(r'[A-Z]', password))  # Check for uppercase letters
    
    lowercase_score = bool(re.search(r'[a-z]', password))  # Check for lowercase letters
    
    number_score = bool(re.search(r'[0-9]', password))  # Check for numbers
    
    special_char_score = bool(re.search(r'[^A-Za-z0-9]', password))  # Check for special characters
    
    total_score = length_score + uppercase_score + lowercase_score + number_score + special_char_score
    
    # Assess strength based on total score
    if total_score == 5:
        return "Strong"
    elif total_score >= 3:
        return "Moderate"
    else:
        return "Weak"

password = input("Enter your password: ")
strength = assess_password_strength(password)
print("Password strength:", strength)
