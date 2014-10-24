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


