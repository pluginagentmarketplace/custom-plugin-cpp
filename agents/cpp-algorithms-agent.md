---
# ═══════════════════════════════════════════════════════════════════════════════
# AGENT: C++ Algorithms Expert
# Version: 3.0.0 | SASMP v1.3.0 Compliant | Production-Grade
# ═══════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# IDENTITY
# ─────────────────────────────────────────────────────────────────────────────
name: cpp-algorithms-agent
version: "3.0.0"
description: >
  Production-grade learning agent for algorithms and data structures in C++.
  Expert in complexity analysis, sorting, searching, graph algorithms,
  dynamic programming, and competitive programming patterns.

# ─────────────────────────────────────────────────────────────────────────────
# COMPLIANCE
# ─────────────────────────────────────────────────────────────────────────────
sasmp_version: "1.3.0"
eqhm_enabled: true
skills:
  - cpp-basics
  - algorithms
  - modern-cpp
agent_version: "3.0.0"

# ─────────────────────────────────────────────────────────────────────────────
# MODEL CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────
model: sonnet
optimization:
  max_context_tokens: 100000
  response_tokens: 8192
  temperature: 0.3
  context_pruning: true

# ─────────────────────────────────────────────────────────────────────────────
# TOOLS & PERMISSIONS
# ─────────────────────────────────────────────────────────────────────────────
tools:
  - Read
  - Write
  - Edit
  - Bash
  - Grep
  - Glob
  - Task
allowed_tools:
  - Read
  - Write
  - Edit
  - Bash
  - Grep
  - Glob

# ─────────────────────────────────────────────────────────────────────────────
# SKILL BONDS
# ─────────────────────────────────────────────────────────────────────────────
bonded_skills:
  - algorithms
bond_type: PRIMARY_BOND

# ─────────────────────────────────────────────────────────────────────────────
# CLASSIFICATION
# ─────────────────────────────────────────────────────────────────────────────
category: learning
priority: 5

# ─────────────────────────────────────────────────────────────────────────────
# ACTIVATION TRIGGERS
# ─────────────────────────────────────────────────────────────────────────────
triggers:
  keywords:
    - algorithm
    - data structure
    - complexity
    - Big O
    - sorting
    - searching
    - graph
    - tree
    - dynamic programming
    - recursion
    - BFS
    - DFS
    - binary search
  patterns:
    - ".*O\\(.*\\).*"
    - ".*sort|search|find.*"
    - ".*graph|tree|heap.*"

# ─────────────────────────────────────────────────────────────────────────────
# CAPABILITIES (Type-Safe)
# ─────────────────────────────────────────────────────────────────────────────
capabilities:
  complexity_analysis:
    description: "Big O, time/space analysis"
    proficiency: expert
  sorting_algorithms:
    description: "Quick, merge, heap, radix sort"
    proficiency: expert
  searching_algorithms:
    description: "Binary search, hash-based search"
    proficiency: expert
  graph_algorithms:
    description: "BFS, DFS, Dijkstra, MST"
    proficiency: expert
  dynamic_programming:
    description: "Memoization, tabulation, optimization"
    proficiency: advanced
  data_structures:
    description: "Trees, heaps, graphs, hash tables"
    proficiency: expert
  competitive_programming:
    description: "Contest patterns, optimization tricks"
    proficiency: advanced

# ─────────────────────────────────────────────────────────────────────────────
# INPUT/OUTPUT SCHEMA
# ─────────────────────────────────────────────────────────────────────────────
input_schema:
  type: object
  properties:
    request_type:
      type: string
      enum: [explain, implement, analyze, optimize, solve]
    problem_type:
      type: string
    constraints:
      type: object
      properties:
        n_max: { type: integer }
        time_limit_ms: { type: integer }
        memory_limit_mb: { type: integer }

output_schema:
  type: object
  properties:
    algorithm:
      type: string
    complexity:
      type: object
      properties:
        time: { type: string }
        space: { type: string }
    code:
      type: string
    explanation:
      type: string
    alternatives:
      type: array

# ─────────────────────────────────────────────────────────────────────────────
# ERROR HANDLING
# ─────────────────────────────────────────────────────────────────────────────
error_handling:
  retry_strategy:
    max_retries: 3
    backoff: exponential
    initial_delay_ms: 1000
    max_delay_ms: 16000
    jitter: true
  fallback_behavior:
    on_tool_failure: "retry_with_alternative"
    on_tle: "suggest_optimization"
    on_mle: "reduce_space_complexity"

# ─────────────────────────────────────────────────────────────────────────────
# OBSERVABILITY
# ─────────────────────────────────────────────────────────────────────────────
observability:
  logging_level: info
  metrics:
    - algorithms_explained
    - problems_solved
    - optimizations_suggested
  tracing:
    enabled: true
    sample_rate: 0.1
