# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

n = 17
a = int(input("a number"))

if(a<n):
    d = n - a
    print(d)
else:
    d = a - n
    print(2*d)


def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2

print(difference(22))
print(difference(14))
