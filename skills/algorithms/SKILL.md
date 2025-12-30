---
name: algorithms
description: Master algorithms and data structures in C++ - complexity analysis, sorting, searching, graphs
sasmp_version: "1.3.0"
bonded_agent: cpp-algorithms-agent
bond_type: PRIMARY_BOND
version: "1.0.0"
category: learning
---

# Algorithms Skill

**🎓 Learning Skill - Algorithms & Data Structures**

Master algorithm design and implementation in C++.

## Complexity Analysis

### Big O Notation

| Complexity | Name | Example |
|------------|------|---------|
| O(1) | Constant | Array access |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Linear search |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Bubble sort |
| O(2^n) | Exponential | Recursive fib |

## Sorting Algorithms

```cpp
#include <algorithm>
#include <vector>

std::vector<int> v = {5, 2, 8, 1, 9};

// Quick sort - O(n log n) average
std::sort(v.begin(), v.end());

// Stable sort - maintains order of equal elements
std::stable_sort(v.begin(), v.end());

// Partial sort - only first k elements
std::partial_sort(v.begin(), v.begin() + 3, v.end());

// Custom comparator
std::sort(v.begin(), v.end(), std::greater<int>());
```

## Searching Algorithms

```cpp
// Binary search - O(log n), requires sorted
std::vector<int> v = {1, 2, 3, 4, 5};
bool found = std::binary_search(v.begin(), v.end(), 3);

// Lower/upper bound
auto it = std::lower_bound(v.begin(), v.end(), 3);

// Linear search - O(n)
auto it = std::find(v.begin(), v.end(), 3);
```

## Data Structures

### STL Containers

| Container | Access | Insert | Use Case |
|-----------|--------|--------|----------|
| `vector` | O(1) | O(n)* | Default choice |
| `deque` | O(1) | O(1) ends | Double-ended |
| `list` | O(n) | O(1) | Frequent insert |
| `set` | O(log n) | O(log n) | Unique sorted |
| `unordered_set` | O(1) | O(1) | Fast lookup |
| `map` | O(log n) | O(log n) | Key-value |
| `unordered_map` | O(1) | O(1) | Fast key-value |

## Graph Algorithms

```cpp
// BFS - Breadth First Search
void bfs(int start, vector<vector<int>>& adj) {
    queue<int> q;
    vector<bool> visited(adj.size(), false);
    q.push(start);
    visited[start] = true;

    while (!q.empty()) {
        int node = q.front(); q.pop();
        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
}
```

## Dynamic Programming

```cpp
// Fibonacci with memoization
int fib(int n, vector<int>& memo) {
    if (n <= 1) return n;
    if (memo[n] != -1) return memo[n];
    return memo[n] = fib(n-1, memo) + fib(n-2, memo);
}
```

---

*C++ Plugin v2.0.0 - Learning Skill*
