# Mazesolver

A user is waiting to be programmed to navigate a maze. The user is required to start at the starting point (S) and find a path, if exist, to the destination (D). Arrows indicate with paths can be reached from with point. If there is at least one path from S to D, the it should tell the master and show a map, or otherwise just tell the master no path exists from S to D.

For this project, I used recursion to solve mazes. First, I to wrote a Python file that implementened the maze solver. The maze is a two-dimensional array/lists. The numbers of rows and columns are given by the user, and must be in the range of [5, 10] inclusively, without the number of rows being the same as that of columns. For example, if the number of rows is 6, then the number of column cannot be 6. The program needs to validate the input and ask for another input if invalid instead of terminating. Also, the program should print out corresponding reasons about why the input is invalid. For example, if the input is "a", the program should print "Sorry, the letter can't be used to set the number of rows. Please type in an integer within the range of [5, 10] inclusively". Once obtained, the number of rows and columns will be used to generate the maze. The maze consists of four symbols as below:

 - Number (e.g., "5") is the position where the user is able to move. The number indicates the amount of coins that the user can collect at that position.
 - Arrows ("→", "←", "↑", "↓") indicates the direction the user can travel between numbers
 - "S" is the starting point. 
 - "D" is the destination.
 
The "S" is always at the top left, while the "D” is always at the bottom right of the maze. Numbers are randomly generated to fill the maze. The number should be within the range of [1, 99] inclusively. Arrow directions are also randomly choosen, with a 2/3 chance toward down and right directions, and 1/3 chance of up and left. Once the maze is drawn, the program should print it on the screen. The user always starts from "S" and tries to find an available path to "D". The user is able to move one step every time in one of the four directions (up, down, left and right) as long as there is an arrow with that corresponding direction. If the user is not able to find a path, it will print the result accordingly. If the user finds a path, then it needs to do two things:

 1. print out the maze with the path marked by "+".
 2. sum up all the numbers on this path and printed it out as the amount of coins found. *(Hint: you may need to cast the number to int in order to do arithmetic operation.)*
