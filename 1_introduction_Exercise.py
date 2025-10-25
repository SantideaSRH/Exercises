#Write a program that asks for a name and prints a persolanized greeting, 
# With a calculation of your birth year

name=input("Enter your name: ")
name=name.capitalize()
print(f"Hello {name}!")
age= int(input("Enter your age: "))
current_year=2025
birth_year= str(current_year - age)
print(f"You where bron in the year {birth_year}.")