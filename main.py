matrix = [[1,0,0,1,0],[1,1,1,0,0],[0,0,1,0,1],[1,0,1,0,1],[1,0,1,1,1]]

# Generates incremented id for every coordinate and assigns the coordinate as the key and returns the unique id.
hashmap = dict(((x,y),(y)*len(matrix)+x+1) for y, sublist in enumerate(matrix) for x, item in enumerate(sublist)) 

path = []
paths = []

def get_coordinates(center, matrix):
    x,y = center
    coordinates = [(x,y-1),(x+1,y),(x,y+1),(x-1,y)] # Up, Right, Down, Left
    for c in coordinates:
        if c[0]>=0 and c[1]>=0:
            x,y = c
            try:
                if matrix[x][y]==1 and matrix[x][y]==1 and hashmap[(x,y)] not in path:
                    matrix[x][y] = '#'
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
