class MonotonicNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.value = 0
        self.local_map = {} 
    def increment(self):
        self.value += 1
        self.applyUpdate(self.node_id, self.value)
    def applyUpdate(self, node_id, value):
        if not node_id in self.local_map.items():
            self.local_map[node_id] = value
        else:
            self.local_map[node_id] = max(value, self.local_map[node_id])
    def merge(self, node: 'MonotonicNode'):
        for node_id, value in node.local_map.items():
            self.applyUpdate(node_id, value)
    def isSubsetOf(self, node: 'MonotonicNode'):
        for node_id, value in node.local_map.items():
            if node_id not in self.local_map or self.local_map[node_id] > value:
                return False
        return True
    def __str__(self):
        return "nodeID: {}\nvalue: {}\nlocal map: {}\n".format(self.node_id, self.value, str(self.local_map))

class MonotonicNetwork:
    def __init__(self, num_of_nodes: int):
        self.node_map = {}
        self.n = num_of_nodes
        for i in range(self.n):
            self.node_map[i] = MonotonicNode(i)
    def createNode(self):
        self.node_map[self.n] = MonotonicNode(self.n)
        self.n += 1
    def mergeNode(self, first_node_id, second_node_id):
        # Merge operation will make both nodes consistent with each other
        # not sure if crdt merge operations are one way or two way 
        self.node_map[first_node_id].merge(self.node_map[second_node_id]) 
        self.node_map[second_node_id].merge(self.node_map[first_node_id]) 
    def batchIncrement(self, list_of_updates: list[int]):
        for node_id in list_of_updates:
            self.node_map[node_id].increment()
