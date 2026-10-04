# SLE-3 – Graph Search System Using BFS and DFS

## Course
**02AML204 – Introduction to Artificial Intelligence**

## Student Details
- **PRN:** 25UAM120
- **Name:** Sharayu Rakesh Savale
- **Division:** B

---

## 1. Project Title

**Graph Search System using BFS and DFS**

---

## 2. Project Description

This project presents the architectural design of a Graph Search System using the **Full C4 Model**.

The system takes a graph, start node, and goal node as input. It uses **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** to search the graph and produces the search result/path.

The system continues the Graph Search System developed and evaluated in **SLE-2**.

---

## 3. C4 Architecture

The system is represented using all four levels of the C4 Model:

### Level 1 – Context Diagram

The Context Diagram shows the interaction between the **User** and the **Graph Search System**.

The user provides:
- Graph
- Start Node
- Goal Node

The system performs the search and returns the search result/path.

**Diagram:** `SLE3_Level1_Context_Diagram.png`

---

### Level 2 – Container Diagram

The Graph Search System is divided into the following containers:

1. **Input Module** – Takes the graph, start node, and goal node.
2. **Search Engine** – Performs BFS and DFS.
3. **Visited Set / Memory** – Stores visited nodes.
4. **Goal Test** – Checks whether the goal node is reached.
5. **Output Module** – Displays the search result/path.

**Diagram:** `SLE3_Level2_Container_Diagram.png`

---

### Level 3 – Component Diagram

The **Search Engine** is divided into the following components:

1. **Frontier / Open List**
2. **Explored / Closed Set**
3. **Goal Test**
4. **Path Reconstructor**

These components work together to perform the search and produce the final path.

**Diagram:** `SLE3_Level3_Component_Diagram.png`

---

### Level 4 – Code Level Overview

The main functions/modules of the system are:

- `graph = {...}` – Stores the graph structure.
- `bfs_search()` – Performs Breadth-First Search.
- `dfs_search()` – Performs Depth-First Search.
- `goal_test()` – Checks the goal node.
- `reconstruct_path()` – Reconstructs the search path.
- `main()` – Handles input and output.

---

## 4. Design Decisions

- BFS and DFS are placed inside the **Search Engine** because they perform the main search operation.
- The system is divided into separate containers for clear organization.
- The **Visited Set / Memory** keeps track of explored nodes.
- The architecture continues the Graph Search System developed in **SLE-2**.
- The Full C4 Model represents the system from overall context to code-level functions.

---

## 5. AI Contribution

**ChatGPT** was used for:

- Understanding the C4 architecture requirements.
- Planning the system architecture.
- Getting guidance for organizing the four C4 levels.
- Preparing and refining the report content.

The student selected the system structure, created and finalized the diagrams, and prepared the final submission.

---

## 6. Files Included

| File | Description |
|---|---|
| `SLE3_25UAM120_Sharayu_Rakesh_Savale.docx` | SLE-3 Report |
| `SLE3_Level1_Context_Diagram.png` | C4 Level 1 – Context Diagram |
| `SLE3_Level2_Container_Diagram.png` | C4 Level 2 – Container Diagram |
| `SLE3_Level3_Component_Diagram.png` | C4 Level 3 – Component Diagram |

---

## 7. Conclusion

The Full C4 Model provides a clear architectural view of the Graph Search System, from the overall system context to its internal components and code-level functions.

This SLE-3 architecture builds upon the Graph Search System developed and evaluated in SLE-2.