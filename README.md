# DepthFirstSearch

This is a problem I created that was inspired by other matrix puzzles. The neighboring values are referenced quaddirectionally (up,down,left,right).

 
I'm would like to work on making an algorithm that will reference 8 neighboring cells ( up_left, up, up_right, left, right, down_left, down, down_right).


Problem: Find the lengths of connecting 1s (horizontally and vertically inclusive),
and return the maximum length of connected 1s.

Problem 2: Return an array of largest to smallest lengths of connecting 1s (Excluding paths containing same path).



**Documentation before solving problem:**

1. Structure: Since this is a two dimensional array, double for loop or DataFrame methods may be necessary.
To simplify indexing coordinates, unique IDs can be generated with a hashmap, using the respective coordinate
as a key and id as value.

3. Method: Depth-first search method will be useful, as there will be multiple neighbors
           fulfilling conditions for a given cell.

Process:
1. Loop through each row and column
2. Call a recursive function that gets the coordinates and values of neighbors.
3. If the value of the neighbor is a 1, then append it to a list of paths for the current cell. (path)
4. Recursively call the function again to find neighbors.
5. Find the maximum length of all of the paths. (paths)

Bugs to fix: The recursive function returns path before other paths can be checked.
