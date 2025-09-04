import json


def load_users():
    """Loads users from the users.json file.

    Returns:
        list: A list of user dictionaries or None if an error occurs.
    """
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: users.json not found. Please create the file.")
        return None
    except json.JSONDecodeError:
        print("Error: users.json is not a valid JSON file.")
        return None


def filter_users_by_name(name):
    """Filters users by name.

    Args:
        name (str): The name to filter by.
    """
    users = load_users()
    if users is not None:
        filtered_users = [user for user in users if user.get("name", "").lower() == name.lower()]

        if not filtered_users:
            print(f"No users found with the name '{name}'.")
        else:
            for user in filtered_users:
                print(user)


def filter_users_by_age(age):
    """Filters users by age.

    Args:
        age (int): The age to filter by.
    """
    users = load_users()
    if users is not None:
        filtered_users = [user for user in users if user.get("age") == age]

        if not filtered_users:
            print(f"No users found with the age '{age}'.")
        else:
            for user in filtered_users:
                print(user)


def filter_users_by_email(email):
    """Filters users by email.

    Args:
        email (str): The email to filter by.
    """
    users = load_users()
    if users is not None:
        filtered_users = [user for user in users if user.get("email", "").lower() == email.lower()]

        if not filtered_users:
            print(f"No users found with the email '{email}'.")
        else:
            for user in filtered_users:
                print(user)


def main():
    """Main function to run the user filtering program."""
    filter_option = input("Which criterion would you like to filter by? (Name/Age/E-Mail): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter by: ").strip()
        if name_to_search:
            filter_users_by_name(name_to_search)
        else:
            print("No name entered.")

    elif filter_option == "age":
        age_to_search_str = input("Enter an age to filter by: ").strip()
        try:
            age_to_search = int(age_to_search_str)
            filter_users_by_age(age_to_search)
        except ValueError:
            print("Invalid input. Please enter an integer for the age.")

    elif filter_option == "e-mail" or filter_option == "email":
        email_to_search = input("Enter an email to filter by: ").strip()
        if email_to_search:
            filter_users_by_email(email_to_search)
        else:
            print("No email entered.")
    else:
        print("This filter option is not supported.")


if __name__ == "__main__":
    main()
    
