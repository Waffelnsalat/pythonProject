#  Write a Python program to test whether a number is within 100 of 1000 or 2000.

test_nr = int(input("A number: "))

if(test_nr < 1100 and test_nr > 900 ):
    print("Number is in the range")
elif(test_nr < 2100 and test_nr > 1900 ):
    print("Number is in the range")
else:
    print("Number is not in range")


def near_thousand(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(2200))