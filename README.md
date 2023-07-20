# Dictionary with Word Completion

## Overview

This project focuses on implementing a dictionary comprising words and their frequencies, allowing word completion. We explore and compare the performance of three different data structures: Array (Python list), Linked List, and Trie. The dictionary supports operations such as adding words, searching for frequencies, deleting words, and auto-completion.

## Data Structures

### Array-Based Dictionary

In the array-based dictionary, we use Python lists to implement common dictionary operations. Each element in the array represents a pair (word, frequency), where word is an English word (string), and frequency is its usage frequency (non-negative integer). The array is sorted alphabetically to facilitate search. Adding a new word preserves the alphabetical order. Example: [(‘ant’, 1000), (‘ape’, 200), (‘auxiliary’, 2000)].

### Linked List-Based Dictionary

The linked-list-based dictionary uses an unsorted singly linked list. Each node stores a pair (word, frequency) and a reference to the next node. Words are added at the front of the list. Search, Delete, and Auto-completion are similar to the array-based implementation, but words are not sorted.

### Trie-Based Dictionary

The trie is a tree-like data structure storing (key, value) pairs. Each node represents a letter from the English alphabet and stores a boolean indicating the end of a word, frequency (if it's the end of a word), and children nodes. The trie is efficient for spell checking and auto-completion.

## Operations

The implemented dictionaries support the following operations:

- Search (S): Search for a word and return its frequency. Return 0 if not found.
- Add (A): Add a word and its frequency to the dictionary. Return True if successful or False if it already exists.
- Delete (D): Delete a word from the dictionary. Return True if successful or False if the word doesn't exist.
- Auto-completion (AC): Return a sorted list of the three most frequent words (if any) in the dictionary that have the given string as a prefix.

## Running the Code

To use the dictionaries and perform operations, run the main program and provide the command file as input. The command file contains a list of operations and arguments.

### Command Format

Each operation is specified in the command file using the following format:

<operation> [arguments]

Where operation is one of {S, A, D, AC}, and arguments are optional depending on the operation.

## Examples

Below are some examples of the commands and their expected outputs:

S apple
Output: 1000

A banana 800
Output: True

D apple
Output: True

AC ba
Output: [(banana, 800)]

##Testing Framework
Debugging. To run the code, from the directory where dictionary file based.py is, execute
(use ‘python3’ on Linux, ‘python’ on Pycharm):
> python3 dictionary_file_based.py <approach> <data filename> <command filename>
<output filename>
where
• approach is one of the following: array, linkedlist, trie,
• data filename is the name of the file containing the initial set of words and frequencies,
• command filename is the name of the file with the commands/operations,
• output filename is where to store the output of program.
For example, to run the test with sampleDataToy.txt, type (in Linux, use ‘python3’, on Pycharm’s
terminal, use ‘python’):
6
