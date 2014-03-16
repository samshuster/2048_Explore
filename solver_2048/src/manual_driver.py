'''
Created on Mar 14, 2014

@author: samshuster
'''
from board import Board

b = Board()
print b
move = raw_input()
while(True):
    try:
        b.make_move(move,non_random=True)
    except KeyError:
        pass
    else:
        print b.score
        print b
    move = raw_input()

