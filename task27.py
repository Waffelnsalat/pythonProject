# Write a Python program to concatenate all elements in a list into a string and return it

def concatate(list):
    string = ""
    for number in list:
        new_string = str(number)
        string = string + new_string
    print(string)

concatate([1, 2, 5, 234, 5])