# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
    
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(7, 9, 11), 'Scalene', '7, 9, 11 should be Scalene')

    def testIscscelesTriangleA(self):
        self.assertEqual(classifyTriangle(5, 5, 7), 'Iscosceles', '5, 5, 7 should be Iscsceles')

    def testIscoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(8, 6, 8), 'Isosceles', '8, 6, 8 should be Isosceles')

    def testInvalidTriangle(self):
        self.assertEqual(classifyTriangle(1, 2, 4), 'Invalid', '1, 2, 4 is not a valid triangle')

    def testInvalidTriangleB(self):
        self.assertEqual(classifyTriangle(0, 3, 3), 'Invalid', '0, 3, 3 is not a valid triangle')

    def testNegetiveSideLengths(self):
        self.assertEqual(classifyTriangle(-2, 3, 4), 'Invalid', '-2, 3, 4 has negetive side lengths')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

