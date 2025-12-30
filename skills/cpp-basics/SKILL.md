---
# ═══════════════════════════════════════════════════════════════════════════════
# SKILL: C++ Basics
# Version: 3.0.0 | SASMP v1.3.0 Compliant | Production-Grade
# ═══════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# IDENTITY
# ─────────────────────────────────────────────────────────────────────────────
name: cpp-basics
version: "3.0.0"
description: >
  Production-grade skill for C++ fundamentals. Covers variables, data types,
  operators, control flow, functions, and program structure. Foundation for
  all C++ development.

# ─────────────────────────────────────────────────────────────────────────────
# COMPLIANCE
# ─────────────────────────────────────────────────────────────────────────────
sasmp_version: "1.3.0"
skill_version: "3.0.0"

# ─────────────────────────────────────────────────────────────────────────────
# BONDING
# ─────────────────────────────────────────────────────────────────────────────
bonded_agent: cpp-fundamentals-agent
bond_type: PRIMARY_BOND
category: learning

# ─────────────────────────────────────────────────────────────────────────────
# PARAMETERS (with validation)
# ─────────────────────────────────────────────────────────────────────────────
parameters:
  topic:
    type: string
    required: true
    enum: [variables, data_types, operators, control_flow, functions, arrays, io]
    description: "Topic to teach or practice"
  skill_level:
    type: string
    required: false
    enum: [beginner, intermediate]
    default: beginner
  output_format:
    type: string
    required: false
    enum: [explanation, code_example, exercise, quiz]
    default: explanation

# ─────────────────────────────────────────────────────────────────────────────
# ERROR HANDLING
# ─────────────────────────────────────────────────────────────────────────────
error_handling:
  retry_logic:
    max_attempts: 3
    backoff: exponential
    initial_delay_ms: 500
    jitter: true
  fallback:
    on_invalid_topic: "suggest_closest_match"
    on_compilation_error: "explain_and_fix"
  recovery:
    steps:
      - "Validate input parameters"
      - "Check for syntax errors in examples"
      - "Verify code compiles"

# ─────────────────────────────────────────────────────────────────────────────
# OBSERVABILITY
# ─────────────────────────────────────────────────────────────────────────────
observability:
  log_level: info
  metrics:
    - topic_requests
    - exercise_completions
    - error_explanations
---

# C++ Basics Skill

**Production-Grade Learning Skill** | Foundation Building

Master the essential building blocks of C++ programming.

---

## Topics Covered

### 1. Variables & Data Types

```cpp
#include <iostream>
#include <cstdint>  // Fixed-width integers

int main() {
    // ─────────────────────────────────────────────────
    // Integer Types (with guaranteed sizes)
    // ─────────────────────────────────────────────────
    int8_t   tiny   = 127;                  // 1 byte, -128 to 127
    int16_t  small  = 32767;                // 2 bytes
    int32_t  normal = 2147483647;           // 4 bytes
    int64_t  large  = 9223372036854775807;  // 8 bytes

    // Unsigned variants
    uint8_t  ubyte  = 255;                  // 0 to 255
    uint32_t ucount = 4294967295;           // 0 to 4B

    // ─────────────────────────────────────────────────
    // Floating Point
    // ─────────────────────────────────────────────────
    float  f = 3.14f;           // ~7 decimal digits
    double d = 3.14159265358979; // ~15 decimal digits

    // ─────────────────────────────────────────────────
    // Character & Boolean
    // ─────────────────────────────────────────────────
    char   c = 'A';       // ASCII character
    bool   b = true;      // true or false

    // ─────────────────────────────────────────────────
    // Modern C++ Initialization (prefer brace init)
    // ─────────────────────────────────────────────────
    int x{42};            // Brace initialization
    auto y = 3.14;        // Type deduction (double)
    auto z{10};           // int

    return 0;
}
```

### 2. Operators

