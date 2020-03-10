# Spelling Bee

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Yoyomanzoor/Spelling-Bee/master?filepath=Spelling%20Bee.ipynb)

Code to take a list of words and turn it into a Spelling bee.

Word list must be provided in the following format:

Category Word Definition

Where category can be {1, 2, 3, 4, 5}. Word must be a single word or hyphenated words (no spaces). Definition is defined as everything after the word.  

Spaces delineate these three items, so there must be one space between category, word, and definition.

Categories:  
1 - Easy and common  
2 - Common but long  
3 - Uncommon and easy or common and hard  
4 - Uncommon and hard  
5 - Impossible

Example:  
3 Aardwolf A hyena-like animal of southern and eastern Africa.

Definitions are _not necessary_, but helpful. If no definition is provided, there still must be a space after the word.

If taking words from the [word bank doc](https://docs.google.com/document/d/1O-1TZITIUuTnN28TyXlmFu6IpotN2YCOjRO343KABn8/edit?usp=sharing), use http://reverse-complement.com/cleanup.html to remove the list numbering.

The game works by simply running in jupyter notebook, selecting a category and choosing a word. Words are eliminated from the categories as they are used.
