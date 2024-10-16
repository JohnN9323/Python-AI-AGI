# print ("Hello world!\nWelcome!")

"# The Python Input Function"

# input ("what is your name?")
# print ("Hello "+ input("What is your full name?")+"!")

" better way to write the above code"
# print("What is your name?")
# name = input()
# print("What is your middle name?")
# print ("Hello"+" " +name+ input()+"!")


"#Python Variables"

# last_name = input ("What is your last name?")
# print(last_name)


"# print variables of different input" 

# a= input()
# b= input()

# c=a
# a=b
# b=c

# print("a:" +a)
# print("b:" +b)

"# DAY 1"

"# for comment"
"""
For multi line comments
"""
# x = 1  # int
# y = 1.0  # float
# z = 1J  # complex

# print(type(x)) #type lets you varity type of value or object that indicates the X
# print(type(y))
# print(type(z))

"length of an variable"
# print("Hello"+input("what is your name?"))

# name = input("what is your name?")
# length = len(name)
# print(length)

"""NOTE: CONCATENATION STRING"""

# 1. Create a greeting  for your program.

# print("welcome to the band name Shalom in Christ")

# 2. Ask the user for city that they grew up in.

# city = input("what is the name of the city that you grew up in?\n")

# 3. Ask the user for the name of the pet.

# pet = input("what is your pet name?\n")

# 4. Combine the name of their city and pet and show them their band name.

# print("your band name could be " + city+" "+pet)

# we can only concatenate strings not integer

# len(12345)

# num_char = len(input("what is your name?"))
# print("your name has " + num_char + "characters.")
# TypeError: can only concatenate str (not "int") to str

# here num_char is has an integer you can check it by type function

# num_char = len(input("what is your name?"))
# print(type(num_char)) # to check the data type
# new_num_char = str(num_char)# data type conversion to integer to string
# print("your name has " + new_num_char + " characters.")

# print(70 + float("100.5")) #converting string to float
# print(str(70) + str(100))

# two_digit_number = input("Type a two digit number: ")

"NOTE:USING MAP"

# numbers = [1,2,3,4]
# #using map() to square each number
# squared = map(lambda x: x**2,numbers)
# #convert the iterator to a list to see the results
# print(list(squared))

# ANS1  
# print(type(two_digit_number))
# print(sum(map(int, two_digit_number)))

# ANS2
# total =0
# for i in two_digit_number:
#  i= int(i)
#  total=total + i
#  print(total)

# ANS 3

# first = int(two_digit_number[0])
# second = int(two_digit_number[1])
# total = first + second
# print(total)
# TypeError: 'int' object is not subscriptable


"# PEMDAS or PEMDASLR (LEFT TO RIGHT)"

# Multiplication and division  and addition or subtraction are given equally important

# 1 Parentheses ( )
# 2 Exponents   **
# 3 Multiplication  *
# 4 Division  /
# 5 Addition +
# 6 Subtraction -

# print(3*3 + 3/3 -3)

"# BMI Calculator"

# BMI = Weight/ height(h)2

# height = input("enter your height in m:")
# weight = input("enter your weight in kg:")
# bmi = int(weight)/float(height)**2
# bmi_as_int = int(bmi)
# print(bmi_as_int)
# or
# print(int(bmi))

"# Number manipulation and F strings in Python"

"# to round the number 26.6666"
# print(round(bmi))

"# If the decimals are required."
# print(round(bmi,2))

"# floor division used when you don't want to convert the result into integer"
# print(8//3)
# print(type(8//3)) #int

"Storing the result in a variable and usecases"
# result = 4/2
# result /= 2
# print(result)

"# Fstrings"

# score =7
#
# print("you score is "+ str(score))

"# instead of converting data, we can use the f-string to incorporate the different data types."

"""# use "f" and curly braces "{}" """

# score = 7
# height = 1.8
# winner = True
#
# print(f"your score is {score}, your height is {height} and you are winning is {winner}")

"# challenge 2: Age calculator"

# age = input("What is your current age?")
# new_age=90-int(age)
# days= new_age * 365
# weeks = new_age * 52
# months = new_age * 12
# hours= new_age * 24*365
# print(f"you have {hours} hours, {days} days, {weeks} weeks, and {months} months left ")

"# challenge 3: Tip Calculator"

# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Round the result to 2 decimal places

# Welcome to the tip calculator

# print("Welcome to tip calculator")
#
# bill = float(input("what is the bill amount?"))
# tip = int(input("how much % of tip do you want to pay? 10,12,15\n"))
# People = int(input("how many people do you want to split the bill?"))
#
# total_tip_amount = bill * tip / 100
# tip_per_person = round(total_tip_amount / People,1)
# total_bill_amount = bill + total_tip_amount
# bill_per_person = round(total_bill_amount / People, 2)

"##instead of using round in bil_per_person we can use the below formate method"

# new_bill_per_person = "{:.2f}".format(bill_per_person)

# print(f"Each person should pay ${bill_per_person} and it includes the {tip} percentage of tips ${tip_per_person} each.")


"# Conditional statements, Logical Operators, Code Blocks and Scope"

"# control a flow with if/ else Conditional Operators"

# print("welcome to the roller coaster!")
#
# height = (int(input("what is your height?")))
# if height >= 120:
#     print("you can ride the roller coaster!")
# else: print ("damn you short lol")
#
# age = (int(input("how old are you?")))
# if 12 <= age <= 18:
#     print("your ticket cost $7!")
#
# elif age < 12:
#     print("your ticket cost $5!")
#
# elif age > 18:
#     print("your ticket cost $12!")
#
# else:
#     print("Sorry, you can't ride the rollercoaster for now")

"# comparison operators"

# > Greater than
# < lesser than
# >= Greater than or equal to
# <= lesser than or equal to
# == equal to
# != not equal to

# remember that while you are using "=" one equal sign you are assigning the values to variables

# The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.

# math=5%2
# print(math)

# number = int(input("Which number do you want to check? "))
#
# if number % 2 ==0:
#     or
# new_number = number % 2
# if new_number == 0:
#  print("this is an even number")
#
# else:
#     print("THis is an odd number")

