# Dzongkha Spell Checker

# Overview
The main aim of this project (Dzongkha spell Checker) is to provide a simple  command line utility to 
the spelling of the words in dzongkha text files. It compares the words from an input file 
against a predefined dictonary of valid Dzongkha words and reports any incorrect spellings, along 
with their exact location in the text and it is a step toward enhancing Dzongkha language tools and
improving written content quality.

# Table of content
- [Usuage](#usage)
- [Implementation-details](#implementation-details)
- [Data-Structure](#data-structure)
- [Algorithns](#algorithms)
- [Challenges-and-solution](#challenges-and-solution)
- [Future-Improvements](#future-improvenment)
- [References](#references)

## Usage

python3

The command to excutive the scripts ( dzongkha_spell_checker. py input.docx)

Dzo.text

# Implementation 
Primarily, the raw dictionary text file containing wrong Dzongkha spellings has bieng cleaned.
The code for the cleaning process is written as  "cleaning_dictionary.py" file.

This Python script converts a .docx file into a plain text .txt file by extracting the text from 
each paragraph in the document and writing it into a text file.

The Dzongkha spell Checker project implement an algorithm using a sliding window technique to  
detect compound words in a text. It checks individual words or word groups against the dictionary,
marking any word not found in the dictionary as s spelling error.

# Data structure
1. set: The correct word of dictionary is contain in set for have good glance.
2. List: Input file is read line by line.
3. Tuple List: Used to store words found as a errors.

# Algorithms
### Dictionary Lookup:
The tool stores valid Dzongkha words in set, allowing for fast word lookups. When processing input
text, it checks each word or group of words against this set. Since set lookups are efficient, this 
makes the process run quickly.

### Sliding Window 
Few Dzongkha words are compound words made up of multiple smaller words. To identify valid compound
words, the sliding window algorithm is used. This algorithm starts by checking one word, then adds
subsequent words to form potential compound words. If the compound word exists in the dictionary, the
tool accepts it and moves forward.

### Word Cleaning:
Before comparing the words against the dictionary, the tool removes certain characters, such as "།" 
(used in Dzongkha), which are not part of the word itself. This ensures  accurate word matching.

This restructuring makes it more reader-friendly while keeping the technical essence intact.

# Challenges and solution
Dzongkha has many long words made from smaller ones. A slidding window method was used to better 
detect these words and handling Dzongkha characters and Punctuation was tricky, so the program 
removed certain symbols (like ":") from the dictionary before matching with text files.

# Future Improvement
Instead of using a basic sliding window, consider an algorithm that analyzes the compound word.