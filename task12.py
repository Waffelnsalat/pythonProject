#  Write a Python program to print the calendar of a given month and year.
import calendar

y = int(input("Give a year: "))
m = int(input("Give a month: "))

print(calendar.month(y, m))