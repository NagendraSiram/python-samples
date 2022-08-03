# input is always read as string
# output always expects the variable to be string
name = input('What is your name? ')
print('Hello ' + name)
year_of_birth = input('What is your year of birth? ')
age = 2022 - int(year_of_birth)
print("Your age is " + str(age))