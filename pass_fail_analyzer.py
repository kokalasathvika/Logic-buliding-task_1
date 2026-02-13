# Given marks list
marks = [45, 78, 90, 33, 60]


def analyze_results(marks_list):
    """
    Function to count pass and fail students.
    Returns total_pass and total_fail.
    """
    total_pass = 0
    total_fail = 0

    for mark in marks_list:
        if mark >= 50:
            total_pass += 1
        else:
            total_fail += 1

    return total_pass, total_fail


def main():
    """Main function to execute result analysis."""
    
    pass_count, fail_count = analyze_results(marks)

    print("Student Marks:", marks)
    print("Total Students:", len(marks))
    print("Number of Students Passed:", pass_count)
    print("Number of Students Failed:", fail_count)


# Run the program
if __name__ == "__main__":
    main()