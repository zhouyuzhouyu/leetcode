"""
208. 实现 Trie (前缀树)
难度
中等

297

收藏

分享
切换为英文
关注
反馈
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true
说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。
"""





class TrieNode:
    R = 26
    def __init__(self):
        self.links = [None for _ in range(self.R)]
        self.bEnd = False

    def setEnd(self):
        self.bEnd = True

    def isEnd(self) -> bool:
        return self.bEnd

    def containsKey(self, ch) -> bool:
        return self.links[ord(ch)-ord('a')] is not None

    def get(self, ch):
        return self.links[ord(ch)-ord('a')]

    def put(self, ch, node):
        self.links[ord(ch)-ord('a')] = node


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for i in range(len(word)):
            currentChar = word[i]
            if not node.containsKey(currentChar):
                node.put(currentChar, TrieNode())
            node = node.get(currentChar)
        node.setEnd()

    def searchPrefix(self, word: str) -> TrieNode:
        node = self.root
        for i in range(len(word)):
            currentChar = word[i]
            if node.containsKey(currentChar):
                node = node.get(currentChar)
            else:
                return None

        return node



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.searchPrefix(word)
        return node is not None and node.isEnd()


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.searchPrefix(prefix)
        return node is not None



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

trie = Trie();

trie.insert("apple");
trie.search("apple");   # 返回 true
trie.search("app");     # 返回 false
trie.startsWith("app"); # 返回 true
trie.insert("app");
trie.search("app");     # 返回 true

