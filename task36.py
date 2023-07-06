# Write a Python program to add two objects if both objects are an integer type.

def testing(num1, num2):
    if type(num1) is int and type(num2) is int:
        res = num1 + num2
        return "These are intigers! Result: " + str(res)
    else:
        return "These are not intigers!"


print(testing(113, 2))


def add_numbers(a, b):
   if not (isinstance(a, int) and isinstance(b, int)):
       return "Inputs must be integers!"
   return a + b
print(add_numbers(10, 20))
print(add_numbers(10, 20.23))
print(add_numbers(5, 6))
print(add_numbers(5, '6'))
