# Exercise 3: lambda functions for simple calculations
# Use filter() with a lambda function to select and return only the odd numbers from a given list of integers.
numbers = [1, 2, 3, 4, 5]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(f"Odd numbers from the list: {odd_numbers}")
# Use map() with a lambda function to square each number in a given list of integers.
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers from the list: {squared_numbers}")
# Use reduce() from the functools module with a lambda function to compute the product of all numbers
from functools import reduce
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print(f"Product of all numbers in the list: {product_of_numbers}")

