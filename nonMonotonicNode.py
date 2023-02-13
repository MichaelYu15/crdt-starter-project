class NonMonotonicNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.data = [0, 0] #(time, value)
        self.local_map = {} 
    def addOperation(self, operation):
        self.data[0] += 1
        self.data[1] += operation
        self.local_map[self.node_id] = self.data
    def merge(self, node: 'NonMonotonicNode'):
        for node_id, data in node.local_map.items():
            time, value = data
            if node_id not in self.local_map or self.local_map[node_id][0] < time:
                self.local_map[node_id] = [time, value]
    def isSubsetOf(self, node: 'NonMonotonicNode'):
        for node_id, data in node.local_map.items():
            if node_id not in self.local_map or self.local_map[node_id][0] > data[0]:
                return False
        return True
    def __str__(self):
        return "nodeID: {}\n(time, value): {}\nlocal map: {}\n".format(self.node_id, self.data, str(self.local_map))

class NonMonotonicNetwork:
    def __init__(self, num_of_nodes: int):
        self.node_map = {}
        self.n = num_of_nodes
        for i in range(self.n):
            self.node_map[i] = NonMonotonicNode(i)
    def createNode(self):
        self.node_map[self.n] = NonMonotonicNode(self.n)
        self.n += 1
    def mergeNode(self, first_node_id, second_node_id):
        # Merge operation will make both nodes consistent with each other
        # not sure if crdt merge operations are one way or two way 
        self.node_map[first_node_id].merge(self.node_map[second_node_id]) 
        self.node_map[second_node_id].merge(self.node_map[first_node_id]) 
    def batchOperation(self, list_of_updates: list[int, int]):
        for node_id, operation in list_of_updates:
            self.node_map[node_id].addOperation(operation)
