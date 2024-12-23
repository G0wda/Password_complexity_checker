import re
    
def assess_password_strength(password):
        # Initialize criteria checks
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[^A-Za-z0-9\s]', password) is not None
    
        # Count the number of criteria met
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])
    
        # Determine the password strength
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met >= 4:
        strength = "Strong"
    elif criteria_met >= 2:
        strength = "Moderate"
    else:
        strength = "Weak"
    
        # Provide feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Password should contain at least one digit.")
    if not special_char_criteria:
        feedback.append("Password should contain at least one special character.")
    
    return strength, feedback
    
def main():
    password = input("Enter your password: ")
    strength, feedback = assess_password_strength(password)
        
    print(f"Password Strength: {strength}")
    if feedback:
        print("Suggestions:")
        for item in feedback:
            print(f"- {item}")
    
if __name__ == "__main__":
    main()                                                                                                                     
