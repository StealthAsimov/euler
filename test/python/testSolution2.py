#! /usr/bin/env python

import unittest
from eulerFunctions import fibonacci

class TestFibonacciNumbers(unittest.TestCase):

  def setUp(self):
    self.fibonacciNumbers = 4000000 
 
  def test_findFibonacciNumbers(self):
    list = []
    tmpSum = 0
    fibonacci.findFibonacciNumbers(rangeNr = self.fibonacciNumbers, list = list)
    self.assertTrue(list[0] < self.fibonacciNumbers)
    for item in list:
      if item % 2 == 0:
        tmpSum += item
    print tmpSum

if __name__ == "__main__":
  unittest.main()
