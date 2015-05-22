from collections import deque
from trie import Trie

trie = Trie()
trie['he'] = 'he'
trie['she'] = 'she'
trie['hers'] = 'hers'
trie['his'] = 'his'

def compute_failures():
    node = trie._root
    node.failure = node

    queue = deque()

    for child in node.children.values():
        child.failure = node
        queue.append(child)

    while len(queue):
        node = queue.popleft()
        for child in node.children.values():
            queue.append(child)

compute_failures()
