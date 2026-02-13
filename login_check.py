# Predefined correct credentials
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "1234"


def login_check(username, password):
    """
    Function to verify user credentials.
    Returns True if credentials match, otherwise False.
    """
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        return True
    else:
        return False


def main():
    """Main function to execute login system."""
    
    # Taking input from user
    entered_username = input("Enter username: ")
    entered_password = input("Enter password: ")

    # Checking login credentials
    if login_check(entered_username, entered_password):
        print("Login Successful")
    else:
        print("Invalid Credentials")


# Run the program
if __name__ == "__main__":
    main()