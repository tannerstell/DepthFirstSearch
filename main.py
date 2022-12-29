from pandas import DataFrame

matrix = [[1,0,0,1,0],[1,0,1,0,0],[0,0,1,0,1],[1,0,1,0,1],[1,0,1,1,0]]

df = DataFrame(matrix)
print(df)

# Problem: Find the lengths of connecting 1s (horizontally and vertically inclusive),
# and return an array of largest to smallest lengths (Excluding paths containing same path).

# 1. Structure: Since this is a two dimensional array, double for loop may be necessary.
# 2. Method: Depth-first search method will be useful, as there will be multiple paths

# Process:
# 1. Loop through each column and find the longest path of 1s, backtracking if necessary.
# 2. Append the integers of the length of paths to a list.

# hashmap = [(x,{}) for x in range(len(matrix))]
# hashmap = dict(hashmap)
hashmap = dict(((x,y),(y)*len(matrix)+x+1) for y, sublist in enumerate(matrix) for x, item in enumerate(sublist))

path = []
paths = []

def get_coordinates(center, df):

    x,y = center
    coordinates = [(x,y-1),(x+1,y),(x,y+1),(x-1,y)] # Up, Right, Down, Left
    for c in coordinates:
        if c[0]>=0 and c[1]>=0:
            x,y = c
            try:
                if df[x][y]==1 and df[x][y]==1 and hashmap[(x,y)] not in path:
                    df[x][y] = '#'
                    path.append(hashmap[(x,y)])
                    center = (x,y)
                    return get_coordinates(center, df)
            except:
                pass
        else:
            pass
    return

for y in range(len(matrix)):
    for x, val in enumerate(matrix[y]):
        if val==1:
            path.append(hashmap[(x,y)])
        get_coordinates((x,y), matrix)
        paths.append(path)
        path = []

t = max([len(path) for path in paths])
print(t)