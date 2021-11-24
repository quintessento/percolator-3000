import random


class Node:
    
    def __init__(self, row: int, col: int, content):
        self.row = row
        self.col = col
        self.content = content
        
        self.left_child = None
        self.right_child = None
        self.bottom_child = None
        
    def __str__(self):
        return "(row=" + str(self.row) + ", col=" + str(self.col) + ") -> " + str(self.content) 
    

values = []

def build_table(rows: int, cols: int, percolation_value: float) -> None:
    for i in range(rows):
        values.append([])
        for j in range(cols):
            values[i].append((0, 1)[random.uniform(0.0, 1.0) > percolation_value])
            

def render_table():
    text = ""
    for row in values:
        text += '\n'
        for cell in row:
            text += str(cell)
            
    print(text)
    
    
unvisited = []
visited = []
path = []
trees = []
    
    
def find_path():
    for j in range(0, len(values[0])):
        cell_value = values[0][j]
        if cell_value == 1:
            trees.append(Node(0, j, 1))
    
    print("Created", len(trees), "trees")
    for tree in trees:
        current_node = tree
        left_index = (current_node.row, current_node.col - 1)
        right_index = (current_node.row, current_node.col + 1)
        bottom_index = (current_node.row + 1, current_node.col)
        print(current_node, "L: ", left_index, "R: ", right_index, "B: ", bottom_index)
    
    #for i in range(1, len(values)):
        #row = values[i]
        #for j in range(len(row)):
            #cell_value = row[j]
            
    
    
build_table(10, 10, percolation_value = 0.5)
render_table()
find_path()
            
