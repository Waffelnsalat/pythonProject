# Write a Python program to check whether a file exists.


import os.path
print(os.path.isfile('main.txt'))
print(os.path.isfile('main.py'))

my_file = open('main.py')
try:
   my_file.close()
   print("File found!")
except FileNotFoundError:
   print("File not found!")