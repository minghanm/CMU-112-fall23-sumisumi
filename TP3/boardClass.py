'''
Board Class: 
each level is a new example of the board class,
it will contain information of the size of the board, 
the number of Sumi on the board, the goal to win the game,
the limited steps to reach the goal, and an additional target
score for the user to accomplish 
'''

import random

class Board:
    def __init__(self, row, col, numOfSumi, goal, steps, score):
        #the sumi list of all sumi charaters
        self.sumiTypes = ["Tokage", "Nyankoyaki", "Nonbi", "Neko", "Hokori", "Jinbesan", "Mikanboya", "Necolon", "Penguin", "Shirokuma"]
        #board size
        self.row = row
        self.col = col
        #number of Sumi
        self.numOfSumi = numOfSumi
        #initialize the random picked sumi in this level, and target sumi in this level
        self.selectedSumi = []
        self.goalSumi = None
        #requirements and goals
        self.goalNum = goal
        self.goalScore = score
        self.steps = steps

        #initialize board without characters
        self.board = [([None] * self.col) for row in range(self.row)]
        
    def __repr__(self):
        return f"this is a {self.row} * {self.col} board with {self.numOfSumi} characters"
    
    #randomly pick sumi characters and target sumi character
    def selectSumi(self):
        while len(self.selectedSumi) < self.numOfSumi:
            selected = self.sumiTypes[random.randint(0, len(self.sumiTypes)-1)]
            if selected not in self.selectedSumi:
                self.selectedSumi.append(selected)
        self.goalSumi = random.choice(self.selectedSumi)
        return self.selectedSumi
    
    def loadWall(self, row, col):
        if self.board[row][col] == None:
            self.board[row][col] = "wall"

    #randomly generate sumi characters onto the empty board
    def loadSumi(self, row, col):
        sumi = random.choice(self.selectedSumi)
        if self.board[row][col] == None:
            self.board[row][col] = sumi
    
