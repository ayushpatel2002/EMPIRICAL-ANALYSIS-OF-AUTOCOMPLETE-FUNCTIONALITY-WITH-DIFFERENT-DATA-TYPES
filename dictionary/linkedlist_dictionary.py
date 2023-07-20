from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency


class ListNode:
    """
    Define a node in the linked list
    """

    #  creating some methods which would be helpful for the bigger functions
    def __init__(self, word_frequency: WordFrequency):
        self.word_frequency = word_frequency
        self.next = None

    def set_next(self, next_element):
        self.next = next_element

    def get_value(self):
        return self.word_frequency

    def get_next(self):
        return self.next

    def set_value(self, word_frequency: WordFrequency):
        self.word_frequency = word_frequency


# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class LinkedListDictionary(BaseDictionary):

    def __init__(self):
        # TO BE IMPLEMENTED
        # initiating the linkedlist with head node as none
        self.head = None

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # we would create a new_node as first element of words_frequencies
        new_node = ListNode(words_frequencies[0])
        # initiating the linkedlist with head node as new_node
        self.head = new_node
        i = 1
        while i in range(len(words_frequencies)):
            # we will assign next node of new_node to current element of words_frequencies list
            new_node.next = ListNode(words_frequencies[i])
            new_node = new_node.next
            # increament the counter
            i = i + 1

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # for search, we will iterate through linked list
        # first, we will initiate current_element as head of the linkedlist
        current_element = self.head
        while current_element:
            if current_element.word_frequency.word == word:
                return current_element.word_frequency.frequency
            # after every iteration, we will current_element as next element to it
            current_element = current_element.next
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # TO BE IMPLEMENTED
        # we will assign word to be added as new node
        new_node = ListNode(word_frequency)
        # if new_node is none, we will init the linkedlist and assign curr as head of linkedlist
        if self.head is None:
            self.head = new_node
            return True
        curr = self.head
        #  iterate through linkedlist, if word is already present, return false
        while curr:
            if curr.word_frequency.word == word_frequency.word:
                return False
            # after every iteration, we will curr as next element to it
            curr = curr.next

        last = self.head
        while last.next:
            last = last.next
        # finally, we will add new element at last of the linkedlist
        last.next = new_node
        return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """

        # TO BE IMPLEMENTED
        current_element = self.head
        # if the word to be deleted found, we will return true and delete thw word with help of iteration of linkedlist
        if current_element.word_frequency.word == word:
            self.head = current_element.next
            return True
        # when the word is found, we will assign prev_element as current_element
        prev_element = current_element
        # followed by, assigning of current_element to next element to it
        current_element = current_element.next

        while current_element:
            # a while is used to unlink the found element
            if current_element.word_frequency.word == word:
                prev_element.set_next(current_element.next)
                return True
            # continuing the loop by assigning current_element as next element to it
            prev_element = current_element
            current_element = current_element.next

        return False

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        # creating a new array which will store all the words with same prefix as parameter
        auto_dict = []
        # iterating through array and searching for words with startswith function
        # if word matches, we will append it to auto_dict
        current_element = self.head
        while current_element:
            if current_element.word_frequency.word.startswith(word):
                auto_dict.append(
                    WordFrequency(current_element.word_frequency.word, current_element.word_frequency.frequency))
            current_element = current_element.next
        #     sorting auto_dict in descending order on frequency
        auto_dict.sort(reverse=True, key=lambda y: y.frequency)
        # selecting first 3 elements auto_dict and deleting rest of it
        del auto_dict[3:]
        # returning auto_dict
        return auto_dict

