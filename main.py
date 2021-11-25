import random


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
    for j in range(0, len(values[0])):
        cell_value = values[0][j]
        if cell_value == 1:
            trees.append(Node(0, j, 1))

    def bt(node: Node, depth: int):
        left_index = (node.row, node.col - 1)
        right_index = (node.row, node.col + 1)
        bottom_index = (node.row + 1, node.col)

        # print(node, "L: ", left_index, "R: ", right_index, "B: ", bottom_index)

        if node.left_child is None and left_index[0] >= 0:
            if values[left_index[0]][left_index[1]] == 1:
                node.left_child = Node(left_index[0], left_index[1], 1)
                node.left_child.right_child = node
                bt(node.left_child, depth)
        if node.right_child is None and right_index[1] < cols:
            if values[right_index[0]][right_index[1]] == 1:
                node.right_child = Node(right_index[0], right_index[1], 1)
                node.right_child.left_child = node
                bt(node.right_child, depth)
        if bottom_index[0] < rows:
            if values[bottom_index[0]][bottom_index[1]] == 1:
                node.bottom_child = Node(bottom_index[0], bottom_index[1], 1)
                bt(node.bottom_child, depth + 1)
    
    print("Created", len(trees), "trees")
    for tree in trees:
        bt(tree, 0)
    
    
def pour_water():

    def traverse(node: Node):
        values[node.row][node.col] = 'W'
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
render_table()
build_trees(rows, cols)
pour_water()
render_table()
            
