# Given list of messages
messages = ["Hi", "Welcome to the platform", "OK"]


def analyze_messages(message_list):
    """
    Function to analyze message lengths.
    Prints length and flags long messages.
    """
    for message in message_list:
        length = len(message)
        print("Message:", message)
        print("Length:", length)

        if length > 10:
            print("Status: Long Message ⚠")
        else:
            print("Status: Short Message")

        print("-" * 30)


def main():
    """Main function to execute message analysis."""
    analyze_messages(messages)


# Run the program
if __name__ == "__main__":
    main()