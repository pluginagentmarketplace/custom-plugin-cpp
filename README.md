# C++ Programming System

[![SASMP v1.3.0](https://img.shields.io/badge/SASMP-v1.3.0-blue.svg)](https://github.com/pluginagentmarketplace)
[![C++](https://img.shields.io/badge/C++-11%2F14%2F17%2F20%2F23-orange?logo=cplusplus)](https://isocpp.org)
[![Plugin Type](https://img.shields.io/badge/Type-Hybrid-purple.svg)](https://github.com/pluginagentmarketplace)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Complete C++ Programming System** - Learn AND Develop with expert AI agents. Master fundamentals, OOP, STL, and modern C++ while building real projects.

## Plugin Type: HYBRID

This plugin serves **two purposes**:

| Mode | Purpose | For Who |
|------|---------|---------|
| **Learning** | Understand C++ concepts | Beginners, Students |
| **Development** | Build real C++ projects | Developers, Engineers |

---

## Features Overview

| Category | Count | Items |
|----------|-------|-------|
| **Agents** | 9 | 5 Learning + 4 Development |
| **Skills** | 9 | 5 Learning + 4 Development |
| **Commands** | 6 | 2 Learning + 4 Development |

---

## Learning Mode

### Learning Agents

| Agent | Expertise |
|-------|-----------|
| `cpp-fundamentals-agent` | Variables, types, control flow, functions |
| `cpp-oop-agent` | Classes, inheritance, polymorphism, patterns |
| `memory-specialist` | Pointers, RAII, smart pointers |
| `stl-master` | Containers, algorithms, iterators |
| `cpp-algorithms-agent` | Complexity, sorting, searching, graphs |

### Learning Commands

```bash
/cpp-learn ownership      # Learn about memory ownership
/cpp-learn oop            # Object-oriented programming
/cpp-practice medium stl  # STL exercises
```

### Learning Skills

- **cpp-basics** - C++ fundamentals
- **oop-patterns** - OOP and design patterns
- **memory-management** - Memory safety
- **stl** - Standard Template Library
- **algorithms** - Data structures and algorithms

---

## Development Mode

### Development Agents

| Agent | Purpose |
|-------|---------|
| `modern-cpp-expert` | C++11/14/17/20/23 features |
| `build-engineer` | CMake, Make, Ninja, CI/CD |
| `performance-optimizer` | Profiling, SIMD, threading |
| `cpp-debugger-agent` | GDB, LLDB, sanitizers |

### Development Commands

| Command | Description |
|---------|-------------|
| `/cpp-new` | Create new project with templates |
| `/cpp-debug` | Debug with GDB/LLDB |
| `/cpp-optimize` | Performance profiling |
| `/cpp-review` | Code review |

### Quick Start: Development

```bash
# Create a new CLI project
/cpp-new my-tool cli

# Debug a crash
/cpp-debug segfault

# Optimize performance
/cpp-optimize profile

# Review code
/cpp-review class
```

---

## Plugin Structure

```
custom-plugin-cpp/
├── agents/
│   ├── cpp-fundamentals-agent.md   # Learning
│   ├── cpp-oop-agent.md            # Learning
│   ├── 02-memory-specialist.md     # Learning
│   ├── 03-stl-master.md            # Learning
│   ├── cpp-algorithms-agent.md     # Learning
│   ├── 01-modern-cpp-expert.md     # Development
│   ├── 04-build-engineer.md        # Development
│   ├── 05-performance-optimizer.md # Development
│   └── cpp-debugger-agent.md       # Development
├── skills/
│   ├── cpp-basics/                 # Learning
│   ├── oop-patterns/               # Learning
│   ├── memory-management/          # Learning
│   ├── stl/                        # Learning
│   ├── algorithms/                 # Learning
│   ├── modern-cpp/                 # Development
│   ├── build-systems/              # Development
│   ├── performance/                # Development
│   └── debugging/                  # Development
├── commands/
│   ├── cpp-learn.md                # Learning
│   ├── cpp-practice.md             # Learning
│   ├── cpp-debug.md                # Development
│   ├── cpp-optimize.md             # Development
│   ├── cpp-review.md               # Development
│   └── cpp-new.md                  # Development
├── hooks/
│   └── hooks.json
└── .claude-plugin/
    ├── plugin.json
    └── marketplace.json
```

---

## Topics Covered

### Core Concepts (Learning)
- Variables, Data Types, Operators
- Control Flow, Functions
- Classes, Inheritance, Polymorphism
- Pointers, References, Smart Pointers
- STL Containers and Algorithms
- Algorithm Complexity Analysis

### Development Skills
- Modern C++ (C++11 through C++23)
- CMake and Build Systems
- Profiling and Optimization
- Debugging with GDB/LLDB
- Code Review Best Practices

---

## Installation

```bash
# Via Claude Code plugin marketplace
/plugin install custom-plugin-cpp
```

---

## Usage Examples

### Learning Flow
```bash
# 1. Start learning
/cpp-learn fundamentals

# 2. Practice with exercises
/cpp-practice easy

# 3. Move to OOP
/cpp-learn oop
```

### Development Flow
```bash
# 1. Create project
/cpp-new my-app cli

# 2. Write code, then review
/cpp-review

# 3. Debug issues
/cpp-debug

# 4. Optimize performance
/cpp-optimize
```

---

## Version History

| Version | Date | Type | Changes |
|---------|------|------|---------|
| 2.0.0 | 2025-12-29 | Hybrid | Merged cpp + cpp-developer, added 4 agents, 4 skills, 6 commands |
| 1.0.0 | 2025-12-29 | Development | Initial version with 5 agents, 5 skills |

---

## Related Resources

- [C++ Reference](https://en.cppreference.com/)
- [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/)
- [Learn C++](https://www.learncpp.com/)

---

## License

MIT License - See [LICENSE](LICENSE) for details.

## Author

Plugin Agent Marketplace - [pluginagentmarketplace@gmail.com](mailto:pluginagentmarketplace@gmail.com)
