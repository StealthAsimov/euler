#! /usr/bin/env python

import types

def findNaturalNumbersWith3And5AsMultiples(number = 10):
  list = []
  for i in range(number):
    if i == 0:
      continue
    elif i % 3 == 0:
      list.append(i)
    elif i % 5 == 0:
      list.append(i)
  return list

def testNaturalNumbersWith3And5AsMultiples(number = None):
  if not isinstance(number, int):
    return False
  elif number % 3 == 0:
    return True
  elif number % 5 == 0:
    return True
  else:
    return False

def mySum(list):
  return sum(list)
