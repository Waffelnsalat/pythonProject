# Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
def new_string(str):
  if len(str) >= 2 and str[:2] == "Is":
    return str
  return "Is" + str

print(new_string("Array"))


def addIs(string):
    if len(string) >= 2 and string[:2] == "Is":
      return string
    return "Is" + string

print(addIs("IsArray"))
