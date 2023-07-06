#  Write a Python program to accept a filename from the user and print the extension of that.

filename = input()
out_f = filename.split(".")
print(out_f)
print(out_f[-1])