"# Nested if statements and elif statements"

"# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height."

# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
#
# # BMI = round(weight/height**2)
# # or
# BMI = float("{:.2f}".format(weight/height**2))

# if BMI < 18.5:
#     print(f"your BMI is {BMI}, you are underweight")

# elif BMI < 25:
#     print(f"your BMI is {BMI}, you are normal weight")

# elif BMI < 30:
#     print(f"your BMI is {BMI}, you are slightly overweight")

# elif BMI < 35:
#     print(f"your BMI is {BMI}, you are obese")

# else:
#     print(f"your BMI is {BMI}, you are clinically obese")

"# Leap year calculator"

# leap year rules
# 1 add an extra day every 4 years
# 2 Skip it if it's a new century
# 3 Unless the century is divisible by 400

# print("welcome to leap year calculator!")
#
# year = int(input("enter the year"))
#
# # if year / 4 == 0 and year/ 100 > 0 or year/100 == 0 and year/400 ==0:
# #     print("leap year")
# #         or
# if year /4 ==0 and year/100 > 0:
#     print("leap year")
#
# elif year/4 == 0 and year/100 == 0 and year/400 == 0:
#     print("leap year")
# else:
#     print("not leap year")

"# Multiple if statements in Succession"

# print("welcome to the roller coaster ride")
#
# height = int(input("Enter your height in cm"))
# age = int(input("Enter your age"))

# if height > 120:
#     print("you can ride the roller coaster")
#     bill=0
#     if age <12:
#         bill=5
#         print("child tickets are $5")
#     elif age <=18:
#         bill=7
#         print("young tickets are $7")
#     elif age >= 45 and age<=55:
#         print("Everything is going to be ok. Have a free ride on us!")
#     else:
#         bill=12
#         print("Adult tickets are $12")
#
#     photo = input("We charge extra $3 for pictures of you are roller coaster ride? please enter  Y = Yes or N= No\n")
#     if photo =="Y":
#         bill+=3
#
#     print(f"your final bill is ${bill}")
#
# else:
#     print("sorry, you are not eligible")

"# Pizza order partice"

# print("welcome to Pizza Party")
#
# size = input("What size pizza do you want? S, M, or L\n")
# add_pepperoni = input("Do you want pepperoni? Y or N\n")
# extra_cheese = input("Do you want extra cheese? Y or N\n")
#
#
# bill =0
#
# if size == "S":
#     bill+= 15
# elif size == "M":
#     bill+=20
# else:
#     bill+=25
#
#
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your total bill is ${bill}")

"#Logical operators"

#multiple condition in the same line of code

# and, or ,not

#"not" to reverse the condition

#-----------------------------------

"#love score calculator"

#To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. '
# Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:
#
# "Your score is **x**, you go together like coke and mentos."
#
# For Love Scores between 40 and 50, the message should be:
#
# "Your score is **y**, you are alright together."
#
# Otherwise, the message will just be their score. e.g.:
#
# "Your score is **z**."

# print("Welcome to love calculator")
# name1 = input("what is your name?\n")
# name2 = input("what is their name?\n")
#
# combine_names = name1 + name2 .lower()
#
# T = combine_names.count("t")
# R = combine_names.count("r")
# U = combine_names.count("u")
# E = combine_names.count("e")
#
# true = T + R + U + E
#
# L = combine_names.count("l")
# O = combine_names.count("o")
# V = combine_names.count("v")
# E = combine_names.count("e")
#
# love = L + O + V + E
#
# love_score = int(str(true) + str(love))
#
# if (love_score < 10) or (love_score >= 90):
#     print(f"Your score is {love_score}, You go together like coke and mentos. ")
# elif (love_score >= 40) and (love_score <= 50):
#     print(f"Your score is{love_score}, You go alright together.")
# else:
#     print(f"Your score is {love_score}")

"#project treasure island"

# 'You're at a crossroad. Where do you want to go? Type "left" or "right"'
# 'You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
# "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
# "It's a room full of fire. Game Over."
# "You found the treasure! You Win!"
# "You enter a room of beasts. Game Over."
# "You chose a door that doesn't exist. Game Over."
# "You get attacked by an angry trout. Game Over."
# "You fell into a hole. Game Over."


# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
#
#
# choice1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()
# if choice1 == "left":
#     choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
#     if choice2 == "wait":
#         choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
#         if choice3 == "red":
#             print("It\'s a room full of fire. Game Over.")
#         elif choice3 == "yellow":
#             print("You found the treasure! You Win!")
#         elif choice3 == "blue":
#             print("You enter a room of beasts. Game Over.")
#         else:
#             print("You chose a door that doesn't exist. Game Over.")
#     else:
#         print("You get attacked by an angry trout. Game Over.")
# else:
#     print("You fell into a hole. Game Over.")


"#Ramdomisation and Python lists"

# import random
#
"random integer generating"
# random_integer = random.randint(1, 10)
# print(random_integer)
#
"random float integer generating"
# random_float = random.random() # Returns the next random floating point number between [0.0 to 1.0)
# print(random_float)

"what if you can multiply the random_float by a number"
# randomFloat = random.random()*5
# print(randomFloat)

" what if I want random_float from 1to5?"
#
# random_float_any = random.uniform(1,5)
# print(random_float_any)
#
# import random

# print('Random number from 0 to 1 :', random.random())
# print('Uniform Distribution between [1,5] :', random.uniform(1, 5))
# print('Gaussian Distribution with mean = 0 and standard deviation = 1 :', random.gauss(0, 1))
# print('Exponential Distribution with lambda = 0.1 :', random.expovariate(0.1))
# print('Normal Distribution with mean = 1 and standard deviation = 2:', random.normalvariate(1, 5))

"Heads or Tails coin flipping using randomization"

# import random

# random_side = random.randint(0,1)
# if random_side == 1:
#     print("Head")
# else:
#     print("Tails")


"""understanding the Offset and Appending items to "List" """

