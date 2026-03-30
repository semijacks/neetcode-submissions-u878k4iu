class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        

    def search(self, word: str) -> bool:
        def dfs(index, node):
            curr = node
            for i in range(index, len(word)):
                char = word[i]
                
                if char == ".":
                    # Try every possible child node
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    # If none of the paths worked, this branch is a fail
                    return False
                
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            
            return curr.word

        return dfs(0, self.root)
        
