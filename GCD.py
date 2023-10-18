# Python code for finding the node (the largest common divisor) of two numbers:

def gcd(a: int, b: int) -> int:     
  if b == 0: return a  
    
  else: return gcd(b, a % b)  

# Usage example:

a = 24
b = 36

print(f"GCD of numbers {a} and {b} : {gcd(a, b)}")

"""
Result of execution: NODE numbers 24 and 36 : 12
In this example, we used the recursive function GCD, which finds the GCD of numbers a and b.
If one of the numbers is zero, then GCD is equal to the other number.
Otherwise, we calculate GCD for the remainder of dividing a larger number by a smaller number and a smaller number.
"""
