'''
Created on Mar 14, 2014

@author: samshuster
'''
import unittest
import random
from board import Board, Square


class Test(unittest.TestCase):

    def testBoardFromArray(self):
        arr = [[1,2,4,3],[0,0,2,3],[2,1,4,3],[2,3,4,9]]
        b = Board()
        b.board_from_array(arr)
        prop = [[Square(1),Square(2),Square(4),Square(3)],
                [Square(),Square(),Square(2),Square(3)],
                [Square(2),Square(1),Square(4),Square(3)],
                [Square(2),Square(3),Square(4),Square(9)]]
        b2 = Board()
        b2.board = prop
        self.assertEqual(str(b), str(b2))

    def testMoveLeft(self):
        b = Board()
        b.board_from_array([[0,2,4,3],[0,0,2,3],[2,1,0,3],[2,0,0,0]])
        b.move_left()
        b2 = Board()
        b2.board_from_array([[2,4,3,0],[2,3,0,0],[2,1,3,0],[2,0,0,0]])
        self.assertEqual(str(b),str(b2))
        
    def testMoveLeft2(self):
        b = Board()
        b.board_from_array([[0,0,0,3],[2,0,0,2],[0,0,3,0],[2,0,2,2]])
        b.move_left()
        b2 = Board()
        b2.board_from_array([[3,0,0,0],[4,0,0,0],[3,0,0,0],[4,2,0,0]])
        self.assertEqual(str(b),str(b2))
        
    def testMoveRight(self):
        b = Board()
        b.board_from_array([[0,2,2,3],[0,0,2,2],[2,1,0,3],[2,2,2,2]])
        b.move_right()
        b2 = Board()
        b2.board_from_array([[0,0,4,3],[0,0,0,4],[0,2,1,3],[0,0,4,4]])
        self.assertEqual(str(b),str(b2))  
        
    def testMoveRight2(self):
        b = Board()
        b.board_from_array([[0,0,0,3],[2,0,0,2],[0,0,3,0],[2,0,2,2]])
        b.move_right()
        b2 = Board()
        b2.board_from_array([[0,0,0,3],[0,0,0,4],[0,0,0,3],[0,0,2,4]])
        self.assertEqual(str(b),str(b2))
        
    def testTranspose(self):
        b = Board()
        b.board_from_array([[0,0,0,3],[2,0,0,2],[0,0,3,0],[2,0,2,2]])
        b.transpose()
        b2 = Board()
        b2.board_from_array([[0,2,0,2],[0,0,0,0],[0,0,3,2],[3,2,0,2]])
        self.assertEqual(str(b),str(b2))
        
    def testMoveDown(self):
        b = Board()
        b.board_from_array([[0,0,0,3],[2,0,0,2],[0,0,3,0],[2,0,2,2]])
        b.move_down()
        b2 = Board()
        b2.board_from_array([[0,0,0,0],[0,0,0,0],[0,0,3,3],[4,0,2,4]])
        self.assertEqual(str(b),str(b2))
        
    def testMoveUp(self):
        b = Board()
        b.board_from_array([[0,0,0,3],[2,0,0,2],[0,0,3,0],[2,0,2,2]])
        b.move_up()
        b2 = Board()
        b2.board_from_array([[4,0,3,3],[0,0,2,4],[0,0,0,0],[0,0,0,0]])
        self.assertEqual(str(b),str(b2))
        
    def testAddRandom(self):
        random.seed(0)
        b = Board()
        b.move_left()
        b.add_random()
        b.move_right()
        b2 = Board()
        b2.board_from_array([[0,0,0,2],[0,0,0,2],[0,0,0,2],[0,0,0,0]])
        self.assertEqual(str(b),str(b2))
        
    def testAddRandom2(self):
        random.seed(0)
        b = Board()
        b.make_move(b.LEFT)
        b.make_move(b.RIGHT)
        b2 = Board()
        b2.board_from_array([[0,0,0,2],[2,0,0,2],[0,0,0,2],[0,0,0,0]])
        self.assertEqual(str(b),str(b2))
        
    def testNoMove(self):
        b = Board()
        b.board_from_array([[0,0,0,3],[0,0,0,2],[0,0,0,0],[0,0,0,0]])
        ans = b.make_move(b.RIGHT)
        self.assertEqual(ans,False)
        
    def testTricky(self):
        b = Board()
        b.board_from_array([[0,0,0,2],[0,0,0,2],[0,0,0,2],[0,0,0,2]])
        b.move_up()
        b2 = Board()
        b2.board_from_array([[0,0,0,4],[0,0,0,4],[0,0,0,0],[0,0,0,0]])
        self.assertEqual(str(b),str(b2))
        b.board_from_array([[0,0,0,4],[0,0,0,2],[0,0,0,2],[0,0,0,2]])
        b.move_up()
        b2.board_from_array([[0,0,0,4],[0,0,0,4],[0,0,0,2],[0,0,0,0]])
        self.assertEqual(str(b),str(b2))
        
    def testDoubleChange(self):
        b = Board()
        b.board_from_array([[0,0,0,8],[0,0,0,4],[0,0,0,0],[0,0,0,4]])
        b.move_down()
        b2 = Board()
        b2.board_from_array([[0,0,0,0],[0,0,0,0],[0,0,0,8],[0,0,0,8]])
        self.assertEqual(str(b),str(b2))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testMoveLeft']
    unittest.main()