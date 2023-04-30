import re

def validation_contact(func):
    def wrapp(*args, **kwargs):
        name, phone = args[0], args[1]
        if not re.match("^[A-Za-z ]+$", name):
             return "Invalid input. Name can only contain English letters and spaces."
        if not re.match("^\d+$", phone):
            return "Invalid input. Phone number can only contain digits."
        return func(*args, **kwargs)
    return wrapp

@validation_contact
def add(name, phone):
    contacts[name] = phone
    return f"Contact {name} with phone number {phone} has been added."


@validation_contact
def change(name, phone):
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for contact {name} has been updated to {phone}."
    else:
        return f"Contact {name} does not exist."


def phone(name):
    if name in contacts:
        return f"Phone number for contact {name} is {contacts[name]}."
    else:
        return f"Contact {name} does not exist."


def show_all():
    if not contacts:
        return "No contacts found."
    else:
        contact_list = "\n".join([f"{name} - {phone}" for name, phone in contacts.items()])
        return f"Contacts:\n{contact_list}"


def hello():
    return "How can I help you?"


def main():
    global contacts
    contacts = {}
    while True:
        command = input("Enter a command: ").lower().split()
        if not command:
            print("Invalid command. Please try again.")
            continue
        if command[0] == "hello":
            print(hello())
        elif command[0] == "add":
            if len(command) != 3:
                print("Invalid command. Please try again.")
                continue
            contact = command[1], command[2]
            print(add(*contact))
        elif command[0] == "change":
            if len(command) != 3:
                print("Invalid command. Please try again.")
                continue
            contact = command[1], command[2]
            print(change(*contact))
        elif command[0] == "phone":
            if len(command) != 2:
                print("Invalid command. Please try again.")
                continue
            print(phone(command[1]))
        elif command[0] == "show":
            if len(command) != 2:
                print("Invalid command. Please try again.")
                continue
            if command[1] == "all":
                print(show_all())
            else:
                print(phone(command[1]))
        elif command[0] in ["good", "bye", "close", "exit", "."]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
