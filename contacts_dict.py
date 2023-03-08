contacts={}
print("Hello")
print("Type 'add' to add a contact")
print("Type 'edit' to edit a contact")
print("Type 'remove' to remove a contact")
print("Type 'show' to show a contacts")
print("Type 'show all' to show a contacts")
print("Type 'stop' to close the contacts")
print()

while True:
    command=input("Please,enter a command: ")
    if command=="add":
        contact=input("Please, enter a contact: ")
        number=input("Please, enter a number: ")
        if contact not in contacts:
            contacts[contact]=number
            print("Your contact is added!")
        else:
            print("The contact is already added")
    if command=="edit":
        contact=input("Please,enter a contact: ")
        number=input("Please, enter a number: ")
        if contact in contacts:
            contacts[contact]=number
        else:
            print("I couldn't find the contact, would you like to add it?")
            print("Would you like to add it?")
            print("If yes, type add")
    if command=="remove":
        contact=input("Please,enter a contact: ")
        if contact in contacts:
            del contacts[contact]
            print("Done")
        else:
            print("I couldn't find the contact")
    if command=="show":
        contact=input("Please, enter a contact: ")
        if contact in contacts:
                print(contacts[contact])
        else:
            print("I couldn't find the contact")
    if command=="show all":
        print(contacts)
    if command=="stop":
        print("Bye")
        break
