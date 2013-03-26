def findFibonacciNumbers(prevNumber = 0, currentNumber = 0, rangeNr = 10, list = []):
  if currentNumber == 0:
    list.append(currentNumber + findFibonacciNumbers(currentNumber, currentNumber + 1, rangeNr, list))
  elif (prevNumber + currentNumber + currentNumber) < rangeNr:
    list.append(currentNumber + findFibonacciNumbers(currentNumber, currentNumber + prevNumber, rangeNr, list))
  
  return currentNumber
