# print("Maksim Hello")
# my_list = [1, 2, 3]


# print(my_list)


"""long_str = "This is a 
very 
long string"

print("1) " + long_str)

print("2) ", type(long_str))

print("3) ", len(long_str))

print("4) ", long_str[0])

print("5) " + long_str[0:6])

print("6) " + long_str[3:])"""


# Methods

"""my_new_string = "Hello, My name is Maksim"

print(my_new_string)

print(my_new_string.replace("Maksim", "Anastasiya"))

print(my_new_string.count(" "))

print(my_new_string.count("is"))"""


# Целые числа


"""friend_qty = 50

print(friend_qty)

print(type(friend_qty))


any_num = input("Enter any number: ")

print(any_num)

print(type(any_num))  # type will be - str


int_num = int(input("Insert any number: "))

print(int_num)

print(type(int_num))  # type will be - number"""


# Возведение в степень

base = 5
power = 3

print(pow(base, power))


# Длинные числа - разрешены нижние подчеркивания, для удобства чтения, но при выводе они не учитываются

"""one_million = 1_000_000

print(one_million)  # 1000000

my_number = 3_427

print(my_number)  # 3427"""

# Задача

"""input_str = input("Insert any number  ")
input_int = int(input_str)

print(input_int)

print(type(input_int))"""

"""
first_num = 5
second_num = 10

print(pow(first_num, second_num))
print(type(pow(first_num, second_num)))

"""

# Выше идет очень интересная тема создания новых файлов и папок, что позволяет нам создавать папки через код. остановился на уроке 200.

#Вычисление факториала. 

# import math

# def calc_factorial(num):
#     if type(num) is not int:
#         raise TypeError("The number should be integer")
#     if num <= 0:
#         raise ValueError("The number should be higher that 0")
#     if num == 1:
#         return 1
#     return calc_factorial(num - 1) * num
    
    
# print(calc_factorial(10))

# print(math.factorial(10))


# ======================================================

# Проверка имейлов при использвании регулярных выражений. 

"""import re


def check_email(email):
    email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"

    email_check_pattern = re.compile(email_regexp)
    validation_result = 'valid' if email_check_pattern.fullmatch(email) else "not valid"
    return (email, validation_result)

#Valid
('bs@gmail.com', 'valid')
print(check_email('bs@gmail.com'))  # ('bs@gmail.com', 'valid')
print(check_email('b_s@gmail.com'))
print(check_email('b.s@gmail.com'))
print(check_email('bs@sub.gmail.com'))

# <re.Match object; span=(0, 12), match='bs@gmail.com'>
#not valid
print(check_email('bs@')) 
print(check_email('bsgmail.com')) 
print(check_email('@gmail.com')) 
print(check_email('bs@gmailcom'))  # ('bs@gmailcom', 'not valid')"""

#Проверка паролей

import re

def check_password(password):
    length_pattern = re.compile(r"\S{,8}")
    lowercase_pattern = re.compile(r"^.*[a-z]+.*$")
    uppercase_pattern = re.compile(r"^.*[A-Z]+.*$")
    number_pattern = re.compile(r"^.*[0-9]+.*$")
    special_symbol_pattern = re.compile(r"^.*[@%#!&*^]+.*$")
    no_wite_space_pattern = re.compile(r"^\S*$")

    if not re.fullmatch(no_wite_space_pattern, password):
        return (False, "No white space allowed in the password")
    
    if not re.fullmatch(length_pattern, password):
        return (False, "Password mush have at least 8 symbols")
    
    if not re.fullmatch(lowercase_pattern, password):
        return (False, "Password must have at least one lowercase letter")
    
    if not re.fullmatch(uppercase_pattern, password):
        return (False, "Password must have at least one uppercase letter")
    
    if not re.fullmatch(number_pattern, password):
        return (False, "Password must have at least one number")
    
    if not re.fullmatch(special_symbol_pattern, password):
        return (False, "Password must have at least one special symbol @%#!&*^")
    return (True, "Password is valid")


while(True):
    password = input("Please enter password: ")
    password_check_result = check_password(password)
    if password_check_result[0]:
        print(password_check_result[1])
        break
    print(password_check_result[1])
    