#Use a for loop with the range() function and an if statement 
#to print all even numbers between 1 and 50, then rewrite it using a single while loop


for num in range(1,51):
    if num % 2 == 0:
        print(f"{num} is even")

print ("-----")

#Rewriting using a while loop
num = 1
while num <= 50:
    if num % 2 == 0:
        print(f"{num} is even")
    num += 1


    