import sys 

class Node():
    def __init__ (self, state, parent, action):
        self.state = state 
        self.parent = parent
        self.action = action

# rem lifo (last in first out)??
class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)
    
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier) # return T if any else F
    
    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception('empty')
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
    
# rem fifo( first in first out )
class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception('empty')
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
        
class Maze():
    
    def __init__(self, filename):
        with open(filename) as f:
            contents = f.read()

        if contents.count('A') != 1:
            raise Exception('have only one start point yk')
        if contents.count('B') != 1:
            raise Exception('also have one end point too')
        
        contents = contents.splitlines()
        self.h = len(contents) # height
        self.w = max(len(line) for line in contents) #width

        self.walls = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                try:
                    if contents[i][j] == 'A':
                        self.start = (i,j)
                        row.append(False)
                    elif contents[i][j] == 'B':
                        self.goal = (i,j)
                        row.append(False)
                    elif contents[i][j] == ' ':
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)
        
        self.solution = None
                        