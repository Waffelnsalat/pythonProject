# Write a Python program to count the number 4 in a given list

numbers = (input("Type in some numbers with a \",\" between (no space)"))
list = numbers.split("," or ".")
list_search_4 = 0
for num in list:
    test = int(num)
    print(test)
    if test == 4:
        list_search_4 = list_search_4 + 1
print(list_search_4)


def list_count_4(nums):
  count = 0
  for num in nums:
    if num == 4:
      count = count + 1

  return count

print(list_count_4([1, 4, 6, 7, 4]))
print(list_count_4([1, 4, 6, 4, 7, 4]))