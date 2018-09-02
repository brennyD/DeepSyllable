###########################
#Program written by Brendan DeMilt
#Formats pre-Calculated word-syllable combinations into usable training data
#for the neural net
#Original Syllable data found at http://delphiforfun.org/programs/syllables.htm
###########################
import random

Input = open("Syllables.txt", "r")
output = open("Training_Data.txt", "w+")


#The longest word length found in this training list will be the number of
#input neurons
longestWord = ''

#The largest syllable count will be the number of possible outputs
biggestSyllable = -1


#In order to increase diversity of data, I'm shuffling the order of the data
#entries

shuffleList = Input.readlines()
random.shuffle(shuffleList)

for text in shuffleList:
    arr = text.split("=")
    sylCount = arr[1].count('-')+1

    if sylCount > biggestSyllable:
        biggestSyllable = sylCount
        
    if len(arr[0]) > len(longestWord):
        longestWord = arr[0]
        
    output.write(arr[0] + " " + str(sylCount) + "\n")

output.write(str(len(longestWord)) + " " + str(biggestSyllable))

output.close()



