import unittest
from monotonicNode import MonotonicNetwork
import random
import numpy as np

class TestStringMethods(unittest.TestCase):
    # Default test that makes sure merges result in the same value across different orderings
    def test_consistency(self):
        # Seeded to replicate results
        random.seed(100000)
        n = 10
        updateList = [random.randint(0, n-1) for _ in range(100)]
        network1 = MonotonicNetwork(n)
        network1.batchIncrement(np.random.permutation(updateList).tolist())
        network2 = MonotonicNetwork(n)
        network2.batchIncrement(np.random.permutation(updateList).tolist())

        # Merging node 0 with all other nodes
        central_node_id = 0
        for i in range(1, n):
            network1.mergeNode(central_node_id, i)
            network2.mergeNode(central_node_id, i)
        print(network1.node_map[central_node_id])
        print(network2.node_map[central_node_id])
        # Tests that node 0 is the same between the two different operation orderings after merging all nodes
        self.assertTrue(network1.node_map[central_node_id].isSubsetOf(network2.node_map[central_node_id]))
        self.assertTrue(network2.node_map[central_node_id].isSubsetOf(network1.node_map[central_node_id]))

    # Expands onto first test, except with added duplicate operations
    def test_duplicates(self):
        random.seed(100000)
        n = 10
        updateList = [random.randint(0, n-1) for _ in range(100)]
        updateList += list(np.random.choice(updateList, 50))

        # Apply the same operations to the network in different orderings
        network1 = MonotonicNetwork(n)
        network1.batchIncrement(np.random.permutation(updateList).tolist())
        network2 = MonotonicNetwork(n)
        network2.batchIncrement(np.random.permutation(updateList).tolist())

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
