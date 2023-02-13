import unittest
from nonMonotonicNode import NonMonotonicNetwork
import random
import numpy as np

class TestStringMethods(unittest.TestCase):
    def test_consistency(self):
        random.seed(100000)
        n = 10
        updateList = [(random.randint(0, n-1), random.randint(-100, 100)) for _ in range(100)]

        # Apply the same operations to the network in different orderings
        network1 = NonMonotonicNetwork(n)
        network1.batchOperation(np.random.permutation(updateList).tolist())

        network2 = NonMonotonicNetwork(n)
        network2.batchOperation(np.random.permutation(updateList).tolist())

        # Merging node 0 with all other nodes
        central_node_id = 0
        for i in range(1, n):
            network1.mergeNode(central_node_id, i)
            network2.mergeNode(central_node_id, i)
        print(network1.node_map[central_node_id])
        print(network2.node_map[central_node_id])
        # Tests that node 0 is the same between the two different orderings after merging all nodes
        self.assertTrue(network1.node_map[central_node_id].isSubsetOf(network2.node_map[central_node_id]))
        self.assertTrue(network2.node_map[central_node_id].isSubsetOf(network1.node_map[central_node_id]))

    def test_duplicates(self):
        random.seed(100000)
        n = 10
        updateList = np.array([(random.randint(0, n-1), random.randint(-100, 100)) for _ in range(100)])
        temp = updateList[np.random.choice(len(updateList), 50).tolist()]
        updateList = updateList.tolist() + temp.tolist()

        # Apply the same operations to the network in different orderings
        network1 = NonMonotonicNetwork(n)
        network1.batchOperation(np.random.permutation(updateList).tolist())
        network2 = NonMonotonicNetwork(n)
        network2.batchOperation(np.random.permutation(updateList).tolist())

        # Merging node 0 with all other nodes
        central_node_id = 0
        for i in range(1, n):
            network1.mergeNode(central_node_id, i)
            network2.mergeNode(central_node_id, i)
        # Tests that node 0 is the same between the two different orderings after merging all nodes
        self.assertTrue(network1.node_map[central_node_id].isSubsetOf(network2.node_map[central_node_id]))
        self.assertTrue(network2.node_map[central_node_id].isSubsetOf(network1.node_map[central_node_id]))

if __name__ == '__main__':
    unittest.main()
