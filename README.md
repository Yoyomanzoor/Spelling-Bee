# Spelling Bee
 
Code to take a list of words and turn it into a Spelling bee.

Word list must be provided in the following format:

Category Word Definition

Where category can be {Eh, Hard, Harder, Hardest} (case sensitive). Word must be a single word or hyphenated words (no spaces). Definition is defined as everything after the word.

Spaces delineate these three items, so there must be one space between category, word, and definition.

Example:  
Hard Aardwolf A hyena-like animal of southern and eastern Africa.

Definitions are _not necessary_, but helpful. If no definition is provided, there still must be a space after the word.

The game works by simple running in jupyter notebook, selecting a category and choosing a word. Words are eliminated from the categories as they are used.
