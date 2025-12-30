---
# ═══════════════════════════════════════════════════════════════════════════════
# SKILL: Debugging
# Version: 3.0.0 | SASMP v1.3.0 Compliant | Production-Grade
# ═══════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# IDENTITY
# ─────────────────────────────────────────────────────────────────────────────
name: debugging
version: "3.0.0"
description: >
  Production-grade skill for C++ debugging. Covers GDB, LLDB, sanitizers,
  memory debugging, crash analysis, and systematic bug investigation techniques.

# ─────────────────────────────────────────────────────────────────────────────
# COMPLIANCE
# ─────────────────────────────────────────────────────────────────────────────
sasmp_version: "1.3.0"
skill_version: "3.0.0"

# ─────────────────────────────────────────────────────────────────────────────
# BONDING
# ─────────────────────────────────────────────────────────────────────────────
bonded_agent: cpp-debugger-agent
bond_type: PRIMARY_BOND
category: development

# ─────────────────────────────────────────────────────────────────────────────
# PARAMETERS
# ─────────────────────────────────────────────────────────────────────────────
parameters:
  debugger:
    type: string
    required: false
    enum: [gdb, lldb, visual_studio, windbg]
    default: gdb
    description: "Debugger to use"
  issue_type:
    type: string
    required: false
    enum: [crash, memory, logic, performance, concurrency]
    description: "Type of issue being debugged"
  sanitizer:
    type: string
    required: false
    enum: [asan, ubsan, tsan, msan]
    description: "Sanitizer to enable"
  verbosity:
    type: string
    required: false
    enum: [minimal, standard, verbose]
    default: standard
    description: "Level of debug output"

# ─────────────────────────────────────────────────────────────────────────────
# ERROR HANDLING
# ─────────────────────────────────────────────────────────────────────────────
error_handling:
  retry_logic:
    max_attempts: 3
    backoff: exponential
    initial_delay_ms: 500
    max_delay_ms: 8000
    jitter: true
  fallback:
    on_crash_not_reproducible: "enable_core_dumps"
    on_debugger_fail: "use_logging"
    on_sanitizer_overhead: "use_sampling"
    on_heisenbug: "add_instrumentation"
  validation:
    verify_debug_symbols: true
    check_optimization_level: true
    confirm_reproducibility: true
---

# Debugging Skill

**Production-Grade Development Skill** | C++ Debugging & Error Analysis

Master C++ debugging tools and systematic investigation techniques.

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

## GDB (GNU Debugger)

### Essential Commands

```bash
# Compile with debug symbols
g++ -g -O0 program.cpp -o program

# Start GDB
gdb ./program

# Core dump analysis
gdb ./program core.dump
```

```gdb
# Execution Control
run [args]              # Start program
continue (c)            # Continue execution
next (n)                # Step over
step (s)                # Step into
finish                  # Run until current function returns
until <line>            # Run until line

# Breakpoints
break main              # Break at function
break file.cpp:42       # Break at line
break *0x400520         # Break at address
break func if x > 5     # Conditional breakpoint
delete <num>            # Remove breakpoint
disable/enable <num>    # Toggle breakpoint

# Inspection
print variable          # Print value
print/x variable        # Print in hex
display variable        # Print at each stop
info locals             # Show local variables
info args               # Show function arguments
ptype variable          # Show type

# Stack Navigation
backtrace (bt)          # Show call stack
frame <n>               # Select frame
up/down                 # Move in stack

# Memory
x/10xw 0x400520         # Examine 10 words in hex
watch variable          # Break when variable changes
rwatch variable         # Break when variable is read

# Advanced
catch throw             # Break on exception
set variable x = 5      # Modify variable
call func(args)         # Call function
```

### GDB Scripts

```gdb
# .gdbinit - Auto-loaded configuration
set history save on
set print pretty on
set print array on
set pagination off

# Custom command
define pv
    print *$arg0@$arg1
end
# Usage: pv array 10
```

---

## LLDB (macOS/Clang)

```bash
# Start LLDB
lldb ./program

# Attach to process
lldb -p <pid>
```

```lldb
# Breakpoints
breakpoint set --name main
breakpoint set --file main.cpp --line 42
breakpoint set --method MyClass::method

# Execution
run
continue
next
step
finish

# Inspection
frame variable              # Show all locals
frame variable varname      # Show specific variable
expression varname          # Evaluate expression
expression -O -- object     # Print object description

# Stack
thread backtrace
frame select <n>
up/down

# Watchpoints
watchpoint set variable varname
watchpoint set expression -- &array[5]
```

---

## Sanitizers

### AddressSanitizer (ASan)

```bash
# Compile with ASan
g++ -fsanitize=address -g -O1 program.cpp -o program

# Run (ASan is active)
./program

# Detects:
# - Heap buffer overflow
# - Stack buffer overflow
# - Global buffer overflow
# - Use after free
# - Use after return
# - Double free
# - Memory leaks (with ASAN_OPTIONS=detect_leaks=1)
```

### UndefinedBehaviorSanitizer (UBSan)

```bash
# Compile with UBSan
g++ -fsanitize=undefined -g program.cpp -o program

# Detects:
# - Signed integer overflow
# - Division by zero
# - Null pointer dereference
# - Invalid shift
# - Out-of-bounds array access
# - Misaligned pointer access
```

### ThreadSanitizer (TSan)

```bash
# Compile with TSan
g++ -fsanitize=thread -g program.cpp -o program

# Detects:
# - Data races
# - Deadlocks (with deadlock_detector=1)
# - Lock order violations
```

### Combined Usage

