import random
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np


class Node:
    
    def __init__(self, row: int, col: int, content):
        self.row = row
        self.col = col
        self.content = content
        self.visited = False
        
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
    

trees = []
    
    
def build_trees(rows, cols):
    for j in range(cols):
        cell_value = values[0][j]
        if cell_value == 1:
            trees.append(Node(0, j, 1))

    def bt(node: Node, depth: int):
        left_index = (node.row, node.col - 1)
        right_index = (node.row, node.col + 1)
        bottom_index = (node.row + 1, node.col)

        if node.content is not 1:
            print(node, "L: ", left_index, "R: ", right_index, "B: ", bottom_index)

        if left_index[0] >= 0 and values[left_index[0]][left_index[1]] == 1 and node.left_child is None:
            node.left_child = Node(left_index[0], left_index[1], 1)
            node.left_child.right_child = node
            bt(node.left_child, depth)
        if right_index[1] < cols and values[right_index[0]][right_index[1]] == 1 and node.right_child is None:
            node.right_child = Node(right_index[0], right_index[1], 1)
            node.right_child.left_child = node
            bt(node.right_child, depth)
        if bottom_index[0] < rows and values[bottom_index[0]][bottom_index[1]] == 1:
            node.bottom_child = Node(bottom_index[0], bottom_index[1], 1)
            bt(node.bottom_child, depth + 1)
    
    print("Created", len(trees), "trees")
    for tree in trees:
        bt(tree, 0)
    
    
def pour_water():

    def traverse(node: Node):
        values[node.row][node.col] = 2
        node.visited = True
        if node.left_child is not None and not node.left_child.visited:
            traverse(node.left_child)
        if node.right_child is not None and not node.right_child.visited:
            traverse(node.right_child)
        if node.bottom_child is not None and not node.bottom_child.visited:
            traverse(node.bottom_child)

    for tree in trees:
        traverse(tree)

    
rows = 10
cols = 10
build_table(rows, cols, percolation_value = 0.5)

# problematic values
values = [
    [1,0,0,1,1,1,1,1,1,1],
    [1,0,1,1,0,0,1,0,0,0],
    [1,0,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1,1,0,0],
    [1,1,0,0,0,1,1,0,0,1],
    [1,0,0,1,0,1,0,1,1,1],
    [0,1,0,1,1,0,0,0,1,0],
    [0,1,0,0,1,1,0,1,1,1],
    [1,1,0,1,0,1,0,1,1,0],
    [0,1,0,0,1,1,1,1,1,1]
]


render_table()
build_trees(rows, cols)
pour_water()
render_table()


#data = np.random.randint(3, size = (10, 10))

cmap = colors.ListedColormap(['white', 'grey', 'green'])

fig, ax = plt.subplots()
ax.imshow(values, cmap=cmap)

# draw gridlines
ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=1)
ax.set_xticks(np.arange(-.5, 10, 1))
ax.set_yticks(np.arange(-.5, 10, 1))

plt.show()
            
