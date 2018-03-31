# -*- coding: UTF-8 -*-
"""Employee Email Script.
This module allows us to evaluate the text of a csv file. It displays word count, sentence count, letter count, and average sentence length
"""
#name of file to evaluate-stored in same location as main.py file
filename = "paragraph_2.txt"
#variables to store counts of lines, words and charactors
numlines = 0
numwords = 0
numchars = 0
#loops through file and starts counting
with open(filename, 'r') as file:
    for line in file:
        #create list for words
        wordslist = line.split()
        numlines += 1
        numwords += len(wordslist) #just get length of worldsist list
        numchars += len(line) # getting length of line on each iteration will be number of characters
# count lines, sentences, and words of a text file
# set all the counters to zero
#setting variables all in single line instead of 4 lines
lines, blanklines, sentences, words = 0, 0, 0, 0
try:
  #reading file to find lines, blanklines, sentences, and words
  textf = open(filename, 'r')
  #error check
except IOError:
  print ('Cannot open file %s for reading' % filename)
  import sys
  sys.exit(0)
# reads one line at a time and starts counting
for line in textf:
  lines += 1
  if line.startswith('\n'):
    blanklines += 1
  else:
    # assuming each sentence ends with . or ! or ?
    # counting these characters
    sentences += line.count('.') + line.count('!') + line.count('?')
    # create a list of words
    # use None to split at any whitespace regardless of length
    # so double space counts as one space
    tempwords = line.split(None)
    # word total count
    words += len(tempwords)
#closes textf variable to finish counting    
textf.close()
#prints heading line
print("Paragraph Analysis")
#prints line space
print ('-' * 25)
#prints "Approximate word count" and appends the count of words
print ("Approximate Word Count: ", words)
#prints ""Approximate Sentence Count:" and appends the count of sentances(the count of sentence ending puncuation)
print ("Approximate Sentence Count: ", sentences)
#print "Average Letter Count:" and appends the solution of characters divided by words to get the average letter count
print("Average Letter Count:", numchars/words)
#prints "average sentence length" and appends the solution of words divided by sentences to get the average sentence length
print("Average Sentence Length:", words/sentences)