# states_of_India = ["Andhra Pradesh", "Andaman & Nicobar Islands", "Arunachal Pradesh", "assam", "Bihar"]
# print(states_of_India[1])


" to change the existing data in the list"

# states_of_India[3] = "Assam"
# print(states_of_India)

"""to add the states to the list "append" function"""

# states_of_India.append("Karnataka")
# print(states_of_India)


# >>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# >>> fruits.count('apple')
# 2
# >>> fruits.count('tangerine')
# 0
# >>> fruits.index('banana')
# 3
# >>> fruits.index('banana', 4)  # Find next banana starting a position 4
# 6
# >>> fruits.reverse()
# >>> fruits
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
# >>> fruits.append('grape')
# >>> fruits
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
# >>> fruits.sort()
# >>> fruits
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
# >>> fruits.pop()
# 'pear'


" Using list and randomization to pay the bill"

#nameList = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

# nameList = input("Give me everybody's names, separated by a comma.")
# names = nameList.split(",") # split will separate the components to list "[]"
# # print(names)

# import random
# lunch = random.randint(0,(len(names) -1)) # Len function to get the total numbers of items in the list.
# print(f"{names[lunch]} is going to buy the meal today!")



# print(f"{names= random.uniform[]} is going to buy the meal today!")

# print("{names.uniform}")

# print("{"nameList.split(",") = random.uniform[nameList]})

#print (nameList.split(",") randon.uniform[namelist])


"#IndexError"

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]
#
# print(dirty_dozen[1][1])
# print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])

"# QN1 Mark the treasure"

# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? \n")

# horizonal = int(position[0])
# vertical = int(position[1])

# map[vertical -1][horizonal-1] = "x"
# #           or
# # selected_row = map[vertical-1]
# # selected_row[horizonal-1] = "x"

# print(f"{row1}\n{row2}\n{row3}")

# or

# letter = position[0].lower()
# abc=["a","b","c"]
# letter_index = abc.index(letter)
# number_index = int(position[1])-1
# map[number_index][letter_index]="x"

# print(f"{row1}\n{row2}\n{row3}")

"ROCK,PAPER,SCISSOR GAME"

# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# game_images = [rock, paper, scissors]

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# print(game_images[user_choice])

# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])

# if user_choice >=3 or user_choice < 0:
#   print("You typed an invalid number, you lose!")
# elif user_choice == 0 and computer_choice == 2:
#   print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#   print("You lose")
# elif computer_choice > user_choice:
#   print("You lose")
# elif user_choice > computer_choice:
#   print("You win!")
# elif computer_choice == user_choice:
#   print("It's a draw")


"Day 5" "Python Loops"

"Created a Password Generator"

"using the for loop with Python Lists"

# fruits = ["Apple","Peach","Pear"]
# for fruit in fruits:
#     print(fruit)

"Calculation Average Height of the students"

# # converting input to list
# print("enter the students height separated by space")
# student_heights = input().split()
# print(student_heights)
# for n in range(0, len(student_heights)):  
#     student_heights[n] = int(student_heights[n])
# print(student_heights)

# # using the about converted student list we have to find the average
# #need to find total height, no_of_students and average height

# # total height
# total_height = 0
# for height in student_heights:
#     total_height += height  
# print(f"total height = {total_height}")

# number_of_students = 0
# for student in student_heights:
#     number_of_students +=1
# print(f"number of students = {number_of_students}")

# average_height = round(total_height /number_of_students)
# print(f"average height = {average_height}")

"fetch the highest score of a student"

# # Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])

# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score in the class is:{highest_score}")


"looping using RANGE function"

# for number in range(a, b):
#     print(number)

# for number in range (1, 10):
#     print(number)

# step by in a range

# for num in range(1,11,3):
#     print(num)

"#sum of 100"
# total=0
# for num in range(1,101):
#     total += num
# print(total)

"# adding even numbers using range loop"

# target = int(input())

# even_sum =0
# for number in range(2, target+1, 2):
#     even_sum += number
# print(even_sum)

"# alternative sum"

# alternative_sum =0
# for number in range(1, target+1):
#    if number %2 ==0:
#        alternative_sum +=number
# print(alternative_sum)


"""FIZZ  BUZZ
FIZZ % 3 AND BUZZ %5 
IF % BY BOTH 3 AND 5 IS FIZZ BUZZ"""

# target =int(input())
# for number in range(1, target+1 ):
#     if number % 3 ==0 and number%5 ==0:
#         print("FIZZBUZZ")
#     elif number % 3 == 0:
#         print("FIZZ")
#     elif number % 5 == 0:
#         print("BUZZ")
#     else:
#         print(number)

"Password Generator"

# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to password Generator")
# no_of_letters = int(input("How many letters would you like in your password?\n")) 
# no_of_symbols = int(input(f"How many symbols would you like?\n"))
# no_of_numbers = int(input(f"How many numbers would you like?\n"))

#EAZY

# password = ""

# for char in range(1, no_of_letters+1):
#     password += random.choice(letters)
#     print(password)

# for char in range(1, no_of_symbols+1):
#     password += random.choice(symbols)
#     print(password)

# for char in range(1, no_of_numbers+1):
#     password += random.choice(numbers)
#     print(password)

# print(f"Your new password:{password}")

#HARD ".append" used insted of "+=" in list we use append function for string we use "+="

# password_list = []

# for char in range(1, no_of_letters+1):
#     password_list.append(random.choice(letters))
#    # print (password_list)
    
# for char in range(1, no_of_symbols+1):
#     password_list.append(random.choice(symbols))
#     # print (password_list)

# for char in range(1, no_of_numbers+1):
#     password_list.append(random.choice(numbers))
#     # print (password_list)

# print (password_list)
# random.shuffle(password_list)
# print (password_list)

# password =" "
# for char in password_list:
#     password += char
# print(f"Your new password:{password}")

"for shuffle either you can use for loop or random.shuffle ()"
# mylist =['a','b','c','d','e']
# myorder= [3,2,0,1,4]
# mylist = [mylist[i] for i in myorder]
# print(mylist)

"ANAGRAM SHUFFLING"

