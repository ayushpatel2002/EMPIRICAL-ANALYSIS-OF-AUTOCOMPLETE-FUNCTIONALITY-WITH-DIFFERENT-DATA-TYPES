from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
import bisect


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class ArrayDictionary(BaseDictionary):

    def __init__(self):
        # TO BE IMPLEMENTED
        self.list = list()

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED
        # creating a list of class words_frequencies
        self.list = words_frequencies
        # sorting the newly created list
        self.list.sort(key=lambda x: x.word)

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # TO BE IMPLEMENTED
        # iterating through array with help of for loop
        for x in self.list:
            # if current word at index i matches word in the parameter, we will return frequence of that word
            if x.word == word:
                return x.frequency
        #     else return 0
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # we will loop through the list if the word to be added is already in the list or not with help of a for loop
        for items in self.list:
            # if present, we will return false
            if items.word == word_frequency.word:
                return False
        #     if not, we will append the word and return true
        self.list.append(word_frequency)
        return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # TO BE IMPLEMENTED
        # we will check if word to be deleted already exists in list or not with help of a for loop
        found = False
        for x in self.list:
            # if present, we will remove the word  and return true else return false
            if x.word == word:
                self.list.remove(x)
                found = True
                return found
        return found

    # Testing Script: -
    # python3 dictionary_file_based.py array sampleDataToy.txt testToy.in testToy.out
    # diff testToy.out testToy.exp
    # python3 dictionary_file_based.py array sampleDataToy.txt testToy.in testToy.out
    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        # we create a new array in which we will store all the words with same prefix
        auto_dict = []
        for x in self.list:
            # if the word has the same prefix, it will be added into the auto_dict
            if x.word.startswith(prefix_word):
                auto_dict.append(WordFrequency(x.word, x.frequency))
        #         we will then sort the auto_dict on the frequency part
        auto_dict.sort(reverse=True, key=lambda y: y.frequency)
        # then we will only select first 3 and delete the rest which will be the words with highest frequency
        del auto_dict[3:]
        return auto_dict

