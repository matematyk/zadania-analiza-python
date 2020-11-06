# zadania-analiza-python

### instalaction
```
conda activate base
source /home/mw/anaconda3/bin/activate 
```

Task 1
Write a program that takes an integer and displays its factorization into prime numbers. Assume that the user enters a valid integer number.

Task 2

Write a program that calculates an approximation of the pi number using the Monte-Carlo method. The program should ask the user for the total number of iterations and the step of printing and then display the current approximation after each step number of iterations and then the final value.

Task 3
Write a function sorted_set_sum(lst1, lst2) that returns the set-theoretic sum of arguments. In this exercise, sets are to be represented as lists of their elements in ascending order (hence there are no duplicates on these lists). You are allowed to use on lists only indexing and the len and append functions.

Sample results of the function:
```
sorted_set_sum([], []) == []
sorted_set_sum([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
sorted_set_sum([], [1, 2, 3]) == [1, 2, 3]
sorted_set_sum([1, 2, 3], []) == [1, 2, 3]

sorted_set_sum([-2, 1, 3], [-3, -2, 0, 1, 34]) == [-3, -2, 0, 1, 3, 34]
```

Additional Task (not obligatory, possibility to get additional points)
A long time ago in a galaxy (not so) far, far away... we have 1000 bottles and 10 brave adventurers.
The task is to detect 1 special bottle hidden among those 1000.
All bottles contain water, and are indistinguishable, as the water inside them is too.
Everyone who will drink from the special bottle will lose the ability to speak for a year, but the effect starts the next day.
The water in bottles never ends (or can be divided infinitely), so everyone is able to drink from every bottle.
The effect of the special bottle is inevitable, no matter if somebody drinks only one drop or more from it.
Design a system of detecting the special bottle in one day, that minimizes the number of people affected.
HINT: Effect of special bottle starts the next day, that means you have only one iteration.
(A) What is the maximal number of people affected (in worst case scenario)?
HINT: If you invent a system, the answer need no computation.
(B) Show the sample simulation as follows:
    Special bottle number is 123

    Person 1 will drink from bottles 1,2,3,...,100
    Person 2 will drink from bottles...
    ...
    Person 10 will drink from bottles ...
