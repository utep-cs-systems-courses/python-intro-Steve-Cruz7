#! /usr/bin/env python3

import sys      #enables command line arguments
import re       #regular expression stuff
import os       #used to check if file exists

#set input and output files
if len(sys.argv) != 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

textFile = sys.argv[1]
outputFile = sys.argv[2]

#checking to see if text file exists
if not os.path.exists(textFile):
    print("text file input %s doesn't exist!! Exiting" % textFile)
    exit()

if not os.path.exists(outputFile):
   print("Given output file does not exist, creating file...") 
   output = open(outputFile, "w")
else:
   print("Given file already exist, overwriting file...")
   output = open(outputFile, "w")   #I think this will overwrite the file

#starting dictionary
dictionary = {}

#starting algo to count words
with open(textFile, 'r') as inputFile:
    for line in inputFile:
        # taking out newLine characters
        line = line.strip()
        #split line on whitespace and punctuation
        line  = re.split("[-!:;.,'?\s \t]", line)
        for word in line:
            if word.lower() in dictionary:
                dictionary[word.lower()] += 1
            else:
                dictionary[word.lower()] = 1
#testing
dictionary.pop("")  #Still dont no why split  was creating literal empty string
sortedDictionary = dict(sorted(dictionary.items()))  #Sorting it alphabetically 

for word in sortedDictionary:
    output.write(word)
    output.write(" ")
    output.write(str(dictionary[word]))
    output.write("\n")
    
        
