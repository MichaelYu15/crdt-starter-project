To test, run `python3 testMonotonicNode.py` and `python3 testNonMonotonicNode.py`

Next tasks:
- Implement CRDT Tree and extend `merge` and `update` operations to the data structure
- Add asynchronous behavior to tests, i.e. represent each node as a socket and track the amount of bandwidth each merge sends across the network to complete the operation.
    - This should help quantify the improvement that the tree provides, in terms of throughput
