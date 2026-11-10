# contacts = {}

# name = input("name: ")
# phone = input("phone: ")

# contacts[name] = phone
# contacts["Omollo"] = "071111111" 

# print(contacts)

import json

try:
    with open("contacts.json") as f:
        contacts = json.load(f)
except FileNotFoundError:
    contacts = {}


while True:
    print("\n--- Contact Book ---")
    print("1. Add contact")
    print("2. View all")
    print("3. Search")
    print("4. Edit")
    print("5. Delete")
    print("6. Quit")

    choice = input("Choose (1-6): ")

    if choice == "1":
        name = input("Name: ").strip().title()

        if name == "":
            print("Name cannot be empty.")
            continue

        phone = input("Phone: ").strip()
        
        if phone =="":
            print("phone cannot be empty!")
            continue
        
        contacts[name] = phone
        print(f"{name} saved.")

        with open("contacts.json", "w") as f:
            json.dump(contacts, f)

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts yet.")
        else:
            for name, phone in contacts.items():
                print(f"{name}: {phone}")

    elif choice == "3":
        name = input("Search name: ").strip().title()
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Not found.")
            
    elif choice == "4":
        name = input("Edit which name: ").strip().title()

        if name in contacts:
            new_phone = input("New phone: ").strip()
            contacts[name] = new_phone
            print(f"{name} updated.")

            with open("contacts.json", "w") as f:
                json.dump(contacts, f)
        else:
            print("Not found.")        

    elif choice == "5":
        name = input("Delete which name: ").strip().title()
        if name in contacts:
            del contacts[name]
            print(f"{name} deleted.")
        else:
            print("Not found.")
            
        with open("contacts.json", "w") as f:
            json.dump(contacts, f)      

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")