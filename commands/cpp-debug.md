---
name: cpp-debug
description: Debug C++ code with expert guidance and tools
allowed-tools: Read, Write, Edit, Bash, Grep
category: development
---

# /cpp-debug

**🔧 Development Mode Command**

Access the C++ debugging expert for finding and fixing bugs.

## Debugging Capabilities

| Tool | Purpose |
|------|---------|
| **GDB** | Interactive debugging, breakpoints |
| **LLDB** | macOS/Clang debugging |
| **Valgrind** | Memory leak detection |
| **ASan** | Address sanitizer |
| **TSan** | Thread sanitizer |

## Usage

```
/cpp-debug [issue-description]
```

## Examples

```bash
/cpp-debug                           # Start debugging session
/cpp-debug segfault                  # Debug segmentation fault
/cpp-debug "memory leak"             # Find memory leaks
/cpp-debug "race condition"          # Debug threading issues
/cpp-debug "crash on line 42"        # Debug specific crash
```

## Common Issues Solved

| Problem | Approach |
|---------|----------|
| Segfault | Check null pointers, array bounds |
| Memory leak | Use Valgrind, smart pointers |
| Data race | Use TSan, add synchronization |
| Stack overflow | Reduce recursion depth |
| Use after free | Fix object lifetimes |

## Debugging Workflow

1. **Reproduce** - Make the bug consistent
2. **Isolate** - Find minimal test case
3. **Instrument** - Add breakpoints/logging
4. **Analyze** - Find root cause
5. **Fix** - Apply targeted fix
6. **Verify** - Confirm fix works

## Quick Commands

```bash
# Compile with debug symbols
g++ -g -O0 program.cpp -o program

# Run with GDB
gdb ./program

# Run with Valgrind
valgrind --leak-check=full ./program

# Compile with sanitizers
g++ -fsanitize=address,undefined -g program.cpp
```

---

*C++ Plugin v2.0.0 - Development Command*