```cmake
# CMakeLists.txt
option(ENABLE_SANITIZERS "Enable sanitizers" OFF)

if(ENABLE_SANITIZERS)
    add_compile_options(
        -fsanitize=address,undefined
        -fno-omit-frame-pointer
        -g
    )
    add_link_options(
        -fsanitize=address,undefined
    )
endif()
```

---

## Valgrind

### Memory Leak Detection

```bash
# Check for memory leaks
valgrind --leak-check=full --show-leak-kinds=all ./program

# With line numbers
valgrind --leak-check=full --track-origins=yes ./program

# Generate suppressions for known issues
valgrind --gen-suppressions=all ./program
```

### Memcheck Options

```bash
valgrind --tool=memcheck \
    --leak-check=full \
    --show-leak-kinds=all \
    --track-origins=yes \
    --verbose \
    --log-file=valgrind.log \
    ./program
```

### Cachegrind (Cache Profiling)

```bash
valgrind --tool=cachegrind ./program
cg_annotate cachegrind.out.*

# Output shows:
# - I1 cache read misses
# - D1 cache read/write misses
# - LL (last level) cache misses
```

---

## Common Issue Patterns

### Issue Diagnostic Table

| Issue | Symptoms | Primary Tool | Secondary Tool |
|-------|----------|--------------|----------------|
| Segfault | SIGSEGV, crash | GDB + bt | ASan |
| Memory leak | Growing memory | Valgrind | ASan (leak check) |
| Buffer overflow | Corruption, crash | ASan | Valgrind |
| Use after free | Random crash | ASan | Valgrind |
| Data race | Random behavior | TSan | Helgrind |
| Deadlock | Hang | GDB + threads | TSan |
| Integer overflow | Wrong results | UBSan | - |
| Null deref | Crash at low address | ASan | GDB |
| Stack overflow | Deep recursion crash | GDB | ulimit |

### Quick Diagnosis Commands

```bash
# Check if crash is reproducible
for i in {1..100}; do ./program || echo "Crashed on run $i"; done

# Get core dump
ulimit -c unlimited
./program  # Will generate core file

# Quick stack trace from core
gdb -batch -ex "bt" ./program core

# Check for memory issues quickly
MALLOC_CHECK_=3 ./program
```

---

## Troubleshooting Decision Tree

```
Program crashed?
├── Segmentation fault (SIGSEGV)
│   ├── Get backtrace: gdb -batch -ex "bt" ./program core
│   ├── Check for NULL deref: look at crash address
│   ├── Check for buffer overflow: run with ASan
│   └── Check for use-after-free: run with ASan
├── Abort (SIGABRT)
│   ├── Check assert failures: look at stderr
│   ├── Check std::terminate: uncaught exception
│   └── Check double free: run with ASan
├── Hang (no progress)
│   ├── Attach debugger: gdb -p <pid>
│   ├── Check for deadlock: info threads, thread apply all bt
│   └── Check for infinite loop: break, bt
└── Wrong output
    ├── Check undefined behavior: run with UBSan
    ├── Add logging at key points
    └── Use debugger to trace execution
```

---

## Debug Build Configuration

```cmake
# CMakeLists.txt
set(CMAKE_BUILD_TYPE Debug)

# Ensure debug symbols
set(CMAKE_CXX_FLAGS_DEBUG "-g -O0")

# Sanitizers for debug builds
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    add_compile_options(-fsanitize=address,undefined)
    add_link_options(-fsanitize=address,undefined)
endif()

# Export compile commands for IDE integration
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
```

---

## Debug Logging Pattern

```cpp
#include <iostream>
#include <source_location>

// Modern debug logging (C++20)
template<typename... Args>
void debug_log(Args&&... args,
               std::source_location loc = std::source_location::current()) {
#ifndef NDEBUG
    std::cerr << "[DEBUG] " << loc.file_name() << ":"
              << loc.line() << " (" << loc.function_name() << "): ";
    (std::cerr << ... << std::forward<Args>(args)) << '\n';
#endif
}

// Usage
void process(int x) {
    debug_log("Processing value: ", x);
    // ...
}
```

---

## Unit Test Template

```cpp
#include <gtest/gtest.h>
#include <signal.h>

class DebuggingTest : public ::testing::Test {
protected:
    void SetUp() override {
        // Enable core dumps for this test
        struct rlimit core_limit;
        core_limit.rlim_cur = RLIM_INFINITY;
        core_limit.rlim_max = RLIM_INFINITY;
        setrlimit(RLIMIT_CORE, &core_limit);
    }
};

// Test that sanitizers catch issues
TEST_F(DebuggingTest, DetectsBufferOverflow) {
    // This should be caught by ASan if enabled
    // Only run with sanitizers in CI
    #ifdef __SANITIZE_ADDRESS__
    GTEST_SKIP() << "Would trigger ASan, skipping";
    #endif
}

TEST_F(DebuggingTest, DebugSymbolsPresent) {
    // Verify debug build
    #ifdef NDEBUG
    FAIL() << "Tests should run in debug mode";
    #endif
}

// Death test for expected crashes
TEST_F(DebuggingTest, CrashOnNullDeref) {
    EXPECT_DEATH({
        int* p = nullptr;
        *p = 42;
    }, "");
}
```

---

## Integration Points

| Component | Interface |
|-----------|-----------|
| `build-engineer` | Debug build flags |
| `memory-specialist` | Memory issue patterns |
| `performance-optimizer` | Performance debugging |
| `modern-cpp-expert` | Smart pointer debugging |

---

*C++ Plugin v3.0.0 - Production-Grade Development Skill*
