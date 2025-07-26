#Numerical Method (Applicable only when an interval is given and for 
# algebric funct)


# Define the function evaluation wrapper
# Function evaluator using eval
def funct(x):
    return eval(function)

# Get user-defined function
function = input("Write a function related to x : ")
print("Your function is:", function)

# Input a and b such that f(a) * f(b) < 0
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))

fa = funct(a)
fb = funct(b)

# Check condition for root existence
if fa * fb >= 0:
    print("Bisection method not applicable: f(a) * f(b) >= 0")
else:
    print("\nStarting Bisection Method for 5 iterations:\n")
    for i in range(1, 6):
        c = (a + b) / 2
        fc = funct(c)

        print(f"Iteration {i}:")
        print(f"  a = {a}, f(a) = {fa}")
        print(f"  b = {b}, f(b) = {fb}")
        print(f"  c = {c}, f(c) = {fc}\n")

        # Update interval
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
