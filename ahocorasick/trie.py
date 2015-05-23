class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = {}
        self.failure = None
        self.parent = None
        self.final = False


class Trie:
    def __init__(self):
        self._root = Node()

    def get(self, key, default=None):
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def _find(self, key):
        node = self._root
        for character in key:
            node = node.children.get(character)
            print(node.children.keys(), node.final, node.value)
            if node is Node or node.final:
                break

        return node

    def __getitem__(self, key):
        node = self._find(key)
        if node is None or node.value is None:
            raise KeyError
        return node.value

    def __setitem__(self, key, value):
        node = self._root
        for character in key:
            next = node.children.get(character)
            if next is None:
                node = node.children.setdefault(character, Node())
            else:
                node = next
        node.value = value
        node.final = True
