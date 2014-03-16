'''
Created on Mar 14, 2014

@author: samshuster
'''
import collections
import copy
from board import Board
import random

class BoardSolver(object):
    
    def __init__(self, board):
        self.board = board
        self.cur_score = self.evaluate(self.board)
        
    def evaluate(self, board):
        empty = len(board.empty_squares)
        score,num_pairs = self.score_board(board.board)
        board.transpose()
        score2,num_pairs2 = self.score_board(board.board)
        board.transpose()
        scoref = 2*empty + 4*score + 5*num_pairs + 5*num_pairs2
        return scoref
        
    def score_board(self, b):
        score = 0
        num_pairs = 0
        for row in b:
            temp = collections.defaultdict(int)
            for el in row:
                score += int(str(el))
                if str(el) != "0":
                    temp[str(el)] += 1
            for v in temp.values():
                if v > 1:
                    num_pairs += 1
        return score, num_pairs
        
    def score_helper(self, func, b):
        if not func():
            return 0
        else:
            return self.evaluate(b)
    
    def find_best_move_helper(self, b, depth):
        if depth == 0:
            return b.score,b
        max_board = None
        max_score = -2
        directions = self.board.directionMapping.keys()
        random.shuffle(directions)
        for movement in directions:
            tempboard = copy.deepcopy(self.board)
            if not tempboard.make_move(movement,False):
                score = -1
            else:
                try:
                    tempboard.add_random()
                except:
                    score = -1
                else:
                    score,_ = self.find_best_move_helper(tempboard,depth-1)
            if score > max_score:
                max_score = score
                max_board = tempboard
        return max_score,max_board
        
    def find_best_move(self, depth = 1):
        if len(self.board.empty_squares) > 2:
            depth = 1
        else:
            depth = 2
        max_score, max_board = self.find_best_move_helper(self.board,depth)
        if max_score == -1:
            return False
        self.board = max_board
        self.cur_score = self.board.score
        return True

    
    def play(self):
        while(self.find_best_move()):
            print self.board.score
            print self.board
            raw_input()

            
    def play_automatic(self):
        winner = False
        while(self.find_best_move()):
            if(self.board.highest_tile > 1000):
                winner = True
        print self.board.score
        print self.board
        if winner:
            print "WINNER:"
            f = open("out1000.txt",'w')
            for prev in self.board.history:
                f.write(prev)
                f.write("\n")
            return True
            
for i in range(1000):
    bs = BoardSolver(Board())
    if bs.play_automatic():
        break
