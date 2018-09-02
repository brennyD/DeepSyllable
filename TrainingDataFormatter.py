###########################
#Program written by Brendan DeMilt
#Formats pre-Calculated word-syllable combinations into usable training data
#for the neural net
#Original Syllable data found at http://delphiforfun.org/programs/syllables.htm
###########################
import random

Input = open("Syllables.txt", "r")
output = open("Training_Data.txt", "w+")

############
#MAXIMUM WORD LENGTH: 16
#LARGEST SYLLABLE COUNT: 7
############


#In order to increase diversity of data, I'm shuffling the order of the data
#entries

shuffleList = Input.readlines()
random.shuffle(shuffleList)

for text in shuffleList:
    arr = text.split("=")

    #Padding words under 16 letters with spaces
    while len(arr[0]) < 16:
        arr[0] += " "
    
    sylCount = arr[1].count('-') + 1
        
    output.write(arr[0] + "-" + str(sylCount) + "\n")

output.close()



