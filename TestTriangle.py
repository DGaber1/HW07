# -*- coding: utf-8 -*-
"""
Test suite for classifyTriangle() in Triangle.py
 
Test design strategy:
  - Equivalence partitioning: one or more tests for each output class
    (Right, Equilateral, Isoceles, Scalene, NotATriangle, InvalidInput)
  - Boundary value analysis: sides of 0, 1, 200, 201
  - Permutations: every ordering of the sides for each triangle type, so a
    bug that only affects one position (a, b or c) gets caught
  - Degenerate triangles: sum of two sides exactly equals the third
  - Invalid types: floats, strings, None
 
Each test name starts with an ID (T01, T02, ...) so results map straight
into the test report table.
"""
 
import unittest
 
from Triangle import classifyTriangle
 
 
class TestTriangles(unittest.TestCase):
 
    # ---------- Right triangles ----------
    def testT01_RightA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')
 
    def testT02_RightB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')
 
    def testT03_RightC(self):
        self.assertEqual(classifyTriangle(4, 5, 3), 'Right', '4,5,3 is a Right triangle')
 
    def testT04_RightD(self):
        self.assertEqual(classifyTriangle(6, 8, 10), 'Right', '6,8,10 is a Right triangle')
 
    def testT05_RightE(self):
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right', '5,12,13 is a Right triangle')
 
    def testT06_RightF(self):
        self.assertEqual(classifyTriangle(13, 5, 12), 'Right', '13,5,12 is a Right triangle')
 
    # ---------- Equilateral triangles ----------
    def testT07_EquilateralMin(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')
 
    def testT08_EquilateralMid(self):
        self.assertEqual(classifyTriangle(50, 50, 50), 'Equilateral', '50,50,50 should be equilateral')
 
    def testT09_EquilateralMax(self):
        self.assertEqual(classifyTriangle(200, 200, 200), 'Equilateral', '200,200,200 should be equilateral')
 
    # ---------- Isoceles triangles ----------
    def testT10_IsocelesAB(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isoceles', '2,2,3 should be isoceles')
 
    def testT11_IsocelesAC(self):
        self.assertEqual(classifyTriangle(2, 3, 2), 'Isoceles', '2,3,2 should be isoceles')
 
    def testT12_IsocelesBC(self):
        self.assertEqual(classifyTriangle(3, 2, 2), 'Isoceles', '3,2,2 should be isoceles')
 
    def testT13_IsocelesLarge(self):
        self.assertEqual(classifyTriangle(5, 5, 8), 'Isoceles', '5,5,8 should be isoceles')
 
    # ---------- Scalene triangles ----------
    def testT14_ScaleneA(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene', '4,5,6 should be scalene')
 
    def testT15_ScaleneB(self):
        self.assertEqual(classifyTriangle(6, 5, 4), 'Scalene', '6,5,4 should be scalene')
 
    def testT16_ScaleneC(self):
        self.assertEqual(classifyTriangle(7, 9, 11), 'Scalene', '7,9,11 should be scalene')
 
    def testT17_ScaleneD(self):
        self.assertEqual(classifyTriangle(5, 7, 4), 'Scalene', '5,7,4 should be scalene')
 
    # ---------- Not a triangle (triangle inequality violated) ----------
    def testT18_NotATriangleDegenerate(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1,2,3 is degenerate (1+2=3)')
 
    def testT19_NotATriangleC(self):
        self.assertEqual(classifyTriangle(1, 1, 3), 'NotATriangle', '1,1,3 is not a triangle')
 
    def testT20_NotATriangleB(self):
        self.assertEqual(classifyTriangle(1, 3, 1), 'NotATriangle', '1,3,1 is not a triangle')
 
    def testT21_NotATriangleA(self):
        self.assertEqual(classifyTriangle(3, 1, 1), 'NotATriangle', '3,1,1 is not a triangle')
 
    def testT22_NotATriangleLong(self):
        self.assertEqual(classifyTriangle(10, 2, 3), 'NotATriangle', '10,2,3 is not a triangle')
 
    def testT23_NotATriangleDegenerateB(self):
        self.assertEqual(classifyTriangle(2, 5, 3), 'NotATriangle', '2,5,3 is degenerate (2+3=5)')
 
    # ---------- Invalid input: lower bound (must be > 0) ----------
    def testT24_ZeroA(self):
        self.assertEqual(classifyTriangle(0, 1, 1), 'InvalidInput', 'a=0 is invalid')
 
    def testT25_ZeroB(self):
        self.assertEqual(classifyTriangle(1, 0, 1), 'InvalidInput', 'b=0 is invalid')
 
    def testT26_ZeroC(self):
        self.assertEqual(classifyTriangle(1, 1, 0), 'InvalidInput', 'c=0 is invalid')
 
    def testT27_NegativeA(self):
        self.assertEqual(classifyTriangle(-1, 2, 2), 'InvalidInput', 'a=-1 is invalid')
 
    def testT28_NegativeB(self):
        self.assertEqual(classifyTriangle(2, -1, 2), 'InvalidInput', 'b=-1 is invalid')
 
    def testT29_NegativeC(self):
        self.assertEqual(classifyTriangle(2, 2, -1), 'InvalidInput', 'c=-1 is invalid')
 
    # ---------- Invalid input: upper bound (must be <= 200) ----------
    def testT30_TooLargeA(self):
        self.assertEqual(classifyTriangle(201, 100, 100), 'InvalidInput', 'a=201 is invalid')
 
    def testT31_TooLargeB(self):
        self.assertEqual(classifyTriangle(100, 201, 100), 'InvalidInput', 'b=201 is invalid')
 
    def testT32_TooLargeC(self):
        self.assertEqual(classifyTriangle(100, 100, 201), 'InvalidInput', 'c=201 is invalid')
 
    def testT33_AllTooLarge(self):
        self.assertEqual(classifyTriangle(300, 300, 300), 'InvalidInput', '300,300,300 is invalid')
 
    # ---------- Invalid input: non-integer types ----------
    def testT34_FloatA(self):
        self.assertEqual(classifyTriangle(1.5, 2, 3), 'InvalidInput', 'float input is invalid')
 
    def testT35_FloatB(self):
        self.assertEqual(classifyTriangle(3, 4.0, 5), 'InvalidInput', 'float input is invalid')
 
    def testT36_StringA(self):
        self.assertEqual(classifyTriangle('3', 4, 5), 'InvalidInput', 'string input is invalid')
 
    def testT37_NoneC(self):
        self.assertEqual(classifyTriangle(3, 4, None), 'InvalidInput', 'None input is invalid')
 
    # ---------- Boundary valid cases ----------
    def testT38_BoundaryMaxIsoceles(self):
        self.assertEqual(classifyTriangle(200, 200, 1), 'Isoceles', '200,200,1 is a valid isoceles triangle')
 
    def testT39_BoundaryMaxScalene(self):
        self.assertEqual(classifyTriangle(200, 199, 2), 'Scalene', '200,199,2 is a valid scalene triangle')
 
 
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
