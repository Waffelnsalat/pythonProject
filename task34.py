# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.


def SUM(num1, num2):
    SUM = num1 + num2
    if SUM >= 15 and SUM <= 20:
        SUM =20
    return SUM

print(SUM(10, 5))