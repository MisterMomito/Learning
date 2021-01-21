class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode('*')

    def add_word(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = TrieNode(letter)
            curr_node = curr_node.children[letter]
        curr_node.is_end_of_word = True

    def does_word_exist(self, word):
        if word == '':
            return True
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]
        return curr_node.is_end_of_word

# My own print function

    def print_trie(self):
        self._print_trie(self.root)

    def _print_trie(self, cur_node, level_counter=0):

        for v, i in (cur_node.children.items()):
            print('Level ' + str(level_counter))
            print('Letter: ' + v)
            print('Children: ' + str(i.children.keys()))
            if cur_node.children[v].is_end_of_word:
                print('This is the end of a word.')
            print()

        for v in cur_node.children.keys():
            self._print_trie(cur_node.children[v], (level_counter+1))

# test code
trie = Trie()
words = {'wait', 'waiter', 'shop', 'shopper'}
for figure in words:
    trie.add_word(figure)


print(trie.does_word_exist('wait'))
print(trie.does_word_exist(''))
print(trie.does_word_exist('waite'))
print(trie.does_word_exist('shop'))
print(trie.does_word_exist('shoppp'))
trie.print_trie()

