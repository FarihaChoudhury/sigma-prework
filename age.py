# Challenge 3 - Task 1: 
# Given your DOB input, caluclate your age
import datetime

def input_date():
    date_str = input('Enter your date of birth in this format yyyy-mm-dd: ')
    date_of_birth = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    return date_of_birth.date()

def calculate_age(date_of_birth):
    today = datetime.datetime.now().date()
    # False if today's month and day is less than DOB month and day, else True. 
    # False = 0, True = 1
    age = today.year - date_of_birth.year -(((today.month, today.day) < (date_of_birth.month, date_of_birth.day)))
    print(f'Your age is {age}')
    return age



date_of_birth = input_date()
age = calculate_age(date_of_birth)