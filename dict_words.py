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
            if not self.dict.search(word):
                self.dict.insert(word)
                print("word inserted: ",word)
            else:
                print("word '{}' already present".format(word))
        
    def delete_word(self, word):
        if self.dict.search(word):
            self.dict.delete_helper(word)
            print("word '{}' deleted".format(word))
        else:
            print("word '{}' not present in dictionary".format(word))
    
    def get_sorted_words(self):
        word_list = []
        word_list = self.dict.display()
        print("sorted list of words")
        for word in word_list:
            print(word)

if __name__ == '__main__':
    dictionary = Dictionary()
    keys = ["abcd","ab"]
    for key in keys:
        dictionary.insert_word(key)

    dictionary.get_sorted_words()
    dictionary.delete_word("abcd")
    dictionary.get_sorted_words()

        


            
