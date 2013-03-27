import itertools
import time

def getPrimeFactors(prime = 0):
  """
    Assigns a list of the prime factors if there excist any to the list argument
  """
  if prime % 2 == 0 or prime % 3 == 0:
    return []
  tmpProduct = 1
  product = 1
  counter = 1
  list = []
  while counter != prime:
    if counter % 2 != 0 and counter % 3 != 0:
      list.append(counter)
    counter += 1
  for i in range(len(list)):
     setTmp = set(itertools.combinations(list, i))

  return list
