import os, sys
from lib.Trie import Trie
from services.prefix_search import PrefixSearch


class Dictionary:
    def __init__(self):
        self.dict = Trie()

    def insert_word(self, word, examples):
        if word:
            if not self.dict.search(word):
                self.dict.insert(word, examples)
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
            for wrd, examples in word.items():
                print(wrd)
                for eg in examples:
                    if eg:
                        print("\t\t\t\t - ",eg)
    
    def get_auto_suggestions(self, key):
        node = self.dict.get_node()
        prefix_search = PrefixSearch()
        words = prefix_search.auto_suggestion(node, key)

        print("words suggested for key: ",key)
        for wrd in words:
            print(wrd)



if __name__ == '__main__':

    dictionary = Dictionary()
    

    keys = ["Kerala","Tamilnadu","Andrapradesh","Karnataka","Maharastra",
            "Jharkhand","Westbengal","MadhyaPradesh","Goa","Gujarath","Delhi","Punjab","Sikkim","Nagaland",
            "Mizoram","Tripura","Himachalpradesh","Rajasthan","Haryana","Bihar","Chattisgarh",
            "Assam","Telangana","Uttarakhand","Arunachalpradesh","Megalaya","Manipur"]
    for key in keys:
        dictionary.insert_word(key, ["just an example", "another example"])

    dictionary.get_sorted_words()

    dictionary.get_auto_suggestions("Te")
   

        


            
