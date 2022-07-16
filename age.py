#This program is to predict the year on which the user will turn 100 years old
current_year = 2022
name = input("What's your name? ")
age = int(input("What's your age? "))
hundred_year = current_year + (100 - age)

print (f"{name}, you will turn hundred in {hundred_year}")