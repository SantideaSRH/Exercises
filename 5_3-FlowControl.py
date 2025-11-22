#Compute the factorial of a user-input number using a for loop,
#then rewrite it using a while loop, and compare their syntactic clarity.

#Using a for loop
number = int(input("Enter a number to compute its factorial using a for loop: "))
factorial_for = 1
for i in range(1, number + 1):
    factorial_for *= i
print(f"The factorial of {number} using for loop is: {factorial_for}")

#Using a while loop
number = int(input("Enter a number to compute its factorial using a while loop: "))
factorial_while = 1
i = 1
while i <= number:
    factorial_while *= i
    i += 1
print(f"The factorial of {number} using while loop is: {factorial_while}")

