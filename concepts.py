my_name = "Rachell"

def give_my_name():
    a_name = "Daniela"
    print(a_name)

print(my_name)

user_input = input("What is your name? ") 
print(f'Nice to meet you, {user_input}!')

# data types
my_string = "This is my string."
my_integer = 1456
my_float = 3.0
is_my_boolean = True

print(my_integer + my_float)

my_declaration = ""
my_initialization = "Hello world"

add = 1 + 2 
subtract = 2 - 1 
divide = 2 / 1
multiply = 1 * 3 
modulo = 10 % 3
exponent = 2 ** 3 

print(modulo)

statement = 4 > 2 
statement2 = 4 >= 2
statement3 = 4 <= 2 
statement4 = 4 == 2 
statement5 = 4 != 2

print(statement)


message = 4 > 2 and 33 < 43 
message2 = 4 < 2 or 33 < 43
x = False 

print(not x)
print(message)

# PEMMDAS

y = 10
x = y >= 10 

z = 7 // 2 
print(z)


def my_function():
    print('I am so great!')

my_function()

def add(num1, num2):
    print(num1 + num2)

my_name = "tacocat"
words = my_name.split('o')
print(words) 

def subtract(num1, num2):
    return num1 - num2

difference = subtract(4,2)

print(difference)