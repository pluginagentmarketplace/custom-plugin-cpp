---
name: debugging
description: Master C++ debugging - GDB, LLDB, sanitizers, memory debugging, and crash analysis
sasmp_version: "1.3.0"
bonded_agent: cpp-debugger-agent
bond_type: PRIMARY_BOND
version: "1.0.0"
category: development
---

# Debugging Skill

**🔧 Development Skill - Debugging & Error Fixing**

Master C++ debugging tools and techniques.

## Debugging Tools

### GDB (GNU Debugger)

```bash
# Compile with debug symbols
g++ -g -O0 program.cpp -o program

# Start GDB
gdb ./program

# Common commands
(gdb) run              # Start execution
(gdb) break main       # Set breakpoint at main
(gdb) break file.cpp:42  # Breakpoint at line
(gdb) next             # Step over
(gdb) step             # Step into
(gdb) print variable   # Print value
(gdb) backtrace        # Show call stack
(gdb) continue         # Continue execution
(gdb) watch variable   # Watch for changes
(gdb) quit             # Exit
```

### LLDB (macOS/Clang)

```bash
lldb ./program

(lldb) breakpoint set --name main
(lldb) run
(lldb) frame variable     # Local variables
(lldb) thread backtrace   # Call stack
(lldb) expression var     # Print/modify
```

## Sanitizers

### AddressSanitizer (ASan)

```bash
# Compile with ASan
g++ -fsanitize=address -g program.cpp -o program

# Detects:
# - Heap/stack buffer overflow
# - Use after free
# - Double free
# - Memory leaks
```

### UndefinedBehaviorSanitizer

```bash
g++ -fsanitize=undefined -g program.cpp
# Detects: signed overflow, null deref, etc.
```

### ThreadSanitizer

```bash
g++ -fsanitize=thread -g program.cpp
# Detects: data races
```

## Memory Debugging

### Valgrind

```bash
# Memory leak detection
valgrind --leak-check=full ./program

# Detailed memory errors
valgrind --track-origins=yes ./program
```

## Common Issues

| Issue | Symptoms | Tools | Fix |
|-------|----------|-------|-----|
| Segfault | Crash, SIGSEGV | GDB, ASan | Check pointers |
| Memory leak | Growing memory | Valgrind | Use RAII |
| Data race | Random behavior | TSan | Add mutex |
| Buffer overflow | Corruption | ASan | Check bounds |
| Use after free | Crash | ASan | Fix lifetime |

## Debugging Workflow

1. **Reproduce** - Make consistent
2. **Isolate** - Minimal test case
3. **Instrument** - Add breakpoints
4. **Analyze** - Find root cause
5. **Fix** - Targeted fix
6. **Verify** - Confirm and test

---

*C++ Plugin v2.0.0 - Development Skill*
