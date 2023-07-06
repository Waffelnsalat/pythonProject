# Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.

def futvalue(amt, percent, time):
    for z in range(time-1):
        amt = amt + (amt/100 * percent)
    return amt
print(futvalue(10000, 3.5, 7))

amt = 10000
int = 3.5
years = 7
future_value = amt*((1+(0.01*int)) ** years)
print(round(future_value, 2))