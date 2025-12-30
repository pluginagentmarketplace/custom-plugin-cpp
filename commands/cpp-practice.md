---
# ═══════════════════════════════════════════════════════════════════════════════
# COMMAND: cpp-practice
# Version: 3.0.0 | SASMP v1.3.0 Compliant | Production-Grade
# ═══════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# IDENTITY
# ─────────────────────────────────────────────────────────────────────────────
name: cpp-practice
version: "3.0.0"
description: Practice C++ with coding exercises and challenges

# ─────────────────────────────────────────────────────────────────────────────
# CLASSIFICATION
# ─────────────────────────────────────────────────────────────────────────────
category: learning
priority: 2

# ─────────────────────────────────────────────────────────────────────────────
# TOOLS & PERMISSIONS
# ─────────────────────────────────────────────────────────────────────────────
allowed_tools:
  - Read
  - Write
  - Bash

# ─────────────────────────────────────────────────────────────────────────────
# AGENT ROUTING
# ─────────────────────────────────────────────────────────────────────────────
routes_to:
  default: cpp-fundamentals-agent
  difficulty:
    easy: cpp-fundamentals-agent
    medium: cpp-oop-agent
    hard: cpp-algorithms-agent
    interview: cpp-algorithms-agent

# ─────────────────────────────────────────────────────────────────────────────
# INPUT VALIDATION
# ─────────────────────────────────────────────────────────────────────────────
input_schema:
  type: object
  properties:
    difficulty:
      type: string
      required: false
      enum: [easy, medium, hard, interview]
      default: medium
      description: "Challenge difficulty level"
    topic:
      type: string
      required: false
      description: "Specific topic for the exercise"
    count:
      type: integer
      required: false
      default: 1
      minimum: 1
      maximum: 5
      description: "Number of exercises to generate"

# ─────────────────────────────────────────────────────────────────────────────
# EXIT CODES
# ─────────────────────────────────────────────────────────────────────────────
exit_codes:
  0: "Success - exercise completed"
  1: "Exercise skipped"
  2: "Solution incorrect"
  3: "Time limit exceeded"

# ─────────────────────────────────────────────────────────────────────────────
# ERROR HANDLING
# ─────────────────────────────────────────────────────────────────────────────
error_handling:
  on_stuck: "provide_hints"
  on_wrong_answer: "explain_error"
  on_timeout: "suggest_optimization"
  on_skip: "provide_solution"
---

# /cpp-practice

**Learning Command** | Coding Exercises & Challenges

Practice C++ programming with exercises tailored to your skill level.

---

## Usage

```
/cpp-practice [difficulty] [topic] [--count=1]
```

## Arguments

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `difficulty` | string | No | easy, medium, hard, interview |
| `topic` | string | No | Specific topic for exercise |
| `--count` | integer | No | Number of exercises (1-5) |

---

## Difficulty Levels

| Level | Focus | Time | Topics |
|-------|-------|------|--------|
| **Easy** | Fundamentals, syntax | 15-30 min | Variables, loops, functions |
| **Medium** | OOP, STL usage | 30-60 min | Classes, containers, algorithms |
| **Hard** | Advanced patterns | 1-2 hours | Templates, optimization, design |
| **Interview** | Common interview Q's | Varies | LeetCode-style problems |

---

## Examples

```bash
# Random challenge at medium difficulty
/cpp-practice

# Easy fundamentals exercise
/cpp-practice easy

# Hard algorithm problem
/cpp-practice hard algorithms

# STL-focused medium challenge
/cpp-practice medium stl

# Interview preparation
/cpp-practice interview

# Multiple exercises
/cpp-practice medium --count=3
```

---

## Topic Categories

### Fundamentals
- Variables and data types
- Control flow (if, switch, loops)
- Functions and parameters
- Arrays and strings
- Basic I/O

### Object-Oriented Programming
- Class design
- Inheritance hierarchies
- Polymorphism and virtual functions
- Operator overloading
- SOLID principles

### STL & Containers
- Vector operations
- Map and set usage
- Algorithm application
- Iterator patterns
- Custom comparators

### Memory Management
- Pointer arithmetic
- Smart pointer usage
- RAII implementation
- Memory debugging
- Resource management

### Algorithms
- Sorting variations
- Searching techniques
- Graph traversal
- Dynamic programming
- Greedy algorithms

### Modern C++
- Lambda expressions
- Move semantics
- Templates and concepts
- Ranges and views
- Structured bindings

---

## Exercise Format

### 1. Problem Statement
Clear description of what to implement.

### 2. Requirements
```
Input: Vector of integers
Output: Sum of even numbers
Constraints: n <= 10^6, -10^9 <= a[i] <= 10^9
```

### 3. Examples
```
Input:  [1, 2, 3, 4, 5, 6]
Output: 12  // 2 + 4 + 6
```

### 4. Starter Code
```cpp
#include <vector>

int sumEven(const std::vector<int>& nums) {
    // Your implementation here
}
```

### 5. Test Cases
```cpp
assert(sumEven({1, 2, 3, 4}) == 6);
assert(sumEven({}) == 0);
assert(sumEven({1, 3, 5}) == 0);
```

---

## Learning Features

### Hints System
Request hints without seeing the full solution:
- **Hint 1**: Algorithm approach
- **Hint 2**: Data structure suggestion
- **Hint 3**: Partial implementation

### Solution Walk-through
After solving (or giving up):
1. Optimal solution code
2. Step-by-step explanation
3. Complexity analysis
4. Alternative approaches

### Progress Tracking
- Exercises completed
- Success rate by topic
- Time statistics
- Skill level progression

---

## Sample Exercises

### Easy: Reverse String
```cpp
// Reverse a string in-place
void reverse(std::string& s);
// Input: "hello" → Output: "olleh"
```

### Medium: Find Duplicates
```cpp
// Find all duplicate elements in O(n) time
std::vector<int> findDuplicates(std::vector<int>& nums);
// Input: [4,3,2,7,8,2,3,1] → Output: [2,3]
```

### Hard: LRU Cache
```cpp
// Implement LRU Cache with O(1) get and put
class LRUCache {
    LRUCache(int capacity);
    int get(int key);
    void put(int key, int value);
};
```

---

## Commands During Exercise

| Command | Action |
|---------|--------|
| `hint` | Get next hint |
| `solution` | See full solution |
| `skip` | Move to next exercise |
| `test` | Run test cases |
| `submit` | Check your solution |

---

## Error Messages

| Error | Cause | Solution |
|-------|-------|----------|
| "Wrong answer" | Logic error | Review test case that failed |
| "Time limit" | O(n²) or worse | Optimize algorithm |
| "Runtime error" | Crash in code | Check bounds, nulls |
| "Compile error" | Syntax issue | Fix compilation errors |

---

## Integration Points

| Component | Interface |
|-----------|-----------|
| `cpp-fundamentals-agent` | Easy exercises |
| `cpp-oop-agent` | OOP exercises |
| `cpp-algorithms-agent` | Algorithm challenges |
| `stl-master` | STL exercises |

---

*C++ Plugin v3.0.0 - Production-Grade Learning Command*
