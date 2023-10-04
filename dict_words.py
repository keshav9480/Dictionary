import os
from Trie import Trie

'''
program to sort the words from the given file
'''
class Dictionary:
    def __init__(self):
        self.dict = Trie()

    def insert_word(self, word):
        if word:
            self.dict.insert(word)
            print("word inserted: ",word)
        
    def delete_word(self, word):
        if self.dict.search(word):
            self.dict.delete(word)
        else:
            print("word '{}' not present in dictionart".format(word))
    
        
    def get_sorted_words(self):
        word_list = []
        word_list = self.dict.display()
        print("sorted list of words")
        for word in word_list:
            print(word)

        


if __name__ == '__main__':
    dictionary = Dictionary()
    keys = ["abc"]
    for key in keys:
        dictionary.insert_word(key)

    dictionary.get_sorted_words()

        


            
