
# Program to find the largest of three numbers using nested if statements and logical operations
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))   
num3 = float(input("Enter third number: "))

# using nested if statements
if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3
print("The largest number is:", largest)


# using logical orperations
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print("The largest number is:", largest)
