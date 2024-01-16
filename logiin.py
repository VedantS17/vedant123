import getpass

def login():
    # Predefined username and password (you would replace this with a database lookup)
    correct_username = "user123"
    correct_password = "password123"

    # Get user input
    input_username = input("Enter your username: ")
    input_password = getpass.getpass("Enter your password: ")

    # Check if the input matches the predefined values
    if input_username == correct_username and input_password == correct_password:
        print("Login successful!")
    else:
        print("Invalid username or password. Please try again.")

# Call the login function to start the program
login()
