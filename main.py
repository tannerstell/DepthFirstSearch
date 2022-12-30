from pandas import DataFrame

matrix = [[1,1,0,1,0],[1,1,1,0,0],[0,0,1,0,1],[1,0,1,0,1],[1,0,1,1,1]]
df = DataFrame(matrix)

# Generates incremented id for every coordinate and assigns the coordinate as the key and returns the unique id.
hashmap_graph = dict([(i*len(row)+j,[]) for i,row in enumerate(matrix) for j,val in enumerate(row)])
id = dict([((i,j),i*len(row)+j) for i,row in enumerate(matrix) for j,val in enumerate(row)])

def get_neighbor(x,y):
    center = x,y
    mappings = [(x,y-1),(x,y+1),(x-1,y),(x+1,y)]
    neighbors = []
    for mapping in mappings:
        try:
            x,y = mapping
            if x>=0 & y>=0:
                if matrix[x][y]==1:
                    neighbors.append(id[(x,y)])
        except:
            pass
    return neighbors


def get_coordinate(id_val):
    return list(id.keys())[list(id.values()).index(id_val)]

def backtracking():

    pass
path = [0]
paths = []
visited = set()

def dfs(id):
    if id not in visited:
        visited.add(id)
    temp_hashmap = hashmap_graph.copy()
    neighbors = temp_hashmap[id]
    for neighbor in neighbors:
        if neighbor not in visited:
            visited.add(neighbor)
            path.append(neighbor)
            return dfs(neighbor)
        else:
            neighbors.pop(0)
            dfs(id)

    if neighbors==[] and len(path)!=0:
        x = [True for subpath in paths if set(path).issubset(set(subpath))]
        if not True in x:
            paths.append(path.copy())
        path.pop()
    if len(path)==0:
        return paths
    dfs(path[-1])

[hashmap_graph[id[(x,y)]].extend(get_neighbor(x,y)) for x, row in enumerate(matrix) for y, val in enumerate(row)]

dfs(0)
print(visited)
