#  Write a Python program to display your details like name, age, address in three different lines.




def personal_data(name, age, address1, address2):
    fullname = name.split()
    plzacity = address1.split(' ', 1)
    streetahnr = address2.rsplit(' ', 1)
    middlename = "Yes"
    #Design
    print("")
    print("")
    print("First Name: " + fullname[0] + ". Last Name: " + fullname[-1])
    print("Age: " + str(age))
    print("PLZ number: " + str(plzacity[0] + ". City: " + plzacity[-1]))
    print("Street: " + str(streetahnr[0]) +". Housenumber: " + str(streetahnr[-1]))
    if len(fullname) > 2:
        middlename = input("You seem to have a middlename. Do you want it in your address? Y/n ")
    if middlename.__contains__("Yes" or "yes" or "Y" or "y"):
        print("YOUR ADDRESS:")
        print(name)
        print(address2)
        print(address1)
    else:
        print("YOUR ADDRESS:")
        print(fullname[0] + " " + fullname[-1])
        print(address2)
        print(address1)

personal_data(input("Write your full name: "), input("Write your age: "),
              input("Write your first addresspart: (PLZ, CITY): "), input("Write your second addresspart: (STREET, HOUSENUMBER)"))