| Category | Operators | Example |
|----------|-----------|---------|
| Arithmetic | `+ - * / %` | `10 / 3 = 3` |
| Comparison | `== != < > <= >=` | `5 == 5` → `true` |
| Logical | `&& \|\| !` | `true && false` → `false` |
| Bitwise | `& \| ^ ~ << >>` | `0xFF & 0x0F` → `0x0F` |
| Assignment | `= += -= *= /=` | `x += 5` |
| Increment | `++ --` | `++i` (prefer prefix) |

### 3. Control Flow

```cpp
// ─────────────────────────────────────────────────────
// Conditionals
// ─────────────────────────────────────────────────────
if (score >= 90) {
    grade = 'A';
} else if (score >= 80) {
    grade = 'B';
} else {
    grade = 'F';
}

// Switch with C++17 init
switch (int x = getValue(); x) {
    case 1:  std::cout << "One\n";  break;
    case 2:  std::cout << "Two\n";  break;
    default: std::cout << "Other\n"; break;
}

// ─────────────────────────────────────────────────────
// Loops
// ─────────────────────────────────────────────────────
// For loop (prefer prefix ++)
for (int i = 0; i < n; ++i) { }

// Range-based for (C++11)
for (const auto& item : container) { }

// While
while (condition) { }

// Do-while (runs at least once)
do { } while (condition);
```

### 4. Functions

```cpp
// ─────────────────────────────────────────────────────
// Function declaration
// ─────────────────────────────────────────────────────
int add(int a, int b);               // Declaration
void greet(std::string_view name);   // string_view for efficiency

// ─────────────────────────────────────────────────────
// Definition with default parameter
// ─────────────────────────────────────────────────────
int add(int a, int b) {
    return a + b;
}

void greet(std::string_view name = "World") {
    std::cout << "Hello, " << name << "!\n";
}

// ─────────────────────────────────────────────────────
// Pass by reference (for modification or large objects)
// ─────────────────────────────────────────────────────
void increment(int& value) {
    ++value;
}

void process(const std::vector<int>& data) {  // const ref for read-only
    for (int x : data) { /* ... */ }
}

// ─────────────────────────────────────────────────────
// Function overloading
// ─────────────────────────────────────────────────────
int max(int a, int b) { return (a > b) ? a : b; }
double max(double a, double b) { return (a > b) ? a : b; }
```

---

## Troubleshooting

### Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `undefined reference` | Missing function definition | Add function body |
| `expected ';'` | Missing semicolon | Check previous line |
| `undeclared identifier` | Variable not declared | Declare before use |
| `narrowing conversion` | Data loss in brace init | Use explicit cast |

### Decision Tree

```
Compilation error?
├── "undefined reference"
│   └── Function declared but not defined → Add definition
├── "expected ';'"
│   └── Missing semicolon → Check line above error
├── "undeclared identifier"
│   └── Variable not in scope → Declare or check spelling
└── "no matching function"
    └── Wrong argument types → Match function signature
```

---

## Unit Test Template

```cpp
#include <cassert>

void test_basics() {
    // Test integer operations
    assert(add(2, 3) == 5);
    assert(add(-1, 1) == 0);

    // Test floating point (with tolerance)
    constexpr double epsilon = 1e-9;
    assert(std::abs(calculateArea(2.0) - 12.566370614) < epsilon);

    // Test boolean logic
    assert((true && false) == false);
    assert((true || false) == true);

    std::cout << "All tests passed!\n";
}
```

---

## Learning Path

```
Week 1: Foundation
├── Day 1-2: Variables & data types
├── Day 3-4: Operators
├── Day 5-6: Control flow
└── Day 7: Practice exercises

Week 2: Functions & Arrays
├── Day 1-2: Functions basics
├── Day 3-4: Arrays & pointers
├── Day 5-6: String handling
└── Day 7: Mini project
```

---

## References

- [C++ Reference](https://en.cppreference.com/w/)
- [Learn C++](https://www.learncpp.com/)
- [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/)

---

*C++ Plugin v3.0.0 - Production-Grade Learning Skill*
