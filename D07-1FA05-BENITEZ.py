import math

"""
REFLECTION:
Using a math library is far more practical than writing calculations from scratch 
because it provides pre-built, highly optimized, and thoroughly tested functions 
that save development time and prevent mathematical errors. In this activity, 
math.sqrt() and math.pow() allowed us to implement the Euclidean distance formula 
clearly and efficiently in a single step. Without these library functions, calculating 
a square root directly would require manually implementing complex numerical algorithms 
like Newton's method, making the program vastly more difficult to write and maintain.

EXAMPLE TEST CASE (Run the code and enter these numbers):
Input:
  Enter x1: 2
  Enter y1: 3
  Enter x2: 7
  Enter y2: 8
Output:
  The distance between the two points is: 7.07
"""

def main():
    # Prompt user for coordinate inputs
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    # Calculate distance using sqrt() and pow() from the math library
    distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

    # Display the result formatted to 2 decimal places
    print(f"\nThe distance between the two points is: {distance:.2f}")

if __name__ == "__main__":
    main()