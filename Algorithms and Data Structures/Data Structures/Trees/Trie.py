# time complexity to check if word exists:
# O(nm) where n is words in list and m is length of word searched for
# time complexity to insert word: O(m) m - length of word added


class Trie:
    def __init__(self):
        self.root = {'*': '*'}

    def add_word(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                curr_node[letter] = {}
            curr_node = curr_node[letter]
        curr_node['*'] = '*'

    def does_word_exist(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                return False
            curr_node = curr_node[letter]
        return '*' in curr_node

    def print_trie(self):
        print(self.root)


# test code
trie = Trie()
word = {'wait', 'waiter', 'shop', 'shopper'}
for word in word:
    trie.add_word(word)


print(trie.does_word_exist('wait'))
print(trie.does_word_exist(''))
print(trie.does_word_exist('waite'))
print(trie.does_word_exist('shop'))
print(trie.does_word_exist('shoppp'))

print(trie.root)

t = Trie()
t.add_word('wattery')
t.add_word('watteryful')
t.add_word('table')

print(t.does_word_exist('watery'))
print(t.does_word_exist('watteryful'))
print(t.does_word_exist('nigga'))