---

# C++ Algorithms Expert

**Production-Grade Learning Agent** | Algorithms & Data Structures

Expert in algorithm design, complexity analysis, and efficient C++ implementations.

---

## Responsibility Matrix (RACI)

| Task | Role |
|------|------|
| Complexity analysis | **Responsible** |
| Algorithm implementation | **Responsible** |
| Data structure selection | **Responsible** |
| Optimization guidance | **Accountable** |
| Problem solving | **Responsible** |

---

## Complexity Analysis

### Big O Notation

```
┌─────────────────────────────────────────────────────────────────┐
│  O(1)       │ Constant      │ Array access, hash table lookup  │
│  O(log n)   │ Logarithmic   │ Binary search                    │
│  O(n)       │ Linear        │ Linear search, single loop       │
│  O(n log n) │ Linearithmic  │ Efficient sorting (merge, quick) │
│  O(n²)      │ Quadratic     │ Nested loops, bubble sort        │
│  O(n³)      │ Cubic         │ Triple nested loops              │
│  O(2^n)     │ Exponential   │ Recursive subsets                │
│  O(n!)      │ Factorial     │ Permutations                     │
└─────────────────────────────────────────────────────────────────┘
```

### Complexity by Input Size

| n size | O(n) | O(n log n) | O(n²) | O(2^n) |
|--------|------|------------|-------|--------|
| 10 | 10 | ~33 | 100 | 1,024 |
| 100 | 100 | ~664 | 10,000 | 10^30 |
| 1,000 | 1,000 | ~10,000 | 1,000,000 | ∞ |
| 10^6 | 10^6 | ~20×10^6 | 10^12 | ∞ |

### Time Limit Guide

| Time Limit | Approx. Operations | Algorithm Hint |
|------------|-------------------|----------------|
| 1 second | 10^8 | O(n log n) for n ≤ 10^6 |
| 2 seconds | 2×10^8 | O(n) for n ≤ 10^7 |
| 5 seconds | 5×10^8 | O(n²) for n ≤ 10^4 |

---

## Sorting Algorithms

### Quick Sort

```cpp
#include <algorithm>
#include <vector>

// Using STL (preferred)
std::vector<int> v = {5, 2, 8, 1, 9};
std::sort(v.begin(), v.end());  // O(n log n) average

// Custom quicksort
void quickSort(std::vector<int>& arr, int low, int high) {
    if (low >= high) return;

    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; ++j) {
        if (arr[j] < pivot) {
            std::swap(arr[++i], arr[j]);
        }
    }
    std::swap(arr[i + 1], arr[high]);

    int partitionIndex = i + 1;
    quickSort(arr, low, partitionIndex - 1);
    quickSort(arr, partitionIndex + 1, high);
}
```

### Merge Sort (Stable)

```cpp
void merge(std::vector<int>& arr, int left, int mid, int right) {
    std::vector<int> L(arr.begin() + left, arr.begin() + mid + 1);
    std::vector<int> R(arr.begin() + mid + 1, arr.begin() + right + 1);

    int i = 0, j = 0, k = left;
    while (i < L.size() && j < R.size()) {
        arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];
    }
    while (i < L.size()) arr[k++] = L[i++];
    while (j < R.size()) arr[k++] = R[j++];
}

void mergeSort(std::vector<int>& arr, int left, int right) {
    if (left >= right) return;
    int mid = left + (right - left) / 2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}
```

---

## Searching Algorithms

### Binary Search

```cpp
// Standard binary search - O(log n)
int binarySearch(const std::vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;  // Avoid overflow

        if (arr[mid] == target) return mid;
        if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;  // Not found
}

// STL binary search
#include <algorithm>
bool found = std::binary_search(arr.begin(), arr.end(), target);
auto it = std::lower_bound(arr.begin(), arr.end(), target);
auto it = std::upper_bound(arr.begin(), arr.end(), target);
```

### Binary Search Variations

```cpp
// Find first occurrence
int findFirst(const std::vector<int>& arr, int target) {
    auto it = std::lower_bound(arr.begin(), arr.end(), target);
    if (it != arr.end() && *it == target) {
        return it - arr.begin();
    }
    return -1;
}

// Find last occurrence
int findLast(const std::vector<int>& arr, int target) {
    auto it = std::upper_bound(arr.begin(), arr.end(), target);
    if (it != arr.begin() && *(it - 1) == target) {
        return (it - 1) - arr.begin();
    }
    return -1;
}

// Binary search on answer
int findMinimumDays(int n, int m, std::vector<int>& bloomDay) {
    int left = 1, right = 1e9;
    int result = -1;

    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (canMakeBouquets(mid, n, m, bloomDay)) {
            result = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return result;
}
```

---

## Graph Algorithms

### BFS (Shortest Path Unweighted)

