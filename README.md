# 📁 DFS Adjacency Matrix Traversal
> A Python implementation of the Depth-First Search algorithm designed to traverse undirected graphs represented by adjacency matrices.

---

## 📌 About

This project explores graph theory by implementing a non-recursive Depth-First Search (DFS). The algorithm processes an **Adjacency Matrix** a square grid where a `1` at `matrix[i][j]` indicates a connection between node `i` and node `j`. This approach is particularly useful for understanding how computers represent physical networks, social connections, or map data in memory

---

## 🧠 What I Learned

- **Adjacency Matrix Navigation** — Mapping rows and columns to node labels. By iterating through a specific row, I learned how to identify all neighbors of a specific vertex in O(V) time.
- **The LIFO Principle** — Utilizing the `list.pop()` method to create a Last-In, First-Out (LIFO) structure, which forces the search to explore the full depth of a branch before backtracking.
- **Handling Disconnected Graphs** — Observation of how the algorithm behaves when starting at an isolated node (as seen in the example output for node 3 in a sparse matrix).
- **Cyclic Graph Prevention** — Using a `visited` collection to ensure that the algorithm doesn't get trapped in infinite loops when traversing undirected edges that point back to previously visited nodes.

---

## 🛠️ Technologies Used
| Tool / Library | Language |
|---|---|
| Python 3.x | Core Language |

---

## 💡 How It Works

The function takes the matrix and a starting node. It pushes the start node onto a stack. While the stack isn't empty, it pops a node, marks it as visited, and finds all neighbors in the matrix that haven't been visited yet, pushing them onto the stack.

```
# Matrix representing: 0 -- 1 -- 2 -- 3
matrix = [
  [0, 1, 0, 0],
  [1, 0, 1, 0],
  [0, 1, 0, 1],
  [0, 0, 1, 0]
]

dfs(matrix, 1) # Result: [1, 2, 3, 0] (Deep dive order)
```

---

## 🚀 Future Improvements

- [ ] Efficiency Upgrade: Replace the `visited` list check with a `set()` to move from O(n) to O(1) lookup time.
- [ ] Graph Variety: Add support for **Adjacency Lists** (dictionaries), which are more space efficient for sparse graphs.
- [ ] Pathfinding: Modify the algorithm to return the shortest path between two specific nodes.
- [ ] Visualization: Use the `networkx` library to draw the graph and highlight the DFS path.

---

## 📂 Project Structure
```
dfs-matrix-traversal/
│
├── DepthFirstSearchAlgorithm.py     # DFS implementation and example test cases
└── README.md
```

---

*Part of my Python learning journey 🐍 — exploring graph structures, matrices, and stack based traversal*
