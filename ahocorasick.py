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
            state_failure = None
            while found is False:
                for state_character, state_child in state.children.items():
                    state_failure = state_child
                    if state_character == child_character:
                        found = True
                        break
                if found is False:
                    if state == root:
                        found = True
                        state_failure = root
                    else:
                        state = state.failure
            child.failure = state_failure

compute_failures()
