# Given list of logs
logs = ["INFO", "ERROR", "WARNING", "ERROR"]


def count_errors(log_list):
    """
    Function to count number of 'ERROR' entries.
    Returns total error count.
    """
    error_count = 0

    for log in log_list:
        if log == "ERROR":
            error_count += 1

    return error_count


def main():
    """Main function to execute error detection."""
    
    total_errors = count_errors(logs)

    print("System Logs:", logs)
    print("Total ERROR entries:", total_errors)


# Run the program
if __name__ == "__main__":
    main()