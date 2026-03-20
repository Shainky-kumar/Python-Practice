
# For loops: For loops are used to iterate over a sequence such as a list, tuple, string or range. They allow to execute a block of code repeatedly, once for each item in the sequence.

# syntax of for loop:
# for variable in sequence:
#     # block of code to be executed

# for i in range(condition)
#         statement 

# 1. example of for loop with a range in forward direction
for i in range(0, 5):
    # print(i)
    print("Hello, World!")
print()
for i in range(0, 5, 1):
    # print(i)
    print("Hello, World!")
print()

for i in range(5):
    # print(i)
    print("Hello, World!")
print()

# 2. example of for loop with a range in backward direction
for i in range(10, 5, -1):
    print(i)
print()

for i in range(10, 0, -1):
    print(i)

for i in range(10, -7, -2):
    print(i)

# 3. write an program to print the table of a number using for loop
num = int(input("Enter a number: "))
for i in range(1, 11):
    i = i * num
    print(i)


# while loops: While loops are used to execute a block of code repeatedly as long as a certain condition is true. They are useful when the number of iterations is not known beforehand.
# syntax of while loop:
# while condition:
#     # block of code to be executed

# 1. example of while loop
count = 0
while count < 5:
    print("Hello, World!")
    count = count + 1
print()


# 2. example of while loop with a break statement
count = 0
while count < 10:
    print(count)
    if count == 5:
        break
    count = count + 1
print()

# 3. example of while loop with a continue statement
count = 0
while count < 13:
    count = count + 1
    if count % 2 == 0:
        continue
    print(count)
   
   