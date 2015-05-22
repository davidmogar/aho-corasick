from collections import deque
from trie import Trie

trie = Trie()
trie['he'] = 'he'
trie['she'] = 'she'
trie['hers'] = 'hers'
trie['his'] = 'his'

def compute_failures():
    root = trie._root
    root.failure = root

    queue = deque()

    for child in root.children.values():
        child.failure = root
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
                    if state == root:
                        found = True
                        state_child = root
                    else:
                        state = state.failure
            child.failure = state_child

compute_failures()
