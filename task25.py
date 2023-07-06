# Write a Python program to check whether a specified value is contained in a group of values.
def test(wert, liste):
    for anzahl in liste:
        if anzahl == wert:
            return True
        else:
            return False


print(test(2.1, [1, 2, 6, 3, 4, 5]))
