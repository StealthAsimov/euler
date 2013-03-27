#! /usr/bin/env python

# The prime factors of 13195 are 5, 7, 13 and 29
# What is the largest prime factor of the number 600851475143 ?

import unittest
from eulerFunctions import prime

class TestLargestPrimeFactor(unittest.TestCase):

  def setUp(self):
    self.number = 1 * 5 * 7 
    #self.number = 600851475143

  def test_findLargestPrimeFactor(self):
    list = [] # list the prime factors according to the self.number
    list = prime.getPrimeFactors(self.number)
    for item in list:
      # Check if the number is an prime number
      self.assertTrue(item % 2 != 0 and item % 3 != 0)

if __name__ == "__main__":
  unittest.main()
