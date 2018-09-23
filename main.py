list_of_names = [("Maciek", 20), ("Kacper", 28), ("Ania", 56), ("Krzysztof", 67), ("Janek", 89)]
result = 0
print("Hi! This is program created by Maciek. It can tell you the age of people. Please follow the instructions:\n")
typed_name = input("what is your your name?\n")

for name in list_of_names:
    if (typed_name == name[0]):
        result = name[1]

if result == 0:
    print("Sorry, there is no your name in database!")
else:
    print("Your age is " + str(result))