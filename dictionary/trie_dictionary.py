from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


# Class representing a node in the Trie
class TrieNode:

    def __init__(self, letter=None, frequency=None, is_last=False):
        self.letter = letter  # letter stored at this node
        # frequency of the word if this letter is the end of a word
        self.frequency = frequency
        self.is_last = is_last  # True if this letter is the end of a word
        # a hashtable containing children nodes, key = letter, value = child node
        self.children: dict[str, TrieNode] = {}


class TrieDictionary(BaseDictionary):

    def __init__(self):
        self.root = TrieNode()
        pass

    # creating a insert_node function which will help creating a trie with help of an array
    def add_new_node(self, word, freq):
        current_node = self.root
        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                new_node = TrieNode(letter)
                current_node.children[letter] = new_node
                current_node = new_node
        current_node.is_last = True
        current_node.frequency = freq

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # call add_new_node method for each word in words_frequencies
        for new_word in words_frequencies:
            self.add_new_node(new_word.word, new_word.frequency)

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # assign current_node as root of trie
        current_node = self.root
        for i in range(len(word)):
            # iterate through each letter in word
            # followed by iteration in keys of current node
            for letter in current_node.children.keys():
                # if word's individual letter is equal to current letter in loop
                if word[i] == letter:
                    #  we will proceed with loop
                    current_node = current_node.children[letter]
                    # if current_node has its is_last as true, we will return its frequency as word is complete then
                    while current_node.is_last and i == len(word) - 1:
                        return current_node.frequency
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # setting current_node as root of trie
        current_node = self.root
        word = word_frequency.word
        # iterate through each letter in word to be added
        for i in range(len(word)):
            for char in current_node.children.keys():
                if char == word[i]:
                    current_node = current_node.children[char]
                    # if current_node has its is_last attribute true, then word is already existing as return false
                    while current_node.is_last and i == len(word) - 1:
                        return False
        #             else add new node to trie by calling add_new_node method
        self.add_new_node(word_frequency.word, word_frequency.frequency)
        return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        current_element = self.root
        # iterating through each letter in word to be deleted
        for char in range(len(word)):
            for letter in current_element.children.keys():
                if word[char] == letter:
                    # assigning prev_element to current_element to keep track of current_element
                    prev_element = current_element
                    # moving to next element if letter in word matches with element in trie
                    current_element = current_element.children[letter]
                    while current_element.is_last and char == len(word) - 1:
                        # we will simply delete the word by simply making its last elemnt's is_last false as now it
                        # indicates that any word hasnt finished
                        if len(current_element.children) != 0:
                            # followed by returning true
                            current_element.is_last = False
                            return True
                        else:
                            # also we need to delete the letters for the word for example the word to be deleted is
                            # c-u-t-t-i-n-g, then we will simply remove the t-i-n-g to successfuly remove
                            # c-u-t-t-i-n-g and c-u-t stays in the trie
                            del prev_element.children[letter]
                            return True
        return False

    def suggest_words(self, node, prefix, auto_dict):
        # a depth_first_search type of method which allows to add words with similar prefix to a list in paramter
        # iterating through child nodes
        for next_child in node.children.values():
            autocomplete = prefix + next_child.letter
            if next_child.is_last:
                # if the child has true for is_last, which means word is complete and ready to appended into array
                auto_dict.append(WordFrequency(autocomplete, next_child.frequency))
            #     we will recursively call suggest_words method on newly created autocomplete
            self.suggest_words(next_child, autocomplete, auto_dict)
        #     finally return auto_dict with matching prefixes
        return auto_dict

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        auto_dict = []
        # assign current_element to the root of trie
        current_element = self.root
        for letter in word:
            # iterate through letter in "word" and then if that letter is present in current_element we will
            # move forward to next node
            if letter in current_element.children:
                current_element = current_element.children[letter]
            else:
                # else set current_element to none and break the loop
                current_element = None
                break

        if current_element is not None:
            # if current_element is not none, we will call suggest_words method to create
            # auto_dict with matching prefixes
            auto_dict = self.suggest_words(current_element, word, auto_dict)
        #     if the word has freaquency not equal to 0, we will append it to auto_dict
        if self.search(word) != 0:
            auto_dict.append(WordFrequency(word, current_element.frequency))
            #     sorting auto_dict in descending order on frequency
        auto_dict.sort(reverse=True, key=lambda y: y.frequency)
        # selecting first 3 elements auto_dict and deleting rest of it
        del auto_dict[3:]
        return auto_dict

