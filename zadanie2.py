import random  as rd

"""
Write a program that calculates an approximation of the pi number using the Monte-Carlo method. 
The program should ask the user for the total number of iterations and the step of printing and then display 
the current approximation after each step number of iterations and then the final value.
"""

def monte_carlo(points_in_square=0):
    points_in_circle = 0

    
    for _ in range(1, points_in_square):
        x, y = rd.uniform(-1,1), rd.uniform(-1,1)

        if(x** 2 + y ** 2 <= 1):
            points_in_circle += 1

    PI = 4 * points_in_circle / points_in_square
    return PI 

print(monte_carlo(points_in_square=10**5))