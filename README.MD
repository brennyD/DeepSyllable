This project aims to successfullly train a neural network to accurately and precisely count the number of syllables in english words, without any prior knowledge of english grammatical rules

It's written in Python and uses TensorFlow alongside Keras for neural network models

To begin, I downloaded Syllables.txt from http://delphiforfun.org/programs/syllables.htm which was suitable for training my model. This file includes approximately 42443 words and their sylable counts, some inputted manually while others were calculated using a program following grammatical laws. In order to put the data into a more serializable form, I converted the file to Training_Data.txt, which removes all symbols leaving only the word with the syllable count next to it, calculated by counting the amount of hyphens in the word separation and adding one. 

I then converted those words in DeepSyllable.py to character arrays with each letter being represented by its ASCII decimal counterpart, and in another array put their syllable number in the corresponding index. As of right now, this neural net has two hidden layers, with the output layer have 8 nodes, the max syllable count I have placed on this net. After 80 epochs, The neural network achieves 75% accuracy, but I believe this can be increased with more advanced techniques I have yet to learn and training.
