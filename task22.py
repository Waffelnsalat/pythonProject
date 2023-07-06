# Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the use

input_nr = int(input("Write a number: "))

if input_nr % 2 == 0:
    print("number is even")
else:
    print("number is odd")