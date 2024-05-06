import re

def assess_password_strength(password):
    # Length check
    length_score = len(password) >= 8
    
    # Check for uppercase letters
    uppercase_score = bool(re.search(r'[A-Z]', password))
    
    # Check for lowercase letters
    lowercase_score = bool(re.search(r'[a-z]', password))
    
    # Check for numbers
    number_score = bool(re.search(r'[0-9]', password))
    
    # Check for special characters
    special_char_score = bool(re.search(r'[^A-Za-z0-9]', password))
    
    # Calculate total score
    total_score = length_score + uppercase_score + lowercase_score + number_score + special_char_score
    
    # Assess strength based on total score
    if total_score == 5:
        return "Strong"
    elif total_score >= 3:
        return "Moderate"
    else:
        return "Weak"

# Example usage
password = input("Enter your password: ")
strength = assess_password_strength(password)
print("Password strength:", strength)