"""To shuffle a string without converting it to a list, using only a for loop, 
we can use a technique that builds a new string character by character. Here's how you can do it:"""

# import random

# string = "STOP"
# shuffled = ""
# remaining = string

# for _ in range(len(string)):
#     # Choose a random index from the remaining string
#     index = random.randint(0, len(remaining) - 1)
#     # Add the character at that index to the shuffled string
#     shuffled += remaining[index]
#     # Remove the chosen character from the remaining string
#     remaining = remaining[:index] + remaining[index+1:]

# print(shuffled)

""" list of anagram shuffling and choosing a word from the list and match it with the existing anagram in the list"""

# import random

# anagrams = ['STOP', 'POTS', 'TOPS', 'OPTS']

# # Print original list
# print("Original list:", anagrams)

# # Shuffle the list
# random.shuffle(anagrams)

# # Print shuffled list
# print("Shuffled list:", anagrams)

# # Pick a random word from the list
# chosen_word = random.choice(anagrams)

# print("\nChosen word:", chosen_word)
# print("Now, let's shuffle its letters:")

# # Convert the word to a list of characters, shuffle, and join back
# shuffled_word = list(chosen_word)
# random.shuffle(shuffled_word)
# shuffled_word = ''.join(shuffled_word)

# print("Shuffled letters:", shuffled_word)

# # Check if the shuffled letters form another word in the list
# if shuffled_word in anagrams:
#     print(f"The shuffled letters form another valid word: {shuffled_word}")
# else:
#     print("The shuffled letters don't form another word in our list. Try again!")

"shuffling the string without using random.suffle but converting to list and using function"

# import random

# def shuffle_string(string):
#     char_list = list(string)
#     n= len(char_list)

#     for i in range(n-1, 0, -1):
#         j = random.randint(0, i)
#         char_list[i],char_list[j]= char_list[j], char_list[i]
#     return ''.join(char_list)

# text = "hello world"
# shuffled_text = shuffle_string(text)
# print(shuffled_text)


" Day 6" "Code Blocks, Functions, While Loops"

# https://docs.python.org/3/library/functions.html

# def : defining a function
# def my_function ():

"Indentation in functions"

# sky = ""
# def my_function():
#     if sky == "clear":
#         print("blue")
#     elif sky == "cloudy":
#         print("grey")
#     else:
#         print("hello")
# print("world")

""" FOR LOOP

for item in list_of_items:
    #Do something to each item

for number in range(a, b):
    print(number)

"""

"""WHILE LOOP

while somethin_is_true:
    #Do something repeatedly

"""


# while at_goal != True:
#     jump()

# or

# while not at_goal():
#     jump()


""" when to use for loop and while loop
if you want to itterate through each item use for loop
use while loop only if you don't care about the range or you don't want to go through all items
it if it meets functionalites or condition you set """

"Day 7:  HANGMAN PROJECT"

"""""
PYTHON RANDOM MODULE METHODS
https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

seed()
getstate()
setstate(state_obj)
getrandbits(k)

GENERATE RANDOM INTEGERS

randrange(start, stop, step)
randint(a,b) a<b

GENERATING RANDOM FLOATING POINT NUMBERS

random.random()
random.uniform(a,b)
random.expovariate(lambda)
random.gauss(mu, sigma)

RANDOM SEQUENCES USING THE RANDOM MODULE

random.shuffle(x)
random.choice(seq)
random.sample(population, k)
random.seed()

"""
# step 1
"pick a random words from the list and match the user input letter with chosen word"

# import random

# word_list = ["ardvark","baboon","camel"]

# chosen_word = random.choice(word_list)

# print(chosen_word)


# user_guess = input("guess a letter:").lower()

# for letter in chosen_word:
#     if letter == user_guess:
#         print("right")
#     else:
#         print("wrong")

# step 2
""""# map the chosen word to the display list and print ["_"] and loop through each position if matches the guess print those letters """


# import random

# word_list = ["ardvark","baboon","camel"]

# chosen_word = random.choice(word_list)

# print(chosen_word)

# display = []

# for letter in chosen_word:
#     display += "_"
# print(display)

# or

# for _ in range(len(chosen_word)):
#     display += "_"
# print(display)

# user_guess = input("guess a letter:").lower()

# for position in range(len(chosen_word)):
#     letter = chosen_word[position]
#     if letter == user_guess:
#         display[position] = letter
    
# print(display)

# step3
"write code to repeateadly asking user guess all the letters in the display and display should not be empty"

# end_of_game = False
# while not end_of_game:
#     user_guess = input("guess a letter:").lower()

#     for position in range(len(chosen_word)):
#         letter = chosen_word[position]
#         if letter == user_guess:
#             display[position] = letter
        
#     print(display)
    
#     if "_" not in display:
#         end_of_game = True
#         print("You Won!")


# step4

"completing the game of the hangman using ASCII ART and map the stages list with wrong letter gussed by user and if the guess is wrong reduce it by 1"

# import random
# from turtle import clear

# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']

# logo = ''' 
#  _                                             
# | |                                            
# | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
# | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
# | | | | (_| | | | | (_| | | | | | | (_| | | | |
# |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                     __/ |                      
#                    |___/    '''

# print(logo)

# word_list = ["ardvark","baboon","camel"]

# chosen_word = random.choice(word_list)

# print(chosen_word)

# lives = 6


# display = []

# for _ in range(len(chosen_word)):
#     display += "_"
# print(display)

# end_of_game = False
# while not end_of_game:
#     user_guess = input("guess a letter:").lower()

#     clear()

#     if user_guess in display:
#          print(f"you've already guessed {user_guess}")

#     for position in range(len(chosen_word)):
#         letter = chosen_word[position]
#         if letter == user_guess:
#             display[position] = letter
    
#     if user_guess not in chosen_word:
          
#         print(f"You guessed {user_guess},that's not in the word. You loose a life.")
#         lives -=1
#         if lives == 0:
#             end_of_game = True
#             print("you lose!")
#     # print(display)  
#     # this will convert the list to string
#     print(f"{'  '.join(display)}")
    
    
#     if "_" not in display:
#         end_of_game = True
#         print("You Won!")
#     print(stages[lives])     

