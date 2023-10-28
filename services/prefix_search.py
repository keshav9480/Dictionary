from utilities.utils import char_to_index, hasChild, toLowerCase, toCapitalize

class PrefixSearch:

    # def __init__(self, node):
    #     self.node = node
    
    def __get_suggestion(self, node, words: list, key: str):
        
        index = 0
        while index < 26:
            if node.children[index]:
                key = key + chr(97+index)
                if node.isWordEnd == False:
                    self.__get_suggestion(node.children[index], words, key)
                    key=key[0:len(key)-1]
                else:
                    if key not in words:
                        words.append(key)
                    if hasChild(node.children[index]):
                        self.__get_suggestion(node.children[index], words, key)
                        key = key[0:len(key)-1]
            index += 1
        

    def auto_suggestion(self, node, key):
        
        key = toLowerCase(key)
        words = []
        for lvl in range(len(key)):
            idx = char_to_index(key[lvl])
            if node.children[idx] is None:
                return None
            node = node.children[idx]

        if node.isWordEnd and not hasChild(node):
            return None
        
        self.__get_suggestion(node, words, key)
        
        return words