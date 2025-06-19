#Task 1 - Conditional Statements
print("Welcome to rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child tickets are $5.")
        bill = 5 
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    elif 45 <= age <= 55: #age >= 45 and age <= 55
        print("Age 45-55 tickets are free.")
    else:
        print("Adult tickets are $12.")
        bill = 12

    wants_photo = input("Do you want a photo taken? Y for yes or N for No: ").strip().upper()
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}.")        
else:
    print("Sorry, you have to grow taller before you can ride.")

#Task 2 - Check odd or even
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

#Task 3 - BMI Calculator
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print(f"Your BMI is {bmi:.1f}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi:.1f}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi:.1f}, you are overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi:.1f}, you are obese.")
else:
    print(f"Your BMI is {bmi:.1f}, you are clinically obese.")

#Task 4 - Pizza Delivery
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ").strip().upper()
add_pepperoni = input("Do you want pepperoni? Y for yes or N for No: ").strip().upper()
extra_cheese = input("Do you want extra cheese? Y for yes or N for No: ").strip().upper()
bill = 0
smallPizza_Price = 15
mediumPizza_Price = 20
largePizza_Price = 25
smallPizza_Pepperoni_Price = 2
medium_large_Pizza_Pepperoni_Price = 3
extra_cheese_Price = 1

if size == "S":
    bill = smallPizza_Price
    if add_pepperoni == "Y":
        bill += smallPizza_Pepperoni_Price
elif size == "M":
    bill = mediumPizza_Price
    if add_pepperoni == "Y":
        bill += medium_large_Pizza_Pepperoni_Price
elif size == "L":
    bill = largePizza_Price
    if add_pepperoni == "Y":
        bill += medium_large_Pizza_Pepperoni_Price
else:
    print("Invalid size selected. Please choose S, M, or L.")

if extra_cheese == "Y":
    bill += extra_cheese_Price

print(f"Your final bill is ${bill}.")


