# https://leetcode.com/problems/clone-graph/
# O(V*E) time ? O(V+E) space, BFS walk

import collections

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        
        d = {node: Node(node.val)}
        q = collections.deque([node])
        while q:
            orig = q.popleft()
            copy = d[orig]
            for n in orig.neighbors:
                if n not in d:
                    d[n] = Node(n.val)
                    q.append(n)
                copy.neighbors.append(d[n])

        return d[node]