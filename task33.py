# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero


def SUM(num1, num2, num3):
    if num1 == num2 or num2 == num3 or num3 == num1:
        SUM = 0
        return SUM
    else:
        SUM = num1 + num2 +num3
        return SUM


print(SUM(3, 2, 3))