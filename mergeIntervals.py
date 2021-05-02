#!/usr/bin/python

import sys
import signal
import time



intervalsToMerge = []

#Adds element to certain list
def addToListIfNotExisting(arg, listToUpdate):
  if listToUpdate.count(arg) <= 0:
    listToUpdate.append(arg)

#Adds element to certain dictionary   
def addToDict(index, message, value, dictonary):
  dictonary.update({"Intervall " + str(index) + message: value}) 

#Handles standard errors
def errorHandler(error, errorArgs, errorDict):
  if error == True:
    try: 
      raise TypeError('Intervalls ' +  str(errorArgs) + ' had the following wrong formats: ' + str(errorDict))
    except TypeError as error:
      print('Type error occured: ', error)
      return False
  else:
    return True  

#Returns offset for point gettes etc.  
def getOffsetForPoint(interval, index, offset, resetindex, errorDict, errorArgs):
  try:
    type(int(interval[index+offset+1]))
  except ValueError:
    return offset
  except IndexError:
    return indexErrorHandler(resetindex, errorArgs, errorDict , True)
  else:
    try:
      while type(int(interval[index+offset])) is int:
        offset += 1
    except IndexError:
      return indexErrorHandler(resetindex, errorArgs, errorDict , True) 
    except ValueError:    
      return (offset - 1)

#Handles index errors
def indexErrorHandler(resetindex, errorArgs, errorDict , error):
  addToDict(resetindex, ' Final sign', 'was forgotten!' + 'Should have been "]"', errorDict)
  addToListIfNotExisting(resetindex, errorArgs)
  errorHandler(error, errorArgs, errorDict)
  appendIntervalIfValid(resetindex)
  return 0      

#Returns the startpoint of an interval
def getStartPoint(interval, index, offset):
  resultToConvert = ''
  if offset == 0:
    return int(interval[index])
  else:
    #Offset+1 because offset only bears shift and otherwise first digit is lost
    for i in range(0, offset+1):
        resultToConvert += interval[index+i]
    return int(resultToConvert)

#Returns the endpoint of an interval
def getEndPoint(interval, index):
  i = 0
  resultToConvert = ''
  try:
    while type(int(interval[index+i])) is int:
      resultToConvert += interval[index+i]
      i+= 1
  except ValueError:
    return int(resultToConvert)
    

#Validates user inputs sign by sign  
def validateInterval(interval, index):
  start = 0
  end = 0
  offset = 0
  endOffset = 0
  error = False
  errorDict = {}
  errorArgs = []
  print('Interval length: ' + str(len(interval)))
  print ('Interval', index, ': ', interval)
  for z in range(0, len(interval)):
    if z == 0:
      if interval[z] != '[':
        error = True
        addToDict(index, ' First Sign', 'was not "["!', errorDict)
        addToListIfNotExisting(index, errorArgs)
    if z == 1:
      try:
        type(int(interval[z]))
        offset = getOffsetForPoint(interval, z, offset, index, errorDict, errorArgs)
        start = getStartPoint(interval, z, offset)
      except ValueError:
        error = True
        addToDict(index, ' Starting Point', 'was not a Number!', errorDict)
        addToListIfNotExisting(index, errorArgs)
    if (z + offset) == 2 + offset:
      try:
        if interval[z + offset] != ',':
          error = True
          addToDict(index, ' Second Sign', 'was not ","!', errorDict)
          addToListIfNotExisting(index, errorArgs)
      except IndexError:
        return bool(indexErrorHandler(index, errorArgs, errorDict , True))  
    if (z + offset) == 3 + offset:
      try:
        if interval[z + offset] != ' ':
          error = True
          addToDict(index, ' Third Sign', 'was not " "!', errorDict)
          addToListIfNotExisting(index, errorArgs)
      except IndexError:
        return bool(indexErrorHandler(index, errorArgs, errorDict , True))     
    if (z + offset) == 4 + offset:        
      try:
        type(int(interval[z + offset]))
        endOffset = getOffsetForPoint(interval, z, offset, index, errorDict, errorArgs)
        #Minus 2 to set start digit for end point correctly
        end = getEndPoint(interval, (z+offset))
        if end <= start:
          error = True
          addToDict(index, ' EndPoint', 'was smaller or equal as StartPoint "]"!', errorDict)
      except ValueError:
        error = True
        addToDict(index, ' Ending Point', 'was not a Number!', errorDict)
        addToListIfNotExisting(index, errorArgs)
    if (z + endOffset) == 5 + endOffset:
      try:
        if interval[z + endOffset] != ']':      
          error = True
          addToDict(index, ' Last Sign', 'was not "]"!', errorDict)
          addToListIfNotExisting(index, errorArgs)
      except IndexError:
        return bool(indexErrorHandler(index, errorArgs, errorDict , True))      
  return errorHandler(error, errorArgs, errorDict)

