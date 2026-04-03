---
name: cpp-basics
description: >
  Writes, explains, and debugs beginner-to-intermediate C++ code covering variables,
  data types, operators, control flow, functions, arrays, and I/O. Generates working
  code examples, fixes compilation errors, and creates exercises with tests.
  Use when the user asks to write a C++ program, learn C++ syntax, debug a .cpp file,
  understand C++ fundamentals, or practice with C++ exercises.
  Trigger terms: C++ basics, learn C++, beginner C++, write C++ code, .cpp, g++,
  compilation error, C++ syntax, C++ exercise, C++ variables, C++ functions.
---

# C++ Basics Skill

## Workflow

When the user requests help with C++ fundamentals, follow these steps:

1. **Identify the task type**: Is this a code-writing request, a debugging request, an explanation, or an exercise?
2. **Write or fix the code** using the conventions below.
3. **Validate** the output against the checklist before presenting it.
4. **If debugging**: use the error-resolution guide to diagnose and fix the issue.

## Conventions

Apply these project-specific rules to all generated C++ code:

- Target **C++17** (`-std=c++17`).
- Use **brace initialization** (`int x{42};`) over `=` where possible.
- Prefer `std::string_view` for read-only string parameters.
- Pass large or non-trivial objects by **const reference**.
- Use **prefix increment** (`++i`) in loops.
- Use **range-based for** loops when iterating containers.
- Always include the required headers; do not rely on transitive includes.
- All examples must compile cleanly with `-Wall -Wextra -Werror`.

## Error Resolution Guide

When the user shares a compilation error, follow this decision tree:

```
Compilation error?
 ├─ "undefined reference"  → Missing function definition. Add the function body or link the correct translation unit.
 ├─ "expected ';'"         → Missing semicolon. Check the line immediately above the error.
 ├─ "undeclared identifier" → Variable not in scope. Declare it or fix the spelling.
 ├─ "no matching function"  → Argument types don't match. Cast or correct the arguments.
 └─ "narrowing conversion"  → Data loss in brace init. Use an explicit static_cast.
```

If the error is not listed above, read the full compiler message, identify the source line, and explain the root cause before proposing a fix.

## Validation Checklist

Before presenting any code to the user, verify:

- [ ] All variables initialized before use
- [ ] `#include` directives match every used type and function
- [ ] No signed/unsigned comparison warnings
- [ ] No missing `break` in switch statements
- [ ] Code compiles with `-Wall -Wextra -std=c++17` without warnings

## Testing Pattern

When generating exercises or verifiable code, include a lightweight test block:

```cpp
#include <cassert>
#include <cmath>
#include <iostream>

void run_tests() {
    assert(add(2, 3) == 5);
    assert(add(-1, 1) == 0);
    constexpr double eps = 1e-9;
    assert(std::abs(area(2.0) - 12.566370614) < eps);
    std::cout << "All tests passed.\n";
}
```

## References

- @references/GUIDE.md for extended usage guidance
- @references/PATTERNS.md for design patterns and anti-patterns
