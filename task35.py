# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

def torf(num1, num2):
    torf = bool(num1 == num2 or num1 + num2 == 5)
    return torf

print(torf(3, 2))
print(torf(5, 2))
print(torf(7, 7))
