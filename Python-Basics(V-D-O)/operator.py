# operator is used to perform operations on variables and values. In Python, there are several types of operators, including arithmetic, assignment, comparison, logical, bitwise, membership, and identity operators. Here are some examples of how to use different types of operators in Python:

# 1. Arithmetic Operators
# 2. Assignment Operators
# 3. Relational Operators
# 4. Logical Operators
# 5. Bitwise Operators



# 1. Arithmetic Operators: - used to perform mathematical operations like addition, subtraction, multiplication, division, modulus, exponentiation, and floor division.

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


# 2. Assignment Operators: - used to assign values to variables. The most common assignment operator is the equal sign (=), but there are also other assignment operators like +=, -=, *=, /=, %=, **=, and //=.

a = 5
b = 10
a += b  # equivalent to a = a + b
print(a)  # Output: 15


x = 10
y = 5
x -= y  # equivalent to x = x - y
print(x)  # Output: 5


A = 3
B = 4
A *= B  # equivalent to A = A * B
print(A)  # Output: 12

X = 20
Y = 4
X /= Y  # equivalent to X = X / Y
print(X)  # Output: 5.0


# 3. Relational Operators: - used to compare two values and return a boolean result (True or False). The most common relational operators are ==, !=, >, <, >=, and <=.

a = 5
b = 10
print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)   # Output: False
print(a < b)   # Output: True
print(a >= b)  # Output: False
print(a <= b)  # Output: True


# 4. Logical Operators: - used to combine multiple boolean expressions and return a boolean result. The most common logical operators are and, or, and not.

a = 5
b = 10
print(a > 0 and b > 0)  # Output: True
print(a > 0 or b < 0)   # Output: True
print(not(a > 0))       # Output: False
print(not(b < 0))       # Output: True


# 5. Bitwise Operators: - used to perform bitwise operations on integers. The most common bitwise operators are &, |, ^, ~, <<, and >>.

a = 5  # in binary: 0101
b = 3  # in binary: 0011
print(a & b)  # Output: 1 (in binary: 0001)
print(a | b)  # Output: 7 (in binary: 0111)
print(a ^ b)  # Output: 6 (in binary: 0110)
print(~a)     # Output: -6 (in binary: 1010)
print(a << 1)  # Output: 10 (in binary: 1010)
print(a >> 1)  # Output: 2 (in binary: 0010

x = 5  # in binary: 0101
print(x << 2)  # Output: 20 (in binary: 10100)
print(x >> 2)  # Output: 1 (in binary: 0001)
print(x >> 1)  # Output: 2 (in binary: 0010)
print(x >> 3)  # Output: 0 (in binary: 0000)



