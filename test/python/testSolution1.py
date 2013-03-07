#! /usr/bin/env python

import unittest
from eulerFunctions import multiples_of_3_and_5

class TestNaturalNumbers(unittest.TestCase):

  def setUp(self):
    self.number = 1000
 
  def test_findNaturalNumbersWith3And5AsMultiples(self):
    list = multiples_of_3_and_5.findNaturalNumbersWith3And5AsMultiples(self.number)
    for item in list:
      self.assertTrue(multiples_of_3_and_5.testNaturalNumbersWith3And5AsMultiples(item))

  def test_NaturalNumbersNotMultiplesOf3And5(self):
    list = [4, 7, 8]
    for item in list:
      self.assertFalse(multiples_of_3_and_5.testNaturalNumbersWith3And5AsMultiples(item))

  def test_sumOfNumbersMultiplesOf3And5(self):
    list = multiples_of_3_and_5.findNaturalNumbersWith3And5AsMultiples(self.number)
    localSum = 0
    for item in list:
      localSum += item

    self.assertEqual(multiples_of_3_and_5.mySum(list), localSum)
    print "Sum is " + str(localSum)

if __name__ == "__main__":
  unittest.main()
