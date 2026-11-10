# #Area and perimeter of a circle

# diameter = float(input("Enter diameter of a circle: "))
# radius = float(input("Enter radius of a circle: ")) 

# area = 3.142 * (radius ** 2)
# perimeter = 3.142 * diameter

# print(f"Area: {area}")
# print(f"Perimeter: {perimeter}")
# print(f"Words: {len(sentence.split())}")

# sentence = input("Enter a sentence: ")
# words = sentence.split()
# print(" " .join(words))

# name = input("Enter your full name: ")
# parts = name.split()

# initials = parts[0][0].upper() + "." + parts[-1][0].upper() + "." 
# print(initials)

name = input("Enter your full name: ")
parts = name.split()

initials = ""
for parts in parts:
    initials += parts[0].upper() + "."
print(initials)
   