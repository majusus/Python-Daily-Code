# Task 1 : Printing to Console
print("Hello world!")

print("This is my first task in the 100 Days of Code challenge.\nHello world!")

# Task 2 : String Interpolation
print("I am excited to learn Python and improve my coding skills.\nLet's get started with the basics!" + "\nI will be sharing my progress daily.")

# Task 3 : Using input Function
name = input("What is your name? ")
print("Hello " + name + "! Welcome to the 100 Days of Code challenge.")

# Task 4 : Using Variables
age = input("How old are you? ")
statement = "You are " + age + " years old, " + name + "! Let's make the most of this challenge together."
print(statement)
length_of_statement = len(statement)
print("The length of your statement is: " + str(length_of_statement) + " characters.")

# Task 5 : Creating a program to generate Band Name
print("Welcome to the Band Name Generator!")
city = input("What is the name of the city you grew up in?\n")
pet_name = input("What is the name of your pet?\n")
band_name = city + " " + pet_name
print("Your band name could be: " + band_name)