"import file "

# import hangman_word  
# chosen_word = random.choice(hangaman_word.word_list)
# # or
# from hangman_word import word_list
# chosen_word = random.choice(word_list)


"Day 8 : Beginner Function with inputs arguments and parameter"


# Function and calling it 
# def greet():
#     print("hello John!")
# greet()

# Function with input values

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
# greet_with_name("Angela")

# Function with more than 1 inputs

# def greet(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
# greet("John","Bangalore")


# position Arguments
# here the arguments should match a=1, b=2, and c=3 but the input has not matched
# def function(a,b,c):
#     print(a,b,c)

# function(1,3,2)

#Keyword Arguments
# to match the argment we use key word in input

# def my_function(a,b,c):
#     print(a,b,c)

# my_function(c=3,a=1,b=2,)

"PAINT CALCULATOR"
"1 can of pain can cover 5 square meters"
"no of can required = wall height * wall width % coverage per can"

# import math

# h = int(input())
# w = int(input())
# c = 5
# def paint_calc(height, width, coverage):
    
#     no_of_cans_required = (height*width) / coverage

#     print(f"you'll need {math.ceil(no_of_cans_required)} cans of paint")
    
# paint_calc(height=h,width=w,coverage =c)

"CEASER CIPHER"

# import os

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def clear():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def data_checker():
#     while True:
#         direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#         if direction in ['encode', 'decode']:
#           break
#         print("Invalid input! Please enter 'encode' or 'decode'.")
#         clear()

#     while True:
#         text = input("Type your message:\n").lower()

#  # this will handle the inputs like numeric,  empty and space in text
#         if not text.isnumeric() and text != "":     
#            break
#         else:
#          print("Invalid! please enter the alphabetic letters only")
#         clear()
    
#     #try and expect is used
#     while True: 
#         try:
#             shift = int(input("Type the shift number:\n"))
#             break
#         except ValueError:
#             print("Invalid input! Please enter a number.")
#         clear()

#     return direction, text, shift


"# method 1"
"# shift is limited based on the aphabetic index"

# def cipher_text(directions, plain_text, shift_amount):
#     result=""
#     for letter in plain_text:
#         if letter in alphabet:
#             position = alphabet.index(letter)
#             if direction =="encode":
#                 new_position = position + shift_amount
#             elif direction == "decode":  
#                 new_position = position - shift_amount 
#             new_letter = alphabet[new_position]
#             result+=new_letter
#         else:
#             result+= letter

#     print(f"The {'encoded' if direction == 'encode' else 'decoded'} text is {result}")    
            
# direction,text,shift = data_checker()               
# cipher_text(directions=direction, plain_text = text, shift_amount=shift)



"# method 2"
"# below code for exceptional haldler if shift > aphabetic indices or any number of shifts it will hadle and use of main "

# def caesar_cipher(text, shift, direction):
#     result = ""
#     for char in text:
#         if char in alphabet:
#             index = alphabet.index(char)
#             if direction == 'encode':
#                 new_index = (index + shift) % 26
#             else:  # decode
#                 new_index = (index - shift) % 26
#             result += alphabet[new_index]
#         else:
#             result += char
#     return result
    

# def main():
#     direction, text, shift = data_checker()
#     result = caesar_cipher(text, shift, direction)
#     print(f"The {'encoded' if direction == 'encode' else 'decoded'} text is: {result}")

# if __name__ == "__main__":
#     main()

"# to see the breakdown of the shift you can use this main () "

# def main():
#     direction, text, shift = data_checker()
#     result = caesar_cipher(text, shift, direction)
#     print(f"The {'encoded' if direction == 'encode' else 'decoded'} text is: {result}")
#     print("\nShift breakdown:")
#     for char, res_char in zip(text, result):
#         if char in alphabet:
#             print(f"'{char}' -> '{res_char}' (shift: {alphabet.index(res_char) - alphabet.index(char) if direction == 'encode' else alphabet.index(char) - alphabet.index(res_char)})")
#         else:
#             print(f"'{char}' -> '{res_char}' (unchanged)")

# if __name__ == "__main__":
#     main()

"""# to check with user if they want to run this progam again if "yes" to confirm and "no" then good bye"""

# def main():
#     should_continue = True
#     while should_continue:
#         direction, text, shift = data_checker()
#         result =caesar_cipher(text, shift, direction)
#         print(f"The {'encoded' if direction == 'encode' else 'decoded'} text is: {result}")
        
#         user = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
#         if user == "no":
#             should_continue = False
#             print("Goodbye")

# if __name__ == "__main__":
#     main()

"# day 9:  DICTIONARIES AND NESTING"

# # mentioning the multiple items in a dictionary
# programming_dictionary = {
#     "Bug": "An error in a programm that prevents the programm from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "loop": "The action of doing something over and over again.",
#     123:"Hello John "
# }

# # retriving an item from the dictionary
# # items in the dictonary are identify by their keys
# # fetching an item from the dictionary a common mistake is spelling the key name icorrectly
# # always provide the key data type here the data type is string  

# print (programming_dictionary["Bug"])
# print (programming_dictionary[123])

# # adding the items to dictionary later on

# programming_dictionary["Function1"] ="function1 for backtracking"
# # now the dictionary will have four items including the function1
# print(programming_dictionary)

# # editing an item in the dictionary

# programming_dictionary["Function1"]="A moth in your computer."

# print(programming_dictionary)

# # creating empty dictionary

# empty_dictionary ={}

# # later you can add the items to dictionary using this method

# empty_dictionary ["Function","Loop","Bug"] = "function","loop","bug"

# # wipe an exsisting dictonary

# empty = {}

# programming_dictionary = {}

# print(programming_dictionary)

# programming_dictionary = empty_dictionary

# print(programming_dictionary)

# # How you loop through dictionary

# # below code will not print the content of the items it prints only keys
# for key in programming_dictionary:
#     # keys based on this line
#     print(key)
#     # values base on this line
#     print(programming_dictionary[key])


"Nesting Lists and Dictionaries"

# capitals = {
#     "France":"Paris",
#     "India": "Delhi",
#     "Germany": "Berlin"
# }

# # Nested list in the dictionaries

# # with listing and nesting for each key has assigned with more than one values
# travel_log = {
    
#     "country": ["France","India","Germany"],
#     "city":["Paris","Delhi","Berlin"],
# }

# # print India from country
# print(travel_log ["country"][1])

# # looping through keys one by one
# for key in travel_log:
#     for value in travel_log[key]:
#      print(f"{key}:{value}")

# # printing list from the inside list

# list = ["A","B",["C","D"]]

# print(list[2][1])

# Nesting dictionary with in a  dictionary itself

# travel_log = {
#     "France":{
#         "cities_visited":["Paris","Lille","Dijon"],
#         "total_visits": 10
#     },
#     "Germany":{
#         "cities_visited": ["Hamburg","Berlin","sturtgart"],
#         "total_visits": 5
#     },
# }

# # printing all the info in the germany
# print(travel_log["Germany"])

# # looping through all the countries and cities visited in the country
# for country in travel_log:
#   print("Country_visited:",country)
#   print ("cities_visited:")
#   for city in travel_log[country]["cities_visited"]:
#     print(city)

# print the first city visited in the country

# print("First city visited in France:", travel_log["France"]["cities_visited"][0])
# print("Total visits:", travel_log["France"]["total_visits"])

# # Using function

# def print_country_info(country):
#   if country in travel_log:
#     print(f"Country:{country}")
#     print(f"Cities visited:")
#     for city in travel_log[country]["cities_visited"]:
#       print("-",city)
#     print("Total visits:", travel_log[country]["total_visits"])
#   else:
#     print(f"No data available for {country}")

# print_country_info("Germany")


"Auction Progamming instruction"

# import os

# def clear():
#   os.system('cls' if os.name == 'nt' else 'clear')

# print("Hello Bidder, welcome to AuctionHub!")

# def find_highest_bidder(bidding_dictionary):
#     # if the data in the dictionary is in this formate key:value
#     # hold of highest bid amount

#     highest_bid=0
#     winner=""
#     for bidder in bidding_dictionary:
#         bid_amount= bidding_dictionary[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"The winner is {winner} with a bid of ${highest_bid}")

# bids={}  #if the bids dictionary inside the loop we loose the previous data we need the previous data for comparision
# continue_bidding = True
# while continue_bidding:
#     name= input("what is your name?:")
#     price=int(input("what is your bid?: $"))
#     bids[name]=price
#     should_continue=input("are they any other bidders? Type 'yes' or 'no' \n").lower()
    
#     if should_continue =="yes":
#        clear() 
#     #  you can use here clear() or use this simple code "print("\n"*20)"
    
#     elif should_continue =="no":
#          continue_bidding = False
#          find_highest_bidder(bids)




"using max function in python"
# # simply we can use max function in python to find the max of bid in the dictionary

# stats = {"a":11, "b":30, "c": 25}

# inverse = [(value,key) for key,value in stats.items()]
# print(max(inverse))

# print(max(stats, key=stats.get))


"Day 10 : FUNCTIONS WITH INPUTS"

"TITLE FUNCTION"

"Either input in lower case or upper case and output will change into tilte case "
"john, JOHN, JoHn all these going to end up like this John"

# def format_name(first_name,last_name):
 
#     formatted_first = first_name.title()
#     formatted_last = last_name.title()
#     return f"{formatted_first} {formatted_last}"

# # Get input from user
# first_name = input('Enter your first name:')
# last_name = input('Enter your last name:')

# # call the function

# formatted_name = format_name(first_name,last_name)
# print("Title Cased Name:", formatted_name)

"taking two function and using first function output as second finction input"

# def function_1(text):
#     return text + text

# def function_2(text):
#     return text.title()

# output = function_2(function_1("hello"))
# print(output)

"More than one return fuction in the same statement"

# def format_name(first_name,last_name):
    
#     if first_name =="" or last_name=="":
#         return "you didn't provide valid input"
    
#     formatted_first = first_name.title()
#     formatted_last = last_name.title()
#     return f"{formatted_first} {formatted_last}"

# print(format_name(input("What is your first_name?"),input("what is your last_name?")))

"DOCSTRINGS"
"""This is Docstring"""

"how to use the reference function example"

# def add(n1,n2):
#     return n1+n2

# my_favourite_operation = add

# print(my_favourite_operation(n1 = 2,n2=5))

 
"CALCULATOR"

# # Creat functions for each operations
# def add(n1,n2):
#     return n1+n2
    
# def subtraction(n1,n2):
#     return n1-n2

# def multiplication(n1,n2):
#     return n1*n2

# def division(n1,n2):
#     return n1/n2

# # store the function in dictionary

# operations ={
#     "+":add,
#     "-":subtraction,
#     "*":multiplication,
#     "/":division,
# }
# # use dictionary to performe operations

# # print(operations["*"](4,8))

# # using recurission to continue if they user choice is 'n' 
# def calculator():
#     num1 = float(input("what is your first number?:"))
#     should_accumlate = True
#     while should_accumlate:

#         for symbol in operations:
#             print(symbol)
#         operations_symbol = input("pick an operation:")

#         num2 = float(input("what is your second number?:"))
#         answer =operations[operations_symbol](num1,num2)
#         print(f"{num1} {operations_symbol} {num2} = {answer}")

#         choice = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calulation:")

#         if choice =="y":
#             num1 = answer
#         elif choice == "n":
#             should_accumlate = False
#             print("\n"*20)
#         # here you can use indent while loop inside another while loop for you can use recurrssion 
#             calculator()

# calculator()

"Blackjack Program/21"  

# """Built in function in PYTHON:
# https://docs.python.org/3/library/functions.html#sum """

# import random

# def deal_card():
#     """Return the random card form the deck"""
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card= random.choice(cards)
#     return card

# """use emoji use shortcut keys: windows + .  mac: ctrl + command +spacebar"""

