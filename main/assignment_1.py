python3 -m pip install https://github.com/gcreneti/cot-4500-as1/blob/src/requirements.txt
#Function to find number of terms until convergence via bisection method
def bisection_method(left: float, right: float, function: str):
    x = left
    x = right
    iter = 0
    tol = 10**-4
    diff = right - left
    while (diff >= tol):
        iter += 1
        mid_point = (left + right) / 2
        x = mid_point
        evaluated_midpoint = eval(function)
        if evaluated_midpoint == 0.0:
            break
        evaluated_left_point = eval(function)
        first_conditional: bool = evaluated_left_point < 0 and evaluated_midpoint > 0
        second_conditional: bool = evaluated_left_point > 0 and evaluated_midpoint < 0
        if first_conditional or second_conditional:
            right = mid_point
        else:
            left = mid_point
        
        diff = abs(right - left)
    
    return(iter)

# Code that visualizes how the eval() function works
def function(val):
  return((val**3)+(4*val)*(val**2) - 10)

# Function to computue the derivative of the specific function we are using
def custom_deriv(val):
  return(3 * val * val) + (8 * val)

# Function to find the number of terms until convergence via Newton Raphson method
def newton_raphson(initial_approx: float, tol: float, seq: str):
    iter = 0
    x = initial_approx
    f = eval(seq)
    f_prime = custom_deriv(initial_approx)
    
    approx: float = f / f_prime
    while(abs(approx) >= tol):
        x = initial_approx
        f = eval(seq) 
        f_prime = custom_deriv(initial_approx)
        approx = f / f_prime
        initial_approx -= approx
        iter += 1
    return(iter)

# Process for representing binary number via double precision floating point

# s = first digit of the binary number
s = 0

# c = sum of the series 2^n, where n is the position of the next eleven non-zero integers of the binary number, counting backwards so n = 10, n+1 = 9, ..., n+10 = 0
c = (2**10) + (2**2) + (2**1) + (2**0)

# f = sum of series (1/2)^n, where n is the position of the next 12 non-zero integers of the binary number such that n=1, n+1=2, ..., n+11=12
f = (1/2)**1 + (1/2)**2 + (1/2)**3 + (1/2)**5 + (1/2)**7 + (1/2)**8 + (1/2)**9 + (1/2)**12

# Obtain number in double precision floating point via this formula
num = ((-1)**s) * (2**(c-1023)) * (1+f)
# Now that we know the number, can perform arithmetic to find chopped and rounded versions of the number
chop = 0.491 * 10**3
round = 0.4915 * 10**3 + 5*(1/10)

# Use absolute and relative error formulas to find errors between true and rounded number
abs_error = abs(num-round)
rel_error = abs(num-round)/abs(num)

#Find minimum terms to compute f(1) under a certain error
n = 0
err = 0

while err < 10**4:
  n += 1
  err = eval("(n+1)**3")

# Find number of terms via Bisection
bis_method = bisection_method(-4, 7, "x**3 + 4*x**2 - 10")

# Find number of terms via Newton-Raphson
n_r_method = newton_raphson(7, 10**-4, "(x**3) + (4*(x**2) - 10)")


print(float(num))
print("\n")

print(chop)
print("\n")

print(round)
print("\n")

print(abs_error)
print("\n")

print(rel_error)
print("\n")


print(n)
print("\n")

print(bis_method)
print("\n")

print(n_r_method)
