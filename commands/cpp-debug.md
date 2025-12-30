---
# ═══════════════════════════════════════════════════════════════════════════════
# COMMAND: cpp-debug
# Version: 3.0.0 | SASMP v1.3.0 Compliant | Production-Grade
# ═══════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# IDENTITY
# ─────────────────────────────────────────────────────────────────────────────
name: cpp-debug
version: "3.0.0"
description: Debug C++ code with expert guidance and professional tools

# ─────────────────────────────────────────────────────────────────────────────
# CLASSIFICATION
# ─────────────────────────────────────────────────────────────────────────────
category: development
priority: 2

# ─────────────────────────────────────────────────────────────────────────────
# TOOLS & PERMISSIONS
# ─────────────────────────────────────────────────────────────────────────────
allowed_tools:
  - Read
  - Write
  - Edit
  - Bash
  - Grep
  - Glob

# ─────────────────────────────────────────────────────────────────────────────
# AGENT ROUTING
# ─────────────────────────────────────────────────────────────────────────────
routes_to: cpp-debugger-agent
fallback_agent: modern-cpp-expert

# ─────────────────────────────────────────────────────────────────────────────
# INPUT VALIDATION
# ─────────────────────────────────────────────────────────────────────────────
input_schema:
  type: object
  properties:
    issue:
      type: string
      required: false
      description: "Description of the bug or issue"
    type:
      type: string
      required: false
      enum: [crash, memory, logic, performance, concurrency, undefined]
      description: "Category of the issue"
    file:
      type: string
      required: false
      description: "File path to focus debugging on"

# ─────────────────────────────────────────────────────────────────────────────
# EXIT CODES
# ─────────────────────────────────────────────────────────────────────────────
exit_codes:
  0: "Success - issue resolved"
  1: "Issue identified but not resolved"
  2: "Unable to reproduce issue"
  3: "Debugging tools unavailable"
  4: "Source file not found"

# ─────────────────────────────────────────────────────────────────────────────
# ERROR HANDLING
# ─────────────────────────────────────────────────────────────────────────────
error_handling:
  on_no_repro: "request_more_context"
  on_tool_missing: "suggest_installation"
  on_complex_issue: "break_into_steps"
  on_heisenbug: "add_instrumentation"
---

# /cpp-debug

**Development Command** | Expert C++ Debugging

Professional debugging assistance with GDB, LLDB, sanitizers, and Valgrind.

---

## Usage

```
/cpp-debug [issue-description] [--type=crash] [--file=path]
```

## Arguments

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `issue` | string | No | Description of the problem |
| `--type` | string | No | crash, memory, logic, performance, concurrency |
| `--file` | string | No | Specific file to debug |

---

## Issue Types

| Type | Symptoms | Primary Tools |
|------|----------|---------------|
| **crash** | Segfault, SIGABRT | GDB, ASan |
| **memory** | Leaks, corruption | Valgrind, ASan |
| **logic** | Wrong output | GDB, logging |
| **performance** | Slow execution | perf, callgrind |
| **concurrency** | Races, deadlocks | TSan, GDB threads |

---

## Examples

```bash
# General debugging session
/cpp-debug

# Specific issue
/cpp-debug "segfault on line 42"
/cpp-debug "memory leak in process()"
/cpp-debug "race condition" --type=concurrency

# Debug specific file
/cpp-debug --file=src/parser.cpp

# Crash debugging
/cpp-debug --type=crash "crash when input is empty"
```

---

## Debugging Workflow

```
┌─────────────┐    ┌──────────────┐    ┌───────────────┐
│  REPRODUCE  │───▶│   ISOLATE    │───▶│  INSTRUMENT   │
│  (confirm)  │    │  (minimize)  │    │  (observe)    │
└─────────────┘    └──────────────┘    └───────────────┘
       │                                      │
       ▼                                      ▼
┌─────────────┐    ┌──────────────┐    ┌───────────────┐
│   VERIFY    │◀───│     FIX      │◀───│   ANALYZE     │
│   (test)    │    │  (correct)   │    │ (root cause)  │
└─────────────┘    └──────────────┘    └───────────────┘
```

---

## Tool Reference

### GDB Commands
```gdb
run                    # Start program
break main             # Set breakpoint
break file.cpp:42      # Breakpoint at line
next (n)               # Step over
step (s)               # Step into
print var              # Show variable
backtrace (bt)         # Call stack
info locals            # Local variables
watch var              # Break on change
```

### Sanitizer Flags
```bash
# AddressSanitizer (memory errors)
g++ -fsanitize=address -g program.cpp

# UndefinedBehaviorSanitizer
g++ -fsanitize=undefined -g program.cpp

# ThreadSanitizer (data races)
g++ -fsanitize=thread -g program.cpp

# Combined
g++ -fsanitize=address,undefined -g -O1 program.cpp
```

### Valgrind
```bash
# Memory leak check
valgrind --leak-check=full ./program

# Detailed with origins
valgrind --leak-check=full --track-origins=yes ./program

# Cache profiling
valgrind --tool=cachegrind ./program
```

---

## Common Issues

| Issue | Symptoms | Diagnosis | Fix |
|-------|----------|-----------|-----|
| Null dereference | SIGSEGV at low address | Check pointer before use | Add null checks |
| Buffer overflow | Corruption, random crash | Run with ASan | Fix bounds |
| Use after free | Random crash, corruption | ASan/Valgrind | Fix lifetimes |
| Memory leak | Growing memory | Valgrind | Use RAII/smart pointers |
| Data race | Inconsistent behavior | TSan | Add synchronization |
| Deadlock | Program hangs | GDB thread info | Fix lock ordering |
| Stack overflow | SIGSEGV in deep call | Check recursion | Reduce depth |
| Integer overflow | Wrong calculation | UBSan | Use checked math |

---

## Quick Diagnosis

```bash
# Compile with debug info
g++ -g -O0 program.cpp -o program

# Quick backtrace from crash
gdb -batch -ex "run" -ex "bt" ./program

# Memory check
valgrind --leak-check=full ./program 2>&1 | head -50

# Check for undefined behavior
g++ -fsanitize=undefined -g program.cpp && ./a.out
```

---

## Debug Checklist

### Before Debugging
- [ ] Can you reproduce the issue consistently?
- [ ] Is the code compiled with `-g -O0`?
- [ ] Do you have a minimal test case?

### During Debugging
- [ ] Where exactly does it crash/fail?
- [ ] What are the variable values at that point?
- [ ] What's the call stack?

### After Fix
- [ ] Does the fix address the root cause?
- [ ] Are there similar bugs elsewhere?
- [ ] Did you add a regression test?

---

## Error Messages

| Error | Cause | Solution |
|-------|-------|----------|
| "Cannot reproduce" | Issue is intermittent | Add logging, run multiple times |
| "GDB not found" | Debugger not installed | Install: `apt install gdb` |
| "No debug symbols" | Missing -g flag | Recompile with -g |
| "Heisenbug" | Bug disappears in debugger | Use logging instead |

---

## Integration Points

| Component | Interface |
|-----------|-----------|
| `cpp-debugger-agent` | Primary debugging agent |
| `memory-specialist` | Memory-related issues |
| `performance-optimizer` | Performance debugging |
| `build-engineer` | Debug build configuration |

---

*C++ Plugin v3.0.0 - Production-Grade Development Command*