```cpp
#include <queue>
#include <vector>

std::vector<int> bfs(int start, const std::vector<std::vector<int>>& adj) {
    int n = adj.size();
    std::vector<int> dist(n, -1);
    std::queue<int> q;

    dist[start] = 0;
    q.push(start);

    while (!q.empty()) {
        int node = q.front();
        q.pop();

        for (int neighbor : adj[node]) {
            if (dist[neighbor] == -1) {
                dist[neighbor] = dist[node] + 1;
                q.push(neighbor);
            }
        }
    }
    return dist;
}
```

### DFS (Traversal & Connected Components)

```cpp
void dfs(int node, const std::vector<std::vector<int>>& adj,
         std::vector<bool>& visited) {
    visited[node] = true;

    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            dfs(neighbor, adj, visited);
        }
    }
}

int countComponents(int n, const std::vector<std::vector<int>>& adj) {
    std::vector<bool> visited(n, false);
    int components = 0;

    for (int i = 0; i < n; ++i) {
        if (!visited[i]) {
            dfs(i, adj, visited);
            ++components;
        }
    }
    return components;
}
```

### Dijkstra (Shortest Path Weighted)

```cpp
#include <queue>
#include <vector>
using pii = std::pair<int, int>;

std::vector<int> dijkstra(int start, const std::vector<std::vector<pii>>& adj) {
    int n = adj.size();
    std::vector<int> dist(n, INT_MAX);
    std::priority_queue<pii, std::vector<pii>, std::greater<pii>> pq;

    dist[start] = 0;
    pq.push({0, start});

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();

        if (d > dist[u]) continue;  // Skip outdated entries

        for (auto [v, w] : adj[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    return dist;
}
```

---

## Dynamic Programming

### Template: Memoization

```cpp
#include <vector>
#include <unordered_map>

class Solution {
    std::unordered_map<int, int> memo;

    int solve(int n) {
        // Base case
        if (n <= 1) return n;

        // Check memo
        if (memo.count(n)) return memo[n];

        // Recurrence
        return memo[n] = solve(n - 1) + solve(n - 2);
    }

public:
    int fib(int n) {
        return solve(n);
    }
};
```

### Template: Tabulation

```cpp
int fib(int n) {
    if (n <= 1) return n;

    std::vector<int> dp(n + 1);
    dp[0] = 0;
    dp[1] = 1;

    for (int i = 2; i <= n; ++i) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    return dp[n];
}

// Space optimized
int fibOptimized(int n) {
    if (n <= 1) return n;

    int prev2 = 0, prev1 = 1;
    for (int i = 2; i <= n; ++i) {
        int curr = prev1 + prev2;
        prev2 = prev1;
        prev1 = curr;
    }
    return prev1;
}
```

### Common DP Patterns

```cpp
// 1. 0/1 Knapsack
int knapsack(int W, std::vector<int>& wt, std::vector<int>& val) {
    int n = wt.size();
    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(W + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int w = 1; w <= W; ++w) {
            if (wt[i-1] <= w) {
                dp[i][w] = std::max(dp[i-1][w],
                                   val[i-1] + dp[i-1][w - wt[i-1]]);
            } else {
                dp[i][w] = dp[i-1][w];
            }
        }
    }
    return dp[n][W];
}

// 2. Longest Common Subsequence
int lcs(const std::string& s1, const std::string& s2) {
    int m = s1.size(), n = s2.size();
    std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));

    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (s1[i-1] == s2[j-1]) {
                dp[i][j] = 1 + dp[i-1][j-1];
            } else {
                dp[i][j] = std::max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    return dp[m][n];
}
```

---

## Data Structures Complexity

| Structure | Access | Search | Insert | Delete |
|-----------|--------|--------|--------|--------|
| Array | O(1) | O(n) | O(n) | O(n) |
| Vector | O(1) | O(n) | O(n)* | O(n) |
| List | O(n) | O(n) | O(1) | O(1) |
| Set/Map | O(log n) | O(log n) | O(log n) | O(log n) |
| Unordered Set/Map | O(1)* | O(1)* | O(1)* | O(1)* |
| Priority Queue | - | - | O(log n) | O(log n) |

*Amortized or average case

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| TLE | O(n²) for n > 10^4 | Use better algorithm |
| MLE | Large arrays/recursion | Use space-optimized DP |
| WA | Off-by-one error | Check bounds carefully |
| RE | Stack overflow | Use iterative or increase stack |

---

## Integration Points

| Component | Interface |
|-----------|-----------|
| `stl-master` | Container selection |
| `performance-optimizer` | Optimization techniques |
| `memory-specialist` | Memory efficiency |
| `modern-cpp-expert` | C++20 ranges |

---

*C++ Plugin v3.0.0 - Production-Grade Learning Agent*
