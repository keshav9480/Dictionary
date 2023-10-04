
class TrieNode:

    def __init__(self):
        self.children = [None]*26
        self.isWordEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def __char_to_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):

        crawlTrie = self.root
        for level in range(len(word)):
            idx = self.__char_to_index(word[level])
            print("index of ch: {} idx: {}".format(word[level], idx))
            if not crawlTrie.children[idx]:
                crawlTrie.children[idx] = TrieNode()
            crawlTrie = crawlTrie.children[idx]

        crawlTrie.isWordEnd = True
    
    def delete(self,word):

        crawlTrie = self.root
        for ch in word:
            idx = self.__char_to_index(ch)
            if crawlTrie.children[idx] == None:
                return False
            crawlTrie = crawlTrie.children[idx]
        crawlTrie.isWordEnd = False
    
    def search(self, word):

        crawlWord = self.root
        for ch in word:
            idx = self.__char_to_index(ch)
            if crawlWord.children[idx] == None:
                return False
            crawlWord = crawlWord.children[idx]

        return True
    
    def _hasChild(self, node):
        index=0
        while index<26:
            if node.children[index]:
                return True
            index += 1
        
        return False

    
    def _display_util(self, node, visited, str):
        
        index = 0
        while index < 26:
            if node.children[index]:
                str += chr(97+index)
                
                if node.isWordEnd == False:
                    print("str: {} is_end: {}".format(str,node.isWordEnd))
                    self._display_util(node.children[index], visited, str)
                    str=str[0:len(str)-1]
                else:
                    print("str end: {}".format(str))
                    if str not in visited:
                        visited.append(str)
                    if self._hasChild(node.children[index]):
                        self._display_util(node.children[index], visited, str)
                        str = str[0:len(str)-1]
            index += 1
        
    
    def display(self):
        #depth first search method
        #print("first char: {}".format(self.root.children[2].isWordEnd))
        crawlTrie = self.root
        visited = []
        str=''
        self._display_util(crawlTrie, visited, str)
        return visited if len(visited) else []







            
