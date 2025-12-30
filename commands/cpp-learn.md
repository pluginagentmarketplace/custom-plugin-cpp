---
# ═══════════════════════════════════════════════════════════════════════════════
# COMMAND: cpp-learn
# Version: 3.0.0 | SASMP v1.3.0 Compliant | Production-Grade
# ═══════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# IDENTITY
# ─────────────────────────────────────────────────────────────────────────────
name: cpp-learn
version: "3.0.0"
description: Start interactive C++ learning session with expert guidance

# ─────────────────────────────────────────────────────────────────────────────
# CLASSIFICATION
# ─────────────────────────────────────────────────────────────────────────────
category: learning
priority: 1

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
  topics:
    fundamentals: cpp-fundamentals-agent
    basics: cpp-fundamentals-agent
    oop: cpp-oop-agent
    classes: cpp-oop-agent
    inheritance: cpp-oop-agent
    memory: memory-specialist
    pointers: memory-specialist
    "smart pointers": memory-specialist
    stl: stl-master
    containers: stl-master
    algorithms: cpp-algorithms-agent
    "data structures": cpp-algorithms-agent
    modern: modern-cpp-expert
    "c++20": modern-cpp-expert
    templates: modern-cpp-expert

# ─────────────────────────────────────────────────────────────────────────────
# INPUT VALIDATION
# ─────────────────────────────────────────────────────────────────────────────
input_schema:
  type: object
  properties:
    topic:
      type: string
      required: false
      description: "Learning topic to focus on"
    level:
      type: string
      required: false
      enum: [beginner, intermediate, advanced]
      default: intermediate
      description: "Skill level for content adaptation"
    style:
      type: string
      required: false
      enum: [conceptual, hands-on, visual, mixed]
      default: mixed
      description: "Preferred learning style"

# ─────────────────────────────────────────────────────────────────────────────
# EXIT CODES
# ─────────────────────────────────────────────────────────────────────────────
exit_codes:
  0: "Success - learning session completed"
  1: "Unknown topic requested"
  2: "Agent routing failed"

# ─────────────────────────────────────────────────────────────────────────────
# ERROR HANDLING
# ─────────────────────────────────────────────────────────────────────────────
error_handling:
  on_unknown_topic: "suggest_similar_topics"
  on_routing_fail: "use_fundamentals_agent"
  on_level_mismatch: "adjust_content_complexity"
---

# /cpp-learn

**Learning Command** | Interactive C++ Education

Launch an expert-guided learning session for any C++ topic.

---

## Usage

```
/cpp-learn [topic] [--level=intermediate] [--style=mixed]
```

## Arguments

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `topic` | string | No | Specific topic to learn |
| `--level` | string | No | beginner, intermediate, advanced |
| `--style` | string | No | conceptual, hands-on, visual, mixed |

---

## Topic Routing

| Topic Keywords | Routes To | Focus |
|----------------|-----------|-------|
| fundamentals, basics, syntax | `cpp-fundamentals-agent` | Core language |
| oop, classes, inheritance | `cpp-oop-agent` | Object-oriented |
| memory, pointers, RAII | `memory-specialist` | Memory management |
| stl, containers, iterators | `stl-master` | Standard library |
| algorithms, complexity | `cpp-algorithms-agent` | Data structures |
| modern, c++20, concepts | `modern-cpp-expert` | Modern features |

---

## Examples

```bash
# General learning session (starts with fundamentals)
/cpp-learn

# Specific topic
/cpp-learn pointers
/cpp-learn "smart pointers"
/cpp-learn oop
/cpp-learn stl

# With level specification
/cpp-learn templates --level=advanced
/cpp-learn basics --level=beginner

# With learning style
/cpp-learn algorithms --style=hands-on
/cpp-learn memory --style=visual
```

---

## Learning Curriculum

### Beginner Track
```
1. Variables & Data Types
2. Control Flow (if, loops)
3. Functions & Parameters
4. Arrays & Strings
5. Introduction to Pointers
6. Basic I/O Operations
```

### Intermediate Track
```
1. Classes & Objects
2. Inheritance & Polymorphism
3. Smart Pointers & RAII
4. STL Containers
5. STL Algorithms
6. Error Handling
```

### Advanced Track
```
1. Templates & Metaprogramming
2. Move Semantics
3. Concepts & Constraints
4. Ranges & Views
5. Coroutines
6. Performance Optimization
```

---

## Teaching Approach

### 1. Concept Explanation
Clear, concise explanation of the concept with real-world analogies.

### 2. Code Demonstration
```cpp
// Example with best practices
auto widget = std::make_unique<Widget>();
widget->process();
// No manual delete needed - RAII handles cleanup
```

### 3. Common Mistakes
```cpp
// ❌ DON'T: Raw new without delete
Widget* w = new Widget();  // Memory leak risk!

// ✅ DO: Use smart pointers
auto w = std::make_unique<Widget>();
```

### 4. Practice Suggestions
- Try implementing the concept yourself
- Modify the example to explore edge cases
- Use `/cpp-practice` for hands-on exercises

---

## Skill Assessment

| Level | Characteristics |
|-------|-----------------|
| **Beginner** | New to C++, familiar with basic programming |
| **Intermediate** | Comfortable with OOP, learning STL |
| **Advanced** | Exploring templates, optimization, modern C++ |

---

## Session Features

- **Interactive Q&A**: Ask follow-up questions anytime
- **Code Examples**: Working code you can compile and run
- **Visualizations**: Diagrams for complex concepts
- **Progress Tracking**: Build on previous sessions
- **Practice Links**: Connected to `/cpp-practice` for exercises

---

## Error Messages

| Error | Cause | Solution |
|-------|-------|----------|
| "Unknown topic" | Topic not recognized | Use suggested alternatives |
| "Level mismatch" | Content too advanced/basic | Adjust --level parameter |

---

## Integration Points

| Component | Interface |
|-----------|-----------|
| `cpp-fundamentals-agent` | Basic concepts |
| `cpp-oop-agent` | OOP patterns |
| `memory-specialist` | Memory management |
| `stl-master` | STL education |
| `cpp-algorithms-agent` | Algorithm design |
| `modern-cpp-expert` | Modern C++ features |

---

*C++ Plugin v3.0.0 - Production-Grade Learning Command*
