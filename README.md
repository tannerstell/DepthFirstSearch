# DepthFirstSearch

Problem: Find the lengths of connecting 1s (horizontally and vertically inclusive),
and return the maximum length of connected 1s (Excluding paths containing same path).

Problem 2: Return an array of largest to smallest lengths of connecting ones. 

1. Structure: Since this is a two dimensional array, double for loop or DataFrame may be necessary.
2. Method: Depth-first search method will be useful, as there will be multiple neighbors
           fulfilling conditions for a given cell.

Process:
1. Loop through each column and find the longest path of 1s, backtracking if necessary.
2. Append the integers of the length of paths to a list.