#Appends intervals as list elements when they are valid
def appendIntervalIfValid(index):
  interval =  str(input('\nPlease Enter the ' +  str(index) + '. interval\n' 'The format would be [<starting_point>,<space><ending_point>]\n' + 'For example [1, 2]\n'))  
  if not validateInterval(interval, index):
    print('Please enter a valid interval! See error message from before\n')
    appendIntervalIfValid(index)
  else:  
    intervalsToMerge.append(interval) 

def signal_handler(sig, frame):
    print('\nYou pressed Ctrl+C!' + '\n' + 'Shutting down....')
    time.sleep(2) 
    sys.exit(0)

#Reads intervals from user inputs
def read():
  print('This is an application to merge Intervals in the style of [1, 5].')
  print('First you have to choose how many intervals you want to Merge (maximal 8) just enter a number and press enter.')
  print('Than you have to enter your intervals, just like the one before') 
  intervalsCount = None
  try:
    intervalsCount = int(input('\nHow many Intervalls should be merged if possible:\n' + 'A maximum of 8 is possible\n'))  
  except ValueError:
    print('\nYou did not enter a number!\nThe amount of Intervals to be errored and merged has to be a numeric input!\n')
    read()
  if intervalsCount is not None:  
    if intervalsCount > 8:
      print('\n' + 'The ammount of intervals you chose is ' + str(intervalsCount) + 'which is bigger than 8!\n' + 'Choose a different ammount!\n')
      read()
    elif intervalsCount < 0:
      print('\n' + 'Obviously it is not possible to have a negative ammount of intervals!' + '\n' + 'Choose a positive ammount please!\n')
      read()   
    elif intervalsCount == 1 or intervalsCount == 0:
      print('\n' + 'You should a least choose 2 intervals!\n')
      read()
    elif intervalsCount <= 8 and intervalsCount >= 2:  
      for i in range(0, intervalsCount):
        appendIntervalIfValid(int(i+1))
        
#The Merging algorithm it compares the last number of before with first number of following        
def mergeAlgorithm(intervalsToMerge, start_index = 0):
  offset = 0
  endOffset = 0
  merged = intervalsToMerge
  for i in range(0, len(merged) - 1):
    if merged[i][1] > merged[i+1][0]:
      mergedStart = merged[i][0]
      if merged[i][1] > merged[i+1][1]:
        mergedEnd = merged[i][1]
      else:
        mergedEnd = merged[i+1][1]      
      merged[i] = [mergedStart, mergedEnd]
      del merged[i+1]
      return mergeAlgorithm(merged, start_index=i)
  return merged        

#Converts string inputs to number list  
def convert():
  convertedList = []
  for current in intervalsToMerge:
    current = current[1:-1]
    convertedList.append([int(s) for s in current.split(', ')])  
  return convertedList
  
#Start the application
def main():
  signal.signal(signal.SIGINT, signal_handler)  
  read()
  intervalsToMerge.sort()
  print('Merged: \n')  
  print(str(mergeAlgorithm(convert())))
  time.sleep(5)  
  
if __name__ == '__main__':
    main()

