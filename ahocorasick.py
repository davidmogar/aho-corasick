from collections import deque
from trie import Trie

class Ahocorasick:

    def __init__(self):
        self._trie = Trie()
        self._trie_root = self._trie._root
        self._trie_root.failure = self._trie_root

    def add_word(self, word, value):
        self._trie[word] = value

    def make_automaton(self):
        queue = deque()

        for child in self._trie_root.children.values():
            child.failure = self._trie_root
            queue.append(child)

        while len(queue):
            node = queue.popleft()
            for child_character, child in node.children.items():
                queue.append(child)
                state = node.failure

                found = False
                while not found:
                    for state_character, state_child in state.children.items():
                        if state_character == child_character:
                            found = True
                            break
                    if not found:
                        if state == self._trie_root:
                            found = True
                            state_child = self._trie_root
                        else:
                            state = state.failure
                child.failure = state_child

    def search(self, text):
        current_node = self._trie_root
        for index, character in enumerate(text.lower()):
            found = False
            for child_character, child in current_node.children.items():
                if child_character == character:
                    current_node = child
                    found = True

                    if child.final:
                        end_index = index + 1
                        value = child.value
                        yield end_index - len(value), end_index, value
                        break
            if not found and current_node != self._trie_root:
                current_node = current_node.failure
