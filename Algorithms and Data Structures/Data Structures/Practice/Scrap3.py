class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode('*')

    def add_word(self, word):
        cur_node = self.root
        for letter in word:
            if letter not in cur_node.children:
                cur_node.children[letter] = TrieNode(letter)
            cur_node = cur_node.children[letter]
        cur_node.is_end_of_word = True

    def does_word_exist(self, word):
        if word == '':
            return True
        cur_node = self.root
        for letter in word:
            if letter not in cur_node.children:
                return False
            cur_node = cur_node.children[letter]
        return cur_node.is_end_of_word

    def delete_word(self, word):
        cur_node = self.root
        del_node = self.root  # meaning deletion will start one after ref node
        i = 0
        letter_count = 0
        for letter in word:
            if letter not in cur_node.children:
                print('Word not in trie')
                return False
            if cur_node.children[letter].is_end_of_word and letter != word[-1]:
                del_node = cur_node.children[letter]
                letter_count = i
            if cur_node.children[letter].is_end_of_word and letter == word[-1]:
                break
            # add precaution in case there is another word that is longer than it. In this case
            # we would just turn is end of word false.
            cur_node = cur_node.children[letter]
            i += 1

        del_node.children[word[letter_count]] = None
        # print(del_node.children[word[1]].letter)
        return True

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


t = Trie()
words = {'wam', 'wamer'}
for word in words:
    t.add_word(word)
# t.print_trie()
print(t.delete_word('wamer'))
print(t.does_word_exist('wamer'))

t.print_trie()