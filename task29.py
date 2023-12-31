# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2




color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

for color1 in color_list_1:
    for color2 in color_list_2:
        if not color1 == color2:
            print(color1)

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("Original set elements:")
print(color_list_1)
print(color_list_2)
print("\nDifferenct of color_list_1 and color_list_2:")
print(color_list_1.difference(color_list_2))
print("\nDifferenct of color_list_2 and color_list_1:")
print(color_list_2.difference(color_list_1))