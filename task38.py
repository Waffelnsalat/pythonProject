# Write a Python program to solve (x + y) * (x + y).

def result(x, y):
    RESULT = (x + y) * (x + y)
    return RESULT

print(result(4, 3))

x, y = 4, 3
result = x * x + 2 * x * y + y * y
print("({} + {}) ^ 2) = {}".format(x, y, result))