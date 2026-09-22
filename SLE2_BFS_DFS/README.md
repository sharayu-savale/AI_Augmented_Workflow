# SLE-2: BFS and DFS Profiling

## Course

**02AML204 – Introduction to Artificial Intelligence**

## Problem Statement

 ## Problem Statement

Perform a search from **Start Node A** to **Goal Node G** using **BFS and DFS search algorithms**, and compare their performance based on **execution time and number of nodes explored**.


## Algorithms Implemented

1. BFS-1 – Queue using `deque`
2. BFS-2 – Queue using Python list
3. DFS-1 – Stack with reversed neighbour order
4. DFS-2 – Stack with normal neighbour order

## Graph

```text
                         A
                       /   \
                      B     C
                     / \   / \
                    D   E F   G
                   / \ / \ / \
                  H  I J K L M N O
                 / \ / \ / \ /
                P Q R S T U V W X Y Z
```

**Start Node:** A
**Goal Node:** G

## Profiling

The programs were tested using the same graph and the same start and goal nodes.

* **Execution-time tool:** Python `timeit`
* **Profiling tool:** py-spy 0.4.2
* **Profiling errors:** 0

## Results

| Algorithm | Nodes Explored | Average Time (ms) |
| --------- | -------------: | ----------------: |
| BFS-1     |              7 |          0.002149 |
| BFS-2     |              7 |          0.001257 |
| DFS-1     |             24 |          0.007203 |
| DFS-2     |              3 |          0.001218 |

## Observation

For this particular graph, DFS-2 reached the goal after exploring only 3 nodes and recorded the lowest measured execution time. BFS-1 and BFS-2 explored 7 nodes each.

The results depend on the graph structure, traversal order and implementation.

## Files

* `bfs_1.py`
* `bfs_2.py`
* `dfs_1.py`
* `dfs_2.py`
* `README.md`
* `Contribution_Log.md`
