# Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.

c = int(input("A number: "))
b = int(input("A number: "))
a = int(input("A number: "))

sum_abc = a + b + c

if(a == b or b == c or a == c) :
    print(3 * sum_abc)
else:
    print(sum_abc)


def sum_thrice(x, y, z):
    sum = x + y + z

    if x == y == z:
        sum = sum * 3
    return sum


print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))
