#Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

def GCD(num1, num2):
    multi2 = 0
    multi3 = 0
    multi5 = 0
    multi7 = 0
    multi11 = 0
    multi13 = 0
    multi2for2 = 0
    multi3for2 = 0
    multi5for2 = 0
    multi7for2 = 0
    multi11for2 = 0
    multi13for2 = 0
    GCD = 1
    while num1 % 2 == 0:
        num1 = num1/2
        print(num1)
        multi2 = multi2 + 1
    while num1 % 3 == 0:
        num1 = num1 / 3
        print(num1)
        multi3 = multi3 + 1
    while num1 % 5 == 0:
        num1 = num1 / 5
        print(num1)
        multi5 = multi5 + 1
    while num1 % 7 == 0:
        num1 = num1 / 7
        print(num1)
        multi7 = multi7 + 1
    while num1 % 11 == 0:
        num1 = num1 / 11
        print(num1)
        multi11 = multi11 + 1
    while num1 % 13 == 0:
        num1 = num1 / 13
        print(num1)
        multi13 = multi13 + 1
    while num2 % 2 == 0:
        num2 = num2/2
        print(num2)
        multi2for2 = multi2for2 + 1
    while num2 % 3 == 0:
        num2 = num2 / 3
        print(num2)
        multi3for2 = multi3for2 + 1
    while num2 % 5 == 0:
        num2 = num2 / 5
        print(num2)
        multi5for2 = multi5for2 + 1
    while num2 % 7 == 0:
        num2 = num2 / 7
        print(num2)
        multi7for2 = multi7for2 + 1
    while num2 % 11 == 0:
        num2 = num2 / 11
        print(num2)
        multi11for2 = multi11for2 + 1
    while num2 % 13 == 0:
        num2 = num2 / 13
        print(num2)
        multi13for2 = multi13for2 + 1
    if multi2 >= multi2for2 and not 0:
        for n in range(multi2for2):
            GCD = GCD * 2
    if multi2 < multi2for2 and not 0:
        for n in range(multi2):
            GCD = GCD * 2
    if multi3 >= multi3for2 and not 0:
        for n in range(multi3for2) :
            GCD = GCD * 3
    if multi3 < multi3for2 and not 0:
        for n in range(multi3):
            GCD = GCD * 3
    if multi5 >= multi5for2 and not 0:
        for n in range(multi5for2):
            GCD = GCD * 5
    if multi5 < multi5for2 and not 0:
        for n in range(multi5):
            GCD = GCD * 5
    if multi7 >= multi7for2 and not 0:
        for n in range(multi7for2):
            GCD = GCD * 7
    if multi7 < multi7for2 and not 0:
        for n in range(multi7):
            GCD = GCD * 7
    if multi11 >= multi11for2 and not 0:
        for n in range(multi11for2):
            GCD = GCD * 11
    if multi11 < multi11for2 and not 0:
        for n in range(multi11):
            GCD = GCD * 11
    if multi13 >= multi13for2 and not 0:
        for n in range(multi13for2):
            GCD = GCD * 13
    if multi13 < multi13for2 and not 0:
        for n in range(multi13):
            GCD = GCD * 13
    if num1 == 1 and num2 == 1:
        print(GCD)
    else:
        print("The numbers are out of range")
GCD(330,30)


def gcd(x, y):
   gcd = 1
   if x % y == 0:
       return y
   for k in range(int(y / 2), 0, -1):
       if x % k == 0 and y % k == 0:
           gcd = k
           break
   return gcd
print("GCD of 12 & 17 =", gcd(12, 17))
print("GCD of 4 & 6 =", gcd(4, 6))
print("GCD of 336 & 360 =", gcd(334, 360))




def LCM2(num1, num2):
    if num1 == num2:
        LCM2 = num2
        return LCM2
    elif num1 > num2:
        for k in range(num2, 1, -1):
            if not k == 0 and (num1 % k == 0) and (num2 % k == 0):
                LCM2 = k
                return LCM2
    elif num1 < num2:
        for k in range(num1, 1, -1):
            if not k == 0 and num1 % k == 0 and num2 % k == 0:
                LCM2 = k
                return LCM2

print(LCM2(30, 120))