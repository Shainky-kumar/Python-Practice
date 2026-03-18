# # Variable in python 

# in Python, variables are used to store data that can be referenced and manipulated during program execution. A variable is essentially a name that is assigned to a value.


# 1.

X = 8,
Y = 10,
Name = "Python"
print(X)
print(Y)
print(Name)

# 2. Addition of two numbers using variables

a = 5
b = 10
print(a + b)  # Output: 15

c = a+b
print(c)  # Output: 15

# 3. Substraction of two numbers using variables

a = 15
b = 5
print(a - b)  # Output: 10

c = a - b
print(c)  # Output: 10

# 4. Multiplication of two numbers using variables

a = 5
b = 10
print(a * b)  # Output: 50

c = a*b
print(c)  # Output: 50

# 5. Division of two numbers using variables

a = 10
b = 90 
print(a / b)  # Output: 0.1111111111111111

c = a / b
print(c)  # Output: 0.1111111111111111

# 6. Modulo of two numbers using variables

a = 94
b = 10
print(a % b)  # Output: 0

c = a%b
print(c)  # Output: 0



# 7. Float number used
a = 3.14
b = 2.71
print(a + b)  # Output: 5.85

c = a + b
print(c)  # Output: 5.85

# 8. string used

first_name = "shainky"
last_name = "kumar"
full_name = first_name + " " + last_name
print(full_name)  # Output: shainky kumar
print("Hello, " + full_name + "!")  # Output: Hello, shainky kumar!
print("My name is " + full_name + ".")  # Output: My name is shainky kumar.
print("I am " + str(22) + " years old.")  # Output: I am 22 years old.
print(first_name + last_name)  # Output: shainkykumar


# 9. boolean used

is_raining = True
is_sunny = False
print("Is it raining?", is_raining)  # Output: Is it raining? True
print("Is it sunny?", is_sunny)  # Output: Is it sunny? False

# counting the number of characters in a string using a variable

Name = "shainky kumar"
length_of_name = len(Name)
print("The length of the name is:", length_of_name)  # Output: The length of the name is: 13



# 10. type conversion using variables

number_str = "42"
# name_str = "shainky"
# number_int = int(name_str) # not working because name_str is not a number can only convert number_str to int
# print("The string value is:", name_str)  # Output: The string value is: shainky
number_int = int(number_str)
print("The integer value is:", number_int)  # Output: The integer value is: 42


# 11. type casting using variables

number_float = float(number_int)
print("The float value is:", number_float)  # Output: The float value is: 42.0

number = type(number_float)
print("The type of the variable is:", number)  # Output: The type of the variable is: <class 'float'>



# 12. Converting different data types to string using variables

# Int to string
print(str(123))         # "123"

# Float to string
print(str(3.14))        # "3.14"

# Bool to string
print(str(True))        # "True"
print(str(False))       # "False"

# List to string
print(str([1,2,3]))     # "[1, 2, 3]"

# None to string
print(str(None))        # "None"

# 13 . Converting int to boolean using variables

int = 0
print(bool(int))  # Output: False (0 is falsy)
int = 5
print(bool(int))  # Output: True (non-zero is truthy)

# 14. Converting string to boolean using variables
string = "Hello"
print(bool(string))  # Output: True (non-empty string is truthy)
empty_string = ""
print(bool(empty_string))  # Output: False (empty string is falsy)
space_string = " "
print(bool(space_string))  # Output: True (string with space is truthy)
one_string = "0"
print(bool(one_string))  # Output: True (non-empty string is truthy)


# 15. Converting float to boolean using variables
float_num = 0.0
print(bool(float_num))  # Output: False (0.0 is falsy)
float_num = 3.14
print(bool(float_num))  # Output: True (non-zero float is truthy)

# 16. Converting boolean to int using variables

bool_true = True
bool_false = False

print(int(True))    # 1
# print(int(bool_false))   # 0
print(float(bool_true))  # 1.0
print(str(bool_true))    # "True"


# 17. Converting string to List using variables

# String to list
print(list("hello"))        # ['h','e','l','l','o']

# Tuple to list
print(list((1,2,3)))        # [1, 2, 3]

# Set to list
print(list({1,2,3}))        # [1, 2, 3]

# Dict to list (gives keys)
print(list({"a":1,"b":2}))  # ['a', 'b']

# Range to list
print(list(range(5)))       # [0, 1, 2, 3, 4]

