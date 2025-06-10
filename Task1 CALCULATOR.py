# Python Program Simple Calculator

# Step -1: Create functions:
# Function to Addition two numbers
def add(num1,num2):
    return num1 + num2

# Function to Substract two numbers
def sub(num1,num2):
    return num1 - num2

# Function to Multiply two numbers
def multiply(num1,num2):
    return num1 * num2

# Function to Divide two numbers
def divide(num1,num2):
    return num1 / num2

# Function to Module two numbers
def module(num1,num2):
    return num1 % num2

# Function to Average two numbers
def avg(num1,num2):
    return (num1 + num2)/2

# Step -2: User Input:
print("Please select a operation:\n " \
"1. Adition\n" \
"2. Substract\n" \
"3. Multiply\n" \
"4. Divide\n" \
"5. Module\n" \
"6. Average")

select = int(input("Select a operation from 1,2,3,4,5,6: "))

number1 =int(input("Enter First number: "))
number2 =int(input("Enter Second number: "))

# Step -3: Print Result:

if select == 1:
    print(number1, "+", number2, "=", \
          add(number1, number2))
    
elif select == 2:
    print(number1, "-", number2, "=", \
          sub(number1, number2))
    
elif select == 3:
    print(number1, "*", number2, "=", \
          multiply(number1, number2))
    
elif select == 4:
    print(number1, "/", number2, "=", \
          divide(number1, number2))
    
elif select == 5:
    print(number1, "%", number2, "=", \
          module(number1, number2))
    
elif select == 6:
    print("(number1, "+", number2)/2 =", 
          avg(number1, number2))
    
else: 
    print("Please select Correct number")