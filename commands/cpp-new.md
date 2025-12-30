---
name: cpp-new
description: Create a new C++ project with best-practice structure
allowed-tools: Read, Write, Bash
category: development
---

# /cpp-new

**🔧 Development Mode Command**

Create a new C++ project with modern CMake setup and best-practice structure.

## Project Templates

| Template | Includes |
|----------|----------|
| **cli** | CLI parsing (argparse), logging |
| **lib** | Header-only or static library |
| **app** | GUI application framework |
| **test** | Testing setup with Catch2/GTest |
| **full** | Complete project with all features |

## Usage

```
/cpp-new <project-name> [template]
```

## Examples

```bash
/cpp-new my-tool cli        # CLI application
/cpp-new my-lib lib         # Library project
/cpp-new my-app full        # Full project structure
/cpp-new calculator         # Default structure
```

## Generated Structure

```
my-project/
├── CMakeLists.txt          # Modern CMake 3.20+
├── src/
│   └── main.cpp
├── include/
│   └── my-project/
│       └── core.hpp
├── tests/
│   └── test_main.cpp
├── cmake/
│   └── CompilerWarnings.cmake
├── .clang-format
├── .clang-tidy
├── .gitignore
└── README.md
```

## CMake Features

- C++20 by default
- Compiler warnings enabled
- Sanitizers in debug mode
- CPM.cmake for dependencies
- Testing with CTest

## Quick Start After Creation

```bash
cd my-project
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build
./build/my-project
```

---

*C++ Plugin v2.0.0 - Development Command*
