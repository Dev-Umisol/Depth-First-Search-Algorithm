# 📁 Depth First Search (DFS)

> A Python implementation of the Depth First Search graph traversal algorithm using an iterative stack-based approach.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Learning](https://img.shields.io/badge/Learning-Journey-orange)
![DSA](https://img.shields.io/badge/Topic-Algorithms-red?logo=python&logoColor=white)

---

## 📌 About

This project implements Depth First Search, one of the two fundamental graph traversal algorithms alongside BFS. Where BFS (implemented in the Generate Parentheses project) explores level by level using a queue, DFS dives as deep as possible along each path before backtracking, using a stack. Built to understand the LIFO traversal strategy, how disconnected graphs behave, and how stack-based iteration mirrors recursive DFS without the call stack overhead.

---

## 🧠 What I Learned

- **LIFO stack for DFS** — Using `stack.pop()` to always process the most recently added node first, which drives the algorithm deep into the graph before exploring other branches — the defining behavior of depth-first traversal
- **BFS vs DFS side by side** — Having implemented BFS (via `queue.pop(0)`) in the Generate Parentheses project, the contrast is clear: swapping FIFO for LIFO is what separates the two traversal strategies entirely
- **`enumerate()` on adjacency matrix rows** — Using `for index, value in enumerate(matrix[node])` to check every column in the current node's row, and only pushing neighbors to the stack where `value == 1`
- **Visited list for cycle prevention** — Checking `if node not in visited` before processing ensures nodes aren't revisited in graphs with cycles, preventing infinite loops
- **Disconnected graph behavior** — Testing with a disconnected graph (nodes 2 and 3 isolated from 0 and 1) confirms that DFS only traverses the connected component containing the start node, unreachable nodes are simply never visited
- **Iterative vs recursive DFS** — Understanding that the stack-based iterative approach produces the same traversal order as recursion but avoids Python's recursion depth limit on very large graphs

---

## 🛠️ Technologies Used

| Tool / Library | Purpose |
|---|---|
| Python 3.x | Core language |

---

## 💡 How It Works

The graph is represented as an undirected adjacency matrix. The algorithm starts at the given node, pushes it to the stack, and repeatedly pops and explores unvisited neighbors until the stack is empty.

```
Graph (4 nodes):
0 - 1 - 2 - 3

Matrix:
[0, 1, 0, 0]
[1, 0, 1, 0]
[0, 1, 0, 1]
[0, 0, 1, 0]

DFS from node 1:
Stack: [1] → pop 1, visited: [1] → push 0, 2
Stack: [0, 2] → pop 2, visited: [1, 2] → push 1, 3
Stack: [0, 1, 3] → pop 3, visited: [1, 2, 3] → push 2
Stack: [0, 1, 2] → pop 2 (already visited)
Stack: [0, 1] → pop 1 (already visited)
Stack: [0] → pop 0, visited: [1, 2, 3, 0]
Result: [1, 2, 3, 0]
```

**Example output:**
```python
dfs(matrix, 1)  # [1, 2, 3, 0]
dfs(matrix, 3)  # [3, 2, 1, 0]

# Disconnected graph — node 3 is isolated
dfs(disconnected_matrix, 3)  # [3]
dfs(disconnected_matrix, 0)  # [0, 1]
```

---

## 🚀 Future Improvements

- [ ] Implement BFS directly alongside DFS and compare traversal order on the same graph
- [ ] Add cycle detection — track back edges during traversal to identify loops
- [ ] Extend to directed graphs and test behavior with one-way edges
- [ ] Implement the recursive version and compare output and performance

---

## 📂 Project Structure

```
depth-first-search/
│
├── DepthFirstSearchAlgorithm.py    # dfs function and example usage
└── README.md
```

---

*Part of my Python learning journey 🐍 — completing the graph traversal pair alongside BFS and Dijkstra's shortest path*
