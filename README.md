dataAndKnowledgeBases
=====================

Todos:
In readData.py
- Find all entities/categories from corpus and include them in readCorpus method
- Find a way to run the inputtext on different models and find the average(or something..)

In ViterbiAlgorithm - What to do with words that don't excist in training corpus. 
1. If it is the first word in a sentence, try feature extraction and assign a defualt value. E.g if the word is "Hans"(not in training corpus) but picked up by feature extraction
replace it with a defult person name. This will work with all entities except "other". If it is not classified by feater extraction, we could shift the observation on to the right, and classify the first word as other.

2. If the word is not the first. 


Start implementing feature extractions 
Different patterens:
- Date
- Time
- Numbers
- Phone
- Adress 
If spesicif word before/after other word(road,street,zip-code)

- List of common names
- List of common Locations
- List of common Organisations



#Documentation

###readData
**readCorpus(number):** Reads data from the directory "corpus" that contains all the tagged training data. ReadData has a number as its input. This number decides how many documents from the corpus it is going to use while training the model. The documents is chosen randomly. All the sentences from the chosen documents get inserted in an array called "corpus". Then it loops through the "corpus" array, and classify each word as organization, person, number, date and location. Each word with the corresponding classifier is saved into a new array called "corp".

**readDataFile:** Is this used? 

**getObs:** Is this used? 

###ViterbiModel

**ConverToEntity(corpus):** The argument "corpus" is an 2*n array where each line contains a word and its corresponding entity. The method returns an array with all the entities from the input argument.

**converToWord(corpus):** The argument "corpus" is an 2*n array where each line contains a word and its corresponding entity. The method returns an array with all the words from the input argument. 

**getStates(corp):** Loop through the array with all the entities. The method returns a list of what entities that exists.  

**getStateProp(states, corpus):** This method creates the start probability array. The method counts how many there is of the different entities. Then each entity get a state propability equal to EntityCount/LengthOfCorpus. 

**getTransitionProp(states, corpus):** First it creates a dictionary, a matrix where both the rows and columns are the different states. Loop through the corpus and count the number of times one specific state (from-state) is right before another spesific state (to-state), and save this in the dictionary. For every cell in the dictionary, divide the number in the cell by the number of words that is classified as the "from-state".

**getEmissionProp(states, corpus):** : This method makes a emission matrix with every state vertically and every word in the corpus horizontally. The number in each cell is based on how big probability to find that specific word given the specific state, P(Word|State). 


###ViterbiAlgorithm

**Viterbi(obs, states, start_p, trans_p, emit_p):** Calculate the probability of each state for every observation. For level 0, let the cell value in the Veterbi matrix be startProp * emitProp * observation. 
For the other levels, let the cell value be...
When the word is unknown, give it the same viterbi value as the word in front of it. <-- kind of bad solution.. 

###CreateModel
**JsonSave(data,name):** Writes the data as a json file.

**saveModel(trans_p, emit_p, states, start_p):** Saves all the arguments in the method as Json files using JsonSave(data,name).

**CreateModel:** This method creates the whole training model. First it reads a part of the corpus. Then it get states from this part. With the states and the sub corpus a startProp, transProp and emitProp is created. It then saves the Model using the function saveModel. 

###RunModel

**readJson(name):** Read json files.  

**readData:** This function use the readJson function to read the json files of transProp, emitProp, startProp and states and return them. 

**Main(text):** This function is the main function which runs the whole application after the startProp, transProp and emitProp is made. It uses the viterbi function on the input text and return the for each word with its most likely entity according to the viterbi matrix. When every word is classified it try to do feature extraction on the words that are classified as other.



###Features





