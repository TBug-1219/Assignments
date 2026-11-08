import string

def is_consecutive(sequence):
    """Check if a sequence of characters is consecutive."""
    for i in range(len(sequence) - 1):
        if ord(sequence[i]) + 1 != ord(sequence[i + 1]):
            return False
    return True

def is_repeating(sequence):
    """Check if all characters in a sequence are the same."""
    return len(set(sequence)) == 1

def analyze_password(password):
    """Analyze the password for weaknesses."""
    weaknesses = []
    
    # Check length
    if len(password) < 8:
        weaknesses.append("Password is fewer than 8 characters.")
    
    # Check for uppercase and lowercase letters
    if not any(c.islower() for c in password):
        weaknesses.append("Password does not contain at least one lowercase letter.")
    if not any(c.isupper() for c in password):
        weaknesses.append("Password does not contain at least one uppercase letter.")
    
    # Check for numeric digit
    if not any(c.isdigit() for c in password):
        weaknesses.append("Password does not contain at least one numeric digit.")
    
    # Check for special character
    if not any(c in string.punctuation for c in password):
        weaknesses.append("Password does not contain at least one special character.")
    
    # Check for sequences
    if password.isupper() and is_consecutive(password):
        weaknesses.append("Password is a sequence of consecutive uppercase letters.")
    if password.islower() and is_consecutive(password):
        weaknesses.append("Password is a sequence of consecutive lowercase letters.")
    if password.isdigit() and is_consecutive(password):
        weaknesses.append("Password is a sequence of consecutive numeric digits.")
    
    # Check for repeating characters
    if is_repeating(password):
        weaknesses.append("Password is a repeating sequence of characters.")
    
    # Display results
    if weaknesses:
        print("Password weaknesses found:")
        for weakness in weaknesses:
            print(f"- {weakness}")
    else:
        print("Password is strong!")

# Main program
def main():
    print("Password Strength Analyzer")
    password = input("Enter a password to analyze: ")
    analyze_password(password)

if __name__ == "__main__":
    main()
