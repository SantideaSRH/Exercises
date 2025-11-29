#EXCERCISE 3: LEGB Rule Illustration
#Global scope variable
x = "global"

def outer_function():
    #Enclosing scope variable
    x = "enclosing"
    
    def inner_function():
        #Local scope variable
        x = "local"
        print("Inner scope (L):", x)  # Should print "local"
    
    inner_function()
    print("Outer scope (E):", x)      # Should print "enclosing"

outer_function()
print (f"Global scope (G): {x}") #uses Global x
print (f"Bulit-in scope (B): {len}") #uses Built-in name
