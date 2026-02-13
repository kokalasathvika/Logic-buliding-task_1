# Given list of names
names = [" Alice ", "bob", " CHARLIE "]


def clean_names(name_list):
    """
    Function to clean names by:
    - Removing extra spaces
    - Converting to lowercase
    Returns cleaned list.
    """
    cleaned_list = []

    for name in name_list:
        cleaned_name = name.strip().lower()
        cleaned_list.append(cleaned_name)

    return cleaned_list


def main():
    """Main function to execute data cleaning."""
    
    cleaned_names = clean_names(names)

    print("Original Names:", names)
    print("Cleaned Names:", cleaned_names)


# Run the program
if __name__ == "__main__":
    main()