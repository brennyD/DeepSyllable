This project aims to successfullly train a neural network to accurately and precisely count the number of syllables in english words, without any prior knowledge of english grammatical rules

It's written in Python and uses TensorFlow for neural network models

To begin, I downloaded Syllables.txt from http://delphiforfun.org/programs/syllables.htm which was suitable for training ym model. This file includes approximately 42443 words and their sylable counts, some inputted manually while others were calculated using a program following grammatical laws. In order to put the data into a more serializable form, I converted the file to Training_Data.txt, which removes all symbols leaving only the word with the syllable count next to it, calculated by counting the amount of hyphens in the word separation and adding one. 

