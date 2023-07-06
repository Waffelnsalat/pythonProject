# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.

copie_n = int(input("write a number: "))
string_i = input("write a string: ")
result = ""
for i in range(copie_n):
    result2 = string_i[0] + string_i[2]
    result = result + result2
print(result)
