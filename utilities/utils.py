

def char_to_index(ch):
        return ord(ch) - ord('a')
    
def hasChild(node):
    for idx in range(26):
        if node.children[idx]:
            return True
    
    return False

def toLowerCase(word):
    return word.lower()

def toCapitalize(word):
    return word.capitalize()
