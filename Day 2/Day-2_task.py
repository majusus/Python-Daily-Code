#Task 1: Subscripting
print("Task_1:_Subscripting"[0:5])
print("Task_1:_Subscripting"[-1:0:-1])

#Task 2: Type
print(type("Task_2:_Type"))
print(type(123))
print(type(123.456))
print(type(True)) 

#Task 3: Type Conversion
print(int(123.456))  # Convert float to int
print(float(123))    # Convert int to float
print(str(123))      # Convert int to str

#Task 4: Mathematical Operations (PEMDASLR)
print(10 + 5)        # Addition
print(10 - 5)        # Subtraction
print(10 * 5)        # Multiplication
print(10 / 5)        # Division
print(10 % 3)        # Modulus
print(10 ** 2)       # Exponentiation
print(10 // 3)       # Floor Division
print(3 * 3 + 3 / 3 - 3)  # Parentheses for precedence
print(3 * (3 + 3) / 3 - 3)  # Parentheses for precedence

#Task 5: Number Manipulation and F strings
print(round(10.5))  # Rounding a float
print(abs(-10))     # Absolute value
print(f"Task_5:_Number_Manipulation_and_F_strings: {10 + 5}")  # Using f-string for output

#Task 6: Tip Calculator project
def tip_calculator():
    print("Welcome to the Tip Calculator!")
    total_bill = float(input("What was the total bill? $"))
    tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    split_people = int(input("How many people to split the bill? "))

    tip_amount = (tip_percentage / 100) * total_bill
    total_amount = total_bill + tip_amount
    amount_per_person = total_amount / split_people

    print(f"Each person should pay: ${amount_per_person:.2f}") #instead of .2f we can use round(amount_per_person, 2)

tip_calculator()