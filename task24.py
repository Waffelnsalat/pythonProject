# Write a Python program to test whether a passed letter is a vowel or not.
# Program taks an array from user and counts the vowels in the array

numbers = (input("Type in some letter with a \",\" between (no space)"))
list = numbers.split("," or ".")
vowel = 0
a = int(len(list))

for i in range(a):
    count = 0
    count = int(list[i].count('a' or 'i' or 'e' or 'o' or 'u'))
    vowel =vowel + count

print(vowel)

