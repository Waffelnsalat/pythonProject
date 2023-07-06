# Write a Python program to create a histogram from a given list of integers.

def histogram(list):
    for number in list:
        symbol = ""
        for x in range(number):
            symbol = symbol + "@"
        print(symbol)


histogram([4, 1, 2, 5, 1, 6, 7, 20, 1])
