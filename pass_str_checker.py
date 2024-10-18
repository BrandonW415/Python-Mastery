import re

def check_password_strength(password):
    if len(password) < 7:
        return False, "Password must be at least 7 characters minimum."
    
    if not re.search(r"[!@#$%^&*()<>?]", password):
        return False, "Password must contain a special character."
    
    if not re.search(r"\d", password):
        return False, "Password must contain a number."
    
    if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password):
        return False, "Password must contain one uppercase and one lowercase letter."
    
    return True, "Strong Password!"

def get_password_strength(password):
    strength = 0
    if len(password) >=12:
        strength += 1
    if len(re.findall(r"\d", password)) > 1:
        strength += 1
    if len(re.findall(r"[!@#$%^&*()<>?]", password)) > 1:
        strength += 1
    return "Very Strong" if strength >= 2 else "Strong"

def main():
    print("Welcome to the Password Strength Checker!")
    print("A strong password must:")
    print("1. Be at least 7 characters long.")
    print("2. Must contain at least 1 special character.")
    print("3. Must contain at least 1 number.")
    print("4. Must contain an uppercase and a lowercase letter.")
    
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        password = input("\nEnter a password to check (or press 'q' to quit): ")
        
        if password.lower() == 'q':
            print("Thank you for using the Password Strength Checker. Have a great day!")
            break
        
        is_strong, message = check_password_strength(password)
        
        if is_strong:
            strength = get_password_strength(password)
            print(f"Password strength: {strength}")
            print(message)
            
            check_another = input("Would you like to check another password at this time? (Y/N): ")
            if check_another.lower() != 'y':
                print("Thank you for using the Password Strength Checker. Goodbye!")
                break
        else:
            print(f"Password is not strong enough. {message}")
            attempts += 1
            if attempts < max_attempts:
                print(f"You have {max_attempts - attempts} attempts left.")
            else:
                print("You have reached the maximum number of attempts! Please try again later.")
                
if __name__ == "__main__":
    main()