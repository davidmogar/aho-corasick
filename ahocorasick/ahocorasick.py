from collections import deque

from .trie import Trie


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

    def search(self, text, longest=True):
        current_node = self._trie_root
        match = None

        for index, character in enumerate(text.lower()):
            found = False
            matched = False
            for child_character, child in current_node.children.items():
                if child_character == character:
                    current_node = child
                    found = True

                    if child.final:
                        matched = True
                        end_index = index + 1
                        value = child.value
                        match = end_index - len(value), end_index, value
                        break
            if match and (not longest or (not matched or index == len(text) - 1)):
                yield match
                match = None
            if not found and current_node != self._trie_root:
                current_node = current_node.failure
