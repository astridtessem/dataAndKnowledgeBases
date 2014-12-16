dataAndKnowledgeBases
=====================

#Documentation

###readData
**readCorpus(number):** Reads data from the directory "corpus" that contains all the tagged training data. ReadData has a number as its input. This number decides how many documents from the corpus it is going to use while training the model. The documents is chosen randomly. All the sentences from the chosen documents get inserted in an array called "corpus". Then it loops through the "corpus" array, and classify each word as organization, person, number, date and location. Each word with the corresponding classifier is saved into a new array called "corp".

**readTestDocument():**
Same as readCorpus(number) but returns only one document.


###ViterbiModel

**ConverToEntity(corpus):** The argument "corpus" is an 2*n array where each line contains a word and its corresponding entity. The method returns an array with all the entities from the input argument.

**converToWord(corpus):** The argument "corpus" is an 2*n array where each line contains a word and its corresponding entity. The method returns an array with all the words from the input argument. 

**getStates(corp):** Loop through the array with all the entities. The method returns a list of what entities that exists.  

**getStateProp(states, corpus):** This method creates the start probability array. The method counts how many there is of the different entities. Then each entity get a state propability equal to EntityCount/LengthOfCorpus. 

**getTransitionProp(states, corpus):** First it creates a dictionary, a matrix where both the rows and columns are the different states. Loop through the corpus and count the number of times one specific state (from-state) is right before another spesific state (to-state), and save this in the dictionary. For every cell in the dictionary, divide the number in the cell by the number of words that is classified as the "from-state".

**getEmissionProp(states, corpus):** : This method makes a emission matrix with every state vertically and every word in the corpus horizontally. The number in each cell is based on how big probability to find that specific word given the specific state, P(Word|State). 


###ViterbiAlgorithm

**Viterbi(obs, states, start_p, trans_p, emit_p):** Calculate the probability of each state for every observation. For level 0, we have a special case using the start probability.
When the word is unknown, use feature extraction to classify it and give it a predefined value. 

###CreateModel
**JsonSave(data,name):** Writes the data as a json file.

**saveModel(trans_p, emit_p, states, start_p):** Saves all the arguments in the method as Json files using JsonSave(data,name).

**CreateModel:** This method creates the models. First it reads a part of the corpus. Then it get states from this part. With the states and the sub corpus a startProp, transProp and emitProp is created. It then saves the models using the function saveModel. The method have two inputs: the number of models to create and how many documents in each model.

###RunModel

**readJson(name):** Read json files.  

**readData:** This function use the readJson function to read the json files of transProp, emitProp, startProp and states and return them. 

**Main(text,numOfMod):** This function is the main function which runs the whole application after the startProp, transProp and emitProp is made. It uses the viterbi function on the input text and return the for each word with its most likely entity according to the viterbi matrix. When every word is classified it try to do feature extraction on the words that are classified as other. The algorithm is using a given number of models and returns the average of each model.



###Features
**featureEmitFail:** This method is run when the word is not in the emission matrix. 

###Testing
**test(numberOfWords,numberOfDocuments,numberOfModels):** This method selects a random document from the corpus to test the algorithm on a given number of words and models. It uses the methods "wash" and "createSentences" to create this test-data. 


