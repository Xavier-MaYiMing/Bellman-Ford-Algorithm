### Bellman-Ford Algorithm

##### Reference: Bellman R. On a routing problem[J]. Quarterly of Applied Mathematics, 1958, 16(1): 87-90.

The Bellman-Ford algorithm for the shortest path problem with negative weights.

| Variables | Meaning                                                      |
| --------- | ------------------------------------------------------------ |
| network   | Dictionary, {node1: {node2: length, node3: length, ...}, ...} |
| nn        | The number of nodes                                          |
| dis       | List, dis[i\]\[j\] denotes the length of the shortest path from node i to node j |
| path      | List, path\[i\]\[j\] denotes the shortest path from node i to node j |

#### Example

![](https://github.com/Xavier-MaYiMing/Bellman-Ford-Algorithm/blob/main/shortest%20path%20problem%20example.png)

```python
if __name__ == '__main__':
    source = 0
    # Example 1
    network1 = {
        0: {1: 6, 2: 5, 3: 5},
        1: {4: -1},
        2: {1: -2, 4: 1},
        3: {2: -2, 5: -1},
        4: {6: 3},
        5: {6: 3},
        6: {},
    }
    print(main(network1, source))

    # Example 2
    network2 = {
        0: {1: 4, 3: 4},
        1: {3: 4},
        2: {1: -10},
        3: {2: 3},
    }
    print(main(network2, source))
```

##### Output

```python
# Example 1
{
    'path': [[0], [0, 3, 2, 1], [0, 3, 2], [0, 3], [0, 3, 2, 1, 4], [0, 3, 5], [0, 3, 2, 1, 4, 6]], 
    'length': [0, 1, 3, 5, 0, 4, 3]
}

# Example 2
The network contains negative weight cycles
None
```

