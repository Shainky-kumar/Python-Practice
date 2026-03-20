# conditionals statement :- used to perform different actions based on different conditions. In Python, we have several types of conditional statements, including if, elif, and else. Here are some examples of how to use conditional statements in Python:


# import pyttsx3
# engine = pyttsx3.init()
# engine.say("hello i am shainky thakur software developer at alpinetech")
# engine.runAndWait()


# Example 1: Using if statement
X = int(input("Enter a number: "))

if X > 0:
    print("The number is positive.")
elif X < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Example 2: Using if-else statement

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Example 3: Using nested if statements
Y = int(input("Enter a number: "))
if Y % 2 == 0:
    print("The number is even.")
else:   
    print("The number is odd.")

# Example 4: Using if-elif-else statement
grade = int(input("Enter your grade: "))
if grade >= 90:
    print("You got an A.")
elif grade >= 80:
    print("You got a B.")
elif grade >= 70:
    print("You got a C.")
elif grade >= 60:
    print("You got a D.")
else:
    print("You got an F.")

# Example 5: Using if statement with logical operators
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > 0 and num2 > 0:
    print("Both numbers are positive.")
elif num1 < 0 and num2 < 0:
    print("Both numbers are negative.")
else:
    print("The numbers have different signs.")


# calculator using conditionals

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Enter the operation (+, -, *, /): ")
if operation == "+":
    result = num1 + num2
    print("The result is:", result)
elif operation == "-":
    result = num1 - num2
    print("The result is:", result)
elif operation == "*":
    result = num1 * num2
    print("The result is:", result)
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("The result is:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of the following: +, -, *, /.")

# using loops calculator
#  i want to use the multiple number to perform the operations and also want to exit the calculator when user want to quit

while True:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /) or 'q' to quit: ")
        if operation == "q":
            print("Exiting the calculator. Goodbye!")
            break
        elif operation == "+":
            result = num1 + num2
            print("The result is:", result)
        elif operation == "-":
            result = num1 - num2
            print("The result is:", result)
        elif operation == "*":
            result = num1 * num2
            print("The result is:", result)
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
                print("The result is:", result)
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation. Please enter one of the following: +, -, *, /, or 'q' to quit.")

# using nested if statements to check the conditions of the calculator

M = int(input("Enter the pre exam marks: "))
if(M>=90):
    print("you clear the exam with A grade")
    if(M>=95):
        print("you are the topper of the class")
        O = int(input("Enter the project marks: "))
        if(O>=90):
            print("you clear the project with A grade")
            P = int(input("Enter the presentation marks: "))
            if(P>=90):
                print("you clear the presentation with A grade")
            elif(P>=80):
                print("you clear the presentation with B grade")
            else:
                print("you clear the presentation with C grade")
elif(M>=80):
    print("you clear the exam with B grade")
    N = int(input("Enter the post exam marks: "))
    if(N>=90):
        print("you clear the post exam with A grade")
    elif(N>=80):
        print("you clear the post exam with B grade")
    else:
        print("you clear the post exam with C grade")
elif(M>=70):
    print("you clear the exam with C grade")
else:
    print("you are fail in the exam")
