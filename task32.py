# Write a Python program to get the least common multiple (LCM) of two positive integers.

def lcm(x, y):
  if x > y:
      z = x
  else:
      z = y
  while(True):
      if((z % x == 0) and (z % y == 0)):
          lcm = z
          break
      z += 1
  return lcm
print(lcm(4, 6))
print(lcm(15, 17))


def LCM2(num1, num2):
    for k in range(1, num1*num2+1, +1):
        if (k % num2 == 0) and (k % num1 == 0):
            LCM2 = k
            return LCM2


print(LCM2(4, 4))

























