#Task 1- For loop
integers = [1, 2, 3, 4, 5]
for i in integers:
    print(i)



#Task 2- Highest Score
student_scores = [85, 92, 78, 90, 88]
highest_score = max(student_scores)

loop_highest_score = 0
for score in student_scores:
    if score > loop_highest_score:
        loop_highest_score = score

print("The highest score using loop is:", loop_highest_score)
print("The highest score using max is:", highest_score)



#Task 3- For loop with range
sum_of_numbers = 0
for i in range(1, 101):
    sum_of_numbers += i
print("The sum of numbers from 1 to 100 is:", sum_of_numbers)


#Task 4- Fizzbuzz
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)



#Task 5- Password Generator Project
import random
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'

print("Welcome to the PyPassword Generator!")


nr_letters = int(input("How many letters would you like in your password? "))
nr_numbers = int(input("How many numbers would you like in your password? "))
nr_symbols = int(input("How many symbols would you like in your password? "))
password_list = []

for _letter in range(nr_letters):
    password_list.append(random.choice(letters))

for _numbers in range(nr_numbers):
    password_list.append(random.choice(numbers))

for _symbols in range(nr_symbols):
    password_list.append(random.choice(symbols))    

print("Your intitial password list is:", password_list)

random.shuffle(password_list)
password = ''.join(password_list)

print("Your generated password is:", password)
