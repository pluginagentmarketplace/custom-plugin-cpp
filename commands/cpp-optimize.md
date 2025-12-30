---
name: cpp-optimize
description: Optimize C++ code for maximum performance
allowed-tools: Read, Write, Edit, Bash, Grep
category: development
---

# /cpp-optimize

**🔧 Development Mode Command**

Access the performance optimization expert for profiling and speeding up C++ code.

## Optimization Areas

| Area | Focus |
|------|-------|
| **Profiling** | Find bottlenecks with perf, VTune |
| **Algorithms** | Choose better data structures |
| **Cache** | Improve memory access patterns |
| **SIMD** | Vectorize computations |
| **Threading** | Parallelize work |
| **Compiler** | Leverage optimization flags |

## Usage

```
/cpp-optimize [focus-area]
```

## Examples

```bash
/cpp-optimize                    # General optimization review
/cpp-optimize profile            # Find performance bottlenecks
/cpp-optimize cache              # Improve cache utilization
/cpp-optimize parallel           # Add parallelism
/cpp-optimize "this function"    # Optimize specific code
```

## Optimization Process

1. **Measure** - Profile to find actual bottlenecks
2. **Analyze** - Understand the performance issue
3. **Optimize** - Apply targeted improvements
4. **Verify** - Benchmark the results

## Quick Profiling

```bash
# Linux perf
perf record ./program
perf report

# Callgrind (detailed)
valgrind --tool=callgrind ./program
kcachegrind callgrind.out.*

# Quick timing
time ./program
```

## Optimization Flags

```bash
# Release build
g++ -O3 -march=native -DNDEBUG program.cpp

# Profile-guided optimization
g++ -fprofile-generate program.cpp
./program  # Run with typical input
g++ -fprofile-use -O3 program.cpp
```

## Common Optimizations

- Use `reserve()` for vectors
- Prefer `emplace_back()` over `push_back()`
- Move instead of copy
- Use SoA instead of AoS for cache
- Parallelize with OpenMP or std::execution

---

*C++ Plugin v2.0.0 - Development Command*
