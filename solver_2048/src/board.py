'''
Created on Mar 14, 2014

@author: samshuster
'''
import random
import collections
import copy

DEAD_VALUE = 0
DEFAULT_VALUES = collections.OrderedDict()
DEFAULT_VALUES[0.9] = 2
DEFAULT_VALUES[1] = 4
DEFAULT_MULTIPLIER = 2

class GameOverException(Exception):
    pass

class Board(object):
    '''
    classdocs
    '''
    LEFT = "a"
    RIGHT = "d"
    DOWN = "s"
    UP = "w"

    def __init__(self, size = 4):
        self.directionMapping = {self.LEFT:self.move_left, self.RIGHT:self.move_right,self.DOWN:self.move_down,self.UP:self.move_up}
        self.board = []
        self.history = []
        self.score = 0
        self.highest_tile = 0
        self.empty_squares = []
        self.size = size
        for outer in range(size):
            self.board.append([])
            for inner in range(size):
                newSquare = Square()
                self.board[outer].append(newSquare)
                self.empty_squares.append(newSquare)
        self.add_random()
        self.add_random()
        
    def make_move(self, direction, add = True, non_random = False):
        self.history.append((str(self.score)+"\n"+str(self)))
        change = self.directionMapping[direction]()
        if change:
            try:
                if add:
                    if non_random:
                        self.add_non_random()
                    else:
                        self.add_random()
            except GameOverException as e:
                print "Game Over!"
                exit()
        return change
        
    def move_left(self):
        change = False
        for row in self.board:
            old_row = copy.copy(map(lambda x: str(x),row))
            count = self.size
            ind = 0
            while ind < count:
                el = row[ind]
                #print row, el, bool(el), ind, count, str(el) == str(row[ind-1])
                if not el:
                    rem = row.pop(ind)
                    row.insert(self.size-1,rem)
                    ind -= 1
                    count -= 1
                elif (ind > 0 and str(el) == str(row[ind-1]) 
                      and not el.updated_flag and not row[ind-1].updated_flag):
                    row.pop(ind-1)
                    self.double_square(row[ind-1])
                    newSquare = Square()
                    row.insert(self.size-1,newSquare)
                    self.empty_squares.append(newSquare)
                    ind -= 1
                    count -= 1
                ind+=1
            if old_row != map(lambda x: str(x),row):
                change = True
            self.reset(row)
        return change
                
    def move_right(self):
        change = False
        for row in self.board:
            old_row = copy.copy(map(lambda x: str(x),row))
            count = -1
            ind = self.size - 1
            while ind > count:
                el = row[ind]
                #print row, el, bool(el), ind, count
                if not el:
                    rem = row.pop(ind)
                    row.insert(0,rem)
                    ind += 1
                    count += 1
                elif (ind < self.size-1 and str(el) == str(row[ind+1]) 
                      and not el.updated_flag and not row[ind+1].updated_flag):
                    row.pop(ind+1)
                    self.double_square(row[ind])
                    newSquare = Square()
                    row.insert(0,newSquare)
                    self.empty_squares.append(newSquare)
                    ind += 1
                    count += 1
                ind-=1 
            if old_row != map(lambda x: str(x),row):
                change = True
            self.reset(row)
        return change      
    
    def double_square(self, square):
        square.double()
        val = int(str(square))
        self.score += val
        if val > self.highest_tile:
            self.highest_tile = val
    
    def reset(self, arr):
        for el in arr:
            el.reset()
    
    def move_down(self):
        self.transpose()
        change = self.move_right()
        self.transpose()
        return change
        
    def move_up(self):
        self.transpose()
        change = self.move_left()
        self.transpose()
        return change
        
    def transpose(self):
        ret = []
        for col in zip(*self.board):
            new_row = []
            for el in col:
                new_row.append(el)
            ret.append(new_row)
        self.board = ret          
    
    def add_random(self):
        if len(self.empty_squares) == 0:
            raise GameOverException()
        num = random.random()
        for prob in DEFAULT_VALUES:
            if num < prob:
                val = DEFAULT_VALUES[prob]
                break
        square_ind = random.randrange(0,len(self.empty_squares))
        square = self.empty_squares.pop(square_ind)
        square.set_value(val)
        
    def add_non_random(self):
        if len(self.empty_squares) == 0:
            raise GameOverException()
        square = self.board[3][0]
        square.set_value(2)
        
    def board_from_array(self, arr):
        ret = []
        for row in arr:
            row_new = []
            for el in row:
                newSquare = Square(el)
                row_new.append(newSquare)
                if el == 0:
                    self.empty_squares.append(newSquare)
            ret.append(row_new)
        self.board = ret
    
    def __repr__(self):
        ret = ""
        for outer in self.board:
            for inner in outer:
                ret += str(inner) + " "
            ret += "\n"
        return ret[:-1]
        
class Square(object):
    def __init__(self, value=DEAD_VALUE):
        self.cur_value = value
        self.updated_flag = False
    
    def set_value(self, value):
        self.cur_value = value
    
    def double(self):
        self.cur_value = self.cur_value * DEFAULT_MULTIPLIER
        self.updated_flag = True
    
    def reset(self):
        self.updated_flag = False
    
    def __repr__(self):
        return str(self.cur_value)
    
    def __nonzero__(self):
        return self.cur_value != 0
    
