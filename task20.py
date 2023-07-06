# Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def larger_string(str, n):
   result = ""
   for i in range(n):
      result = result + str
   return result

print(larger_string('abcd', 2))
print(larger_string('.py', 6))


a = 3

for i in range(a):
   print(i)
