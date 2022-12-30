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

def coordinate(id_val):
    return list(id.keys())[list(id.values()).index(id_val)]

[hashmap_graph[id[(x,y)]].extend(get_neighbor(x,y)) for x, row in enumerate(matrix) for y, val in enumerate(row)]

print(hashmap_graph)
