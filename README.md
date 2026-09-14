DISTANCE CALCULATOR
This Python program calculates the distance between two points using the Euclidean distance formula. The user enters the coordinates of two points, and the program displays the distance between them.
The program uses Python's math library to perform the calculation and displays the answer rounded to two decimal places.

Sample Output:
**import math

  x1 = float(input("Enter x1: "))
  y1 = float(input("Enter y1: "))
  x2 = float(input("Enter x2: "))
  y2 = float(input("Enter y2: "))

  
  distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

    
  print(f"\nThe distance between the two points is: {distance:.2f}")

if __name__ == "__main__":
    main()
