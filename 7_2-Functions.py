#Excercise 2: Recursive Fibonacci
def fibonacci(n):
    """computes the nth Fibonacci number recrusively"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Base case is n=0 and n=1
        return fibonacci(n - 1) + fibonacci(n - 2)
    

print (f"Fibonacci sequence for n=4: {fibonacci(7)}")
