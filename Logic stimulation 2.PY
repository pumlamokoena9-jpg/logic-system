correct_username = "admin"
correct_password = "12345"

max_attempts = 3
attempt = 0

print("=== Welcome to the Login System ===")

while attempt < max_attempts:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username == correct_username and password == correct_password:
        print("\nLogin successful! ")
        break  
    else:
        attempt += 1
        print("\nIncorrect username or password.")
        if attempt < max_attempts:
            print(f"You have {max_attempts - attempt} attempt(s) left.\n")
        else:
            print("maximum attempts reached. access denied.")