import random  as rd

"""
Write a program that calculates an approximation of the pi number using the Monte-Carlo method. 
The program should ask the user for the total number of iterations and the step of printing and then display 
the current approximation after each step number of iterations and then the final value.
"""

def monte_carlo(points_in_square=10 ** 5, step_of_printing = 10):
    points_in_circle = 0

    
    for i  in range(1, points_in_square):
        x, y = rd.uniform(-1,1), rd.uniform(-1,1)

        if(x** 2 + y ** 2 <= 1):
                points_in_circle += 1
        
        PI = 4 * points_in_circle / points_in_square
        if i % step_of_printing == 0:  
            print(PI)
        
    return PI 



if __name__ == "__main__":
    iteraction = int(input("Please define number of iteration"))
    step = int(input("Please define step of printing value"))
    print(monte_carlo(points_in_square=iteraction, step_of_printing=step))

