from utilities.utils import char_to_index, hasChild, toLowerCase, toCapitalize


class TrieNode:

    def __init__(self):
        self.children = [None]*26
        self.isWordEnd = False
        self.examples = [None]

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, examples):
        crawlTrie = self.root

        word = toLowerCase(word)
        for level in range(len(word)):
            idx = char_to_index(word[level])
            if not crawlTrie.children[idx]:
                crawlTrie.children[idx] = TrieNode()
            if level == len(word)-1:
                crawlTrie.isWordEnd = True
                for eg in examples:
                    crawlTrie.examples.append(eg)

            crawlTrie = crawlTrie.children[idx]
    
    def delete_helper(self,word):
        crawlTrie = self.root
        
        word = toLowerCase(word)
        rc = self.delete(crawlTrie, word, 0)
    
    def delete(self, root, word, depth):
        '''
        1. unique word
        2. key is prefix of a bigger word
        3. if combined keys: to del bigger words, del operation is performed 
            from bottom up
        '''
        if not root:
            return None
        
        if depth == len(word)-1:
            if root.isWordEnd == True:
                root.isWordEnd = False
            
            if not hasChild(root):
                del root
                root = None
            return root
  
        idx = char_to_index(word[depth])
        root.children[idx] = self.delete(root.children[idx], word, depth+1)

        if not hasChild(root) and not root.isWordEnd:
            del root
            root = None
        
        return root


    def search(self, word):
        crawlWord = self.root
        word = toLowerCase(word)
        for lvl in range(len(word)):
            idx = char_to_index(word[lvl])
            if crawlWord.children[idx] == None:
                return False
            
            if lvl == len(word)-1:
                if crawlWord.isWordEnd:
                    return True
            crawlWord = crawlWord.children[idx]

        return False
    
    def get_word_example(self, word):
        crawlWord = self.root
        word = toLowerCase(word)
        
        if self.search(word):
            for lvl in range(lvl(word)):
                idx = char_to_index(word[lvl])
                if lvl == len(word)-1:
                    if crawlWord.isWordEnd == True:
                        return crawlWord.examples
                crawlWord = crawlWord.children[idx]
        return []
    
    def get_node(self):
        return self.root

    def _display_util(self, node, visited, str):
        index = 0
        while index < 26:
            if node.children[index]:
                str += chr(97+index)
                
                if node.isWordEnd == False:
                    self._display_util(node.children[index], visited, str)
                    str=str[0:len(str)-1]
                else:
                    if str not in visited:
                        visited.append({toCapitalize(str): node.examples})
                    if hasChild(node.children[index]):
                        self._display_util(node.children[index], visited, str)
                        str = str[0:len(str)-1]
            index += 1
        
    
    def display(self):
        crawlTrie = self.root
        visited = []
        str=''
        self._display_util(crawlTrie, visited, str)
        return visited if len(visited) else []