# def compare(u_score, c_score):
#     if u_score == c_score:
#         return "Draw 😊"   
#     elif c_score ==0:
#         return " Lose, opponent has Blackjack 😱"
#     elif u_score == 0:
#         return "win with a Blackjack 😎"
#     elif u_score >21:
#         return "you went over. You lose🫡"
#     elif c_score>21:
#         return "Opponent went over. You win 😁"
#     elif u_score > c_score:
#         return "You win 😀"
#     else:
#         return "you loose😭"

# def play_game():
#     user_cards=[]
#     computer_cards=[]
#     computer_score =-1
#     user_score=-1
#     is_game_over = False


#     """ LIST METHOD:Here are some common list methonds:
#     https://developers.google.com/edu/python/lists#list-methods """ 

#     def calculate_score(cards):

#         if sum(cards) == 21 and len(cards)==2:
#             return 0
        
#         if 11 in cards and sum(cards)>21:
#             cards.remove(11)
#             cards.append(1)

#         return sum(cards)

#     for _ in range(2): 
#         """ this will make the loop run twice """
#         new_card = deal_card()

#         """when to use .append(0) only if you don't extent the exsisting list or "+=" 
#         user_card.extend  or "+=" will through Trackback error you can't assign a single item to a list  if you use 

#         if you want to use .extend or "+=" this will not pop an error

#         new_card = [deal_card(),deal_card1()]
#         user_cards.extend(new_card)
#         """ 
#         user_cards.append(new_card)   
#         """ or you can use directly : user_cards.append(deal_car()) """
#         computer_cards.append(deal_card())


#     """loop it till the game is over"""
#     while not is_game_over:

#         """call the funciton and assign to some variable"""
#         user_score = calculate_score(user_cards)
#         computer_score = calculate_score(computer_cards)
#         print(f"Your cards:{user_cards},current score:{user_score}")
#         print(f"computer first card:{computer_cards[0]}")
        

#         if user_score == 0 or computer_score == 0 or user_score >21:
#             is_game_over = True 

#         else:
#             user_should_deal = input("Type 'y' to get another card, type 'n' to pass:")
            
#             if user_should_deal =="y":
#                 user_cards.append(deal_card())
#                 user_score = calculate_score(user_cards)
#             else:
#                 is_game_over = True

#     """if you use the below while loop you have define a empty variable 'computer_score= -1' outside the first wile loop"""
#     while computer_score !=0 and computer_score <17:
#         computer_cards.append(deal_card())
#         computer_score = calculate_score(computer_cards)


#     print(f"Your final hand:{user_cards},final score:{user_score}")
#     print(f"Computer final hand:{computer_cards},final score:{computer_score}")
#     print(compare(u_score =user_score, c_score = computer_score))


# """to ask the use to keep on playing a game of Blackjack in the beginning"""

# while input("Do you want to play a game of Balckjack? Type 'y' or 'n':") == "y":
#     print("\n"*20)
#     play_game()


"Namespaces and Scope : Local vs. Global Scope"

# """Global variable"""
# player_name = "John"
# player_num = 7

# def game():

#     def games_won():
#         """Local variable"""
#         games = 2  
#         """Declare that we are using the global variable"""
#         global player_num , player_name
#         # player_last_name = "Logan"
#         player_name += " Logan"
#         player_num +=12 
#         print(f"{games} games won by{player_name} has jersey no:{player_num}")
#     games_won()

# game()

# print(player_num, player_name)

# """Correct way to write the above code"""

"""Important notes:
Using global variables like this is generally discouraged in Python, as it can make code harder to understand and maintain.
A better practice would be to pass player_num as an argument to game() and return the modified value.
If you're working with immutable types like strings, you can't modify them in-place. You would need to reassign the variable,
 like player_num = player_num + "suffix".
"""
# def game(player_num):
#     def games_won(num):
#         games = 2   
#         num += 7
#         print(f"{games} games won by {num}")
#         return num
#     return games_won(player_num)

# player_num = 7
# player_num = game(player_num)
# print(player_num)

"""DOES PYTHON HAVE BLOCK SCOPE"""

"""Python is bit different from other programming languages in that it does not have block scope
   This means that variables created nested in other blocks of code e.g. for loops, if statements, while loops etc.
   don't get local scope. They are given function scope if they are within a function or global scope if they are not."""


# game_level = 10
# players = ["John", "Logan", "Luke"]

# def find_best_player():
#     """you need to call the best_player as empty before assigning its value """
#     best_player = ""
#     if game_level < 5:
#         best_player = players[0] 
    
#     print(best_player)

# find_best_player()


"HOW TO MODIFY VARIABLES WITH GLOBAL SCOPE"

"""Never modify the global varible within function or name the global variable and local variable with identical names"""

"""example for using global variable"""

# name = "John"
# def name_correction():
#     global name
#     name = "John Logan"
# name_correction()  
# print(name)

"""what if you want a function that changes the name without calling global 
   you can do that using return"""
# name = "John"
# def name_correction(full_name):
#     return full_name + " "+ "Logan" 
# name = name_correction(name)  
# print(name)


"""Python Constants and Global Scope"""

"""Global Constants: you will define in all caps and never planning to modify them"""
# PI =3.14
# def my_func():
#     print(PI)
# my_func()


"""The Number Guessing Game"""

# from random import randint

# # global variable for turns
# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5

# Function to check users' guess against actual answer
# Track the number of turns and reduce by 1 if they get it wrong
"""how can you reduce the turn without creating and  passing the global variable in the functionality and modify it you can
   passing the turn to function"""

# def check_answer(user_guess,actual_answer,turns):
#     if user_guess > actual_answer:
#         print( "Too high.")
#         return turns -1
#     elif user_guess < actual_answer:
#         print("Too Low.")
#         return turns -1
#     else:
#         print(f"You got it! The answer was {actual_answer}")

# # Function to set difficulty
# def set_difficulty():
#     level =input("Choose a dificulty. Type 'easy' or 'hard':")
#     if level == "easy":
#     #     global turns
#     #     turns = EASY_LEVEL_TURNS
#     # else:
#     #     turns = HARD_LEVEL_TURNS
#     # or
      
