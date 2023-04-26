def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact name not found. Please provide a valid name."
        except ValueError:
            return "Invalid input. Please provide the correct input."
        except IndexError:
            return "Invalid input. Please provide valid input."
    return wrapper


def hello():
    return "How can I help you?"


def add(contact):
    name, phone = contact.split()
    contacts[name] = phone
    return "Contact {} with phone number {} has been added.".format(name, phone)


def change(contact):
    name, phone = contact.split()
    if name in contacts:
        contacts[name] = phone
        return "Phone number for contact {} has been updated to {}.".format(name, phone)
    else:
        return "Contact {} does not exist.".format(name)


def phone(name):
    if name in contacts:
        return "Phone number for contact {} is {}.".format(name, contacts[name])
    else:
        return "Contact {} does not exist.".format(name)


def show_all():
    if not contacts:
        return "No contacts found."
    else:
        contact_list = "\n".join(["{} - {}".format(name, phone) for name, phone in contacts.items()])
        return "Contacts:\n{}".format(contact_list)


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
            contact = "{} {}".format(command[1], command[2])
            print(add(contact))
        elif command[0] == "change":
            if len(command) != 3:
                print("Invalid command. Please try again.")
                continue
            contact = "{} {}".format(command[1], command[2])
            print(change(contact))
        elif command[0] == "phone":
            if len(command) != 2:
                print("Invalid command. Please try again.")
                continue
            print(phone(command[1]))
        elif command[0] == "show":
            if len(command) != 2 or command[1] != "all":
                print("Invalid command. Please try again.")
                continue
            print(show_all())
        elif command[0] in ["good", "bye", "close", "exit", "."]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()

