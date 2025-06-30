import json


def filter_users_by_name(name):
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("Fehler: users.json nicht gefunden. Bitte erstelle die Datei.")
        return
    except json.JSONDecodeError:
        print("Fehler: users.json ist keine valide JSON-Datei.")
        return

    filtered_users = [user for user in users if user.get("name", "").lower() == name.lower()]

    if not filtered_users:
        print(f"Keine Benutzer mit dem Namen '{name}' gefunden.")
    else:
        for user in filtered_users:
            print(user)


def filter_users_by_age(age):
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("Fehler: users.json nicht gefunden. Bitte erstelle die Datei.")
        return
    except json.JSONDecodeError:
        print("Fehler: users.json ist keine valide JSON-Datei.")
        return

    filtered_users = [user for user in users if user.get("age") == age]

    if not filtered_users:
        print(f"Keine Benutzer mit dem Alter '{age}' gefunden.")
    else:
        for user in filtered_users:
            print(user)


def filter_users_by_email(email):
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("Fehler: users.json nicht gefunden. Bitte erstelle die Datei.")
        return
    except json.JSONDecodeError:
        print("Fehler: users.json ist keine valide JSON-Datei.")
        return

    filtered_users = [user for user in users if user.get("email", "").lower() == email.lower()]

    if not filtered_users:
        print(f"Keine Benutzer mit der E-Mail '{email}' gefunden.")
    else:
        for user in filtered_users:
            print(user)


if __name__ == "__main__":
    filter_option = input("Nach welchem Kriterium möchtest du filtern? (Name/Alter/E-Mail): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Gib einen Namen zum Filtern ein: ").strip()
        if name_to_search:
            filter_users_by_name(name_to_search)
        else:
            print("Kein Name eingegeben.")

    elif filter_option == "alter":
        age_to_search_str = input("Gib ein Alter zum Filtern ein: ").strip()
        try:
            age_to_search = int(age_to_search_str)
            filter_users_by_age(age_to_search)
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine ganze Zahl für das Alter ein.")

    elif filter_option == "e-mail" or filter_option == "email":
        email_to_search = input("Gib eine E-Mail zum Filtern ein: ").strip()
        if email_to_search:
            filter_users_by_email(email_to_search)
        else:
            print("Keine E-Mail eingegeben.")
    else:
        print("Diese Filteroption wird nicht unterstützt.")

