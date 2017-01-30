# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: In sudoku problem, we can find out the possible answers in each box. If there is only one possible answer in the box, then we can consider that the box has been answered. To reduce the possible answers in the box, we can usear several constraint propagation strategies. The naked twins is one of the constraint propagation strategies. In one unit (row, column or 3X3 squares), if there are 2 boxes having same 2 digits, then we sure that thoese 2 digits are unable to be appeared in other boxes in the unit.

So, to resolve this naked twins proble, first of all, find the naked twins from the each unit in unitlist. If there is a naked twins in the unit, then remove 2 digits of naked twins value from the the other boxes in the same unit.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: Simply we can consider this problem as an addition of 2 diagonal units. If we add those 2 diagonal units into new diagonal_units, then add diagonal_units into unitlist, then our Constraint Propagation (Eliminate Strategy, Naked Twins Strategy and Only Choice Strategy) will be applied to diagonal_units same as row_units, column_units and square_units.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.