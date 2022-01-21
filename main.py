from array import array
from operator import le
import random
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from manim import *


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
    
def build_table(rows: int, cols: int, percolation_value: float) -> array:
    values = []
    for i in range(rows):
        values.append([])
        for _ in range(cols):
            values[i].append((0, 1)[random.uniform(0.0, 1.0) > percolation_value])

    return values
            

def render_table(values: array) -> None:
    text = ""
    for row in values:
        text += '\n'
        for cell in row:
            text += str(cell)
            
    print(text)
    
    
def build_trees(values: array) -> array:
    trees = []
    rows = len(values)
    cols = len(values[0])

    for j in range(cols):
        cell_value = values[0][j]
        if cell_value == 1:
            trees.append(Node(0, j, 1))

    def bt(node: Node, depth: int):
        left_index = (node.row, node.col - 1)
        right_index = (node.row, node.col + 1)
        bottom_index = (node.row + 1, node.col)

        if left_index[1] >= 0 and values[left_index[0]][left_index[1]] == 1 and node.left_child is None:
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

    return trees
    
    
def pour_water(trees: array, values: array) -> array:
    path = []
    def traverse(node: Node):
        values[node.row][node.col] = 2
        coord = (node.row, node.col)
        if coord not in path:
            path.append(coord)

        node.visited = True
        if node.left_child is not None and not node.left_child.visited:
            traverse(node.left_child)
        if node.right_child is not None and not node.right_child.visited:
            traverse(node.right_child)
        if node.bottom_child is not None and not node.bottom_child.visited:
            traverse(node.bottom_child)

    for tree in trees:
        traverse(tree)

    return path

    
class PercolationDemo(Scene):
    
    def construct(self):
        values_str = []
        for i in range(len(values)):
            chars = []
            for j in range(len(values[i])):
                chars.append(str(values[i][j]))
            values_str.append(chars)
        print(values_str)
        table = Table(values_str)

        table = table.scale_to_fit_height(config.frame_height)
        scale_x = config.frame_width/table.width
        scale_y = config.frame_height/table.height
        scale = min(scale_x, scale_y)
        table = table.scale(scale)
        
        scale_ratio = scale_x / scale_y
        cell_scale = 1.0 / scale_ratio - 0.05
        self.add(table)

        self.play(table.create())

        print("Path length: ", len(path))
        for coord in path:
            shifted_coord = (coord[0] + 1, coord[1] + 1)
            highlight = table.get_highlighted_cell(shifted_coord, color=None)
            highlight.scale(cell_scale)
            table.add_to_back(highlight)
            self.play(highlight.animate.set_color(GREEN), run_time = 0.1) 

        self.wait()

values = build_table(10, 10, percolation_value = 0.5)

render_table(values)
trees = build_trees(values)
path = pour_water(trees, values)
render_table(values)

#data = np.random.randint(3, size = (10, 10))

cmap = colors.ListedColormap(['white', 'grey', 'green'])

fig, ax = plt.subplots()
ax.imshow(values, cmap=cmap)

# draw gridlines
ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=1)
ax.set_xticks(np.arange(-.5, 10, 1))
ax.set_yticks(np.arange(-.5, 10, 1))

plt.show()
            