#         return EASY_LEVEL_TURNS
#     else:
#         return HARD_LEVEL_TURNS

# def game():
#     # choosing a random number between 1 to 100
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 to 100.")
#     answer = randint(1,100)
#     print(answer)

#     # turns = 0
#     turns = set_difficulty()
#     print(f"You have {turns} attempts remaning to guess the number.")

#     # Repeat the guessing functionality if they get it wrong
#     guess=0
#     while guess != answer:
#         # Let the user guess a number
#         guess = int(input("Make a guess:"))

#         # call the function check answer
#         turns =check_answer(guess, answer,turns)
#         print(f"turns remaning:{turns}")
        
#         #to stop the truns loop to negative
#         if turns == 0:
#             print("You've run out of guess, you lose.")
#             return
#         """still you are not able to stop the game even if the turn = 0 
#         he solution here is we have our game in a funciton you can just use return to stop the game"""

# game()

"DEBUGGING: How to find and fix errors in your code"

# def my_function():
#     for i in range(1,20+1):
#         if i ==20:
#             print("you got it")

# my_function()

"Reproduce the bug"

"List index out of the bound"

# from random import randint

# dice_images = ["😭","😀","😁","😍","😎","🫡"]
# dice_num = randint(0,5)
# print(dice_images[dice_num])

"use TRY AND EXCEPT BLOCK for 'value error'"

# import os

# def clear():
#    os.system('cls' if os.name == 'nt' else 'clear')

# ask_age = True
# while ask_age:

#     try:
#        age =int(input("How old are your?"))
#        if age>18:
#           print(f"You can drive at age{age}")
#           ask_age = False
#        else:
#           print(f"You are not old enough to drive at age {age}")
#           ask_age = False
#     except ValueError:
#        print("Invalid input: Please enter your age as a number")
#        input("Press Enter to try again")
#        clear()
   

"example: the error system can't catch"

# try:
#    age = int(input("How old are your?"))
# except ValueError:
#    print("invalid input")
#    age = int(input("How old are your?"))

# if age >18:
#    print("You can drive at age {age}")

# # output: "How old are your?21
# # You can drive at age {age}"
#    print(f"You can drive at age {age}")

"Squash bugs with a print() Statement"

# word_per_page =0
# pages = int(input("Number of pages: "))
# word_per_page =(int(input("Number of words per page:")))
# total_words = pages * word_per_page
# print(total_words)

"how to use debugger and break out in a code"

"""lear how to use debugger in vscode, pycharm

    step over, step into, step into my code(ignore library function)"""

# import random


# def mutate(a_list):
#     b_list =[]
#     new_item =0
#     for item in a_list:
#         new_item = item*2
#         new_item += random.randint(1,3)
#         new_item = new_item + item
#         b_list.append(new_item)
#     print(b_list)

# mutate([1,2,3,5,8,13])

"""HIGHER OR LOWER GAME PROJECT"""

# import random
# from turtle import clear

# data =[
#    {
#       'name': 'Instagram',
#       'follower_count' : 364,
#       'description': 'Social media platform',
#       'country': 'United States'

#     },
#    {
#       'name': 'Cristiano Ronaldo',
#       'follower_count' : 215,
#       'description': 'Footballer',
#       'country': 'Portugal'
       
#    },
#    {
#       'name': 'Ariana Grade',
#       'follower_count' : 187,
#       'description': 'Musician and actress',
#       'country': 'United States'
       
#    },
#    {
#       'name': 'Dwayen Johnson',
#       'follower_count' : 177,
#       'description': 'Actor and professional wrestler',
#       'country': 'United States'
       
#    }]



# # from the account data into printable formate.
# def format_data (account):
#     """Takes the account data and returns the pritable format."""

#     account_name = account["name"]
#     account_desc = account["description"]
#     account_country = account["country"]
#     return f"{account_name},a {account_desc},from {account_country}"


# def check_answer(user_guess, a_follwers, b_followers):
#     """Take a user's guess and the followers count and returns if the user is right"""
    
#     if a_follwers > b_followers:
#       #   if guess == 'a':
#       #       return True
#       #   else:
#       #       return False
#       #   or
#         return guess == "a"
#     else:
#         return guess == "b"

# score = 0  
# # Making account at position B become the next account at position A.
# account_b = random.choice(data)
# # Make the game repeatable
# game_should_continue = True
# while game_should_continue:

#    # Generate the random account from the game data
#    # Making account at position B become the next account at position A.
#    """In our second guess the account b from first guess should become account a and account b should continued to be random pick
#       so we mentioned account_a outside the look and modified it inside the loop for futher guess"""
   
#    account_a = account_b
#    account_b = random.choice(data)

#    if account_a == account_b:
#       account_b = random.choice(data)

#    # you are going to call the description
#    print(f"Compare A:{format_data(account_a)}.")
#    print("VS")
#    print(f"Against B:{format_data(account_b)}")

#    # ask user for a guess.
#    print(f"Guess who has more followers in Social media?")
#    guess = input(f"Type 'A' for {account_a["name"]} and 'B' for {account_b["name"]} :").lower()

#    # clear the screen
#    print("\n" *20)
   
#    # check if the user is correct
#    # -Get follower count of each account
#    a_followers_count = account_a["follower_count"]
#    b_followers_count = account_b["follower_count"]

#    is_correct = check_answer(guess,a_followers_count,b_followers_count)

#    # Give user feedback on their guess.
#    # score keeping.
  
#    if is_correct:
#       score += 1
#       print(f"You are right! Current score {score}")
      
#    else:
#       game_should_continue = False
#       print(f"Sorry, that's wrong. Final score: {score}")
      
"NOTE PROJECT: COFFEE MACHINE PROJECT"

# print
# what would you like? (espresso/latte/cappuccino):
# Print report

# Check resource sufficient?

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit  =0 
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on =True

while is_on:
   choice =input("what would you like? (espresso/latte/cappuccino):")
   if choice == "off":
      is_on = False
# to get the current resources values left in the machine
   elif choice == "report":
   