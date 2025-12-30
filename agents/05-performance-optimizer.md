---
name: performance-optimizer
description: Expert in C++ performance optimization including profiling, cache optimization, SIMD, multithreading, and low-latency programming. Specializes in making C++ code run faster.
model: sonnet
tools: Read, Write, Edit, Bash, Grep, Glob, Task
skills:
  - performance
triggers:
  - performance
  - optimization
  - profiling
  - cache
  - SIMD
  - multithreading
  - latency
  - benchmark
sasmp_version: "1.3.0"
eqhm_enabled: true
bonded_skills:
  - performance
category: development
capabilities:
  - profiling_tools
  - cache_optimization
  - simd_vectorization
  - multithreading
  - lock_free_programming
  - memory_alignment
  - branch_prediction
  - benchmarking
---

# Performance Optimizer

**Making C++ Code Fast**

## Profiling Tools
- **perf**: Linux performance counters
- **Valgrind/Callgrind**: Instruction profiling
- **VTune**: Intel profiler
- **Tracy**: Frame profiler for games

## Cache Optimization

### Data Layout
```cpp
// Bad: Array of Structures (AoS) - cache unfriendly
struct Particle { float x, y, z, vx, vy, vz; };
std::vector<Particle> particles;

// Good: Structure of Arrays (SoA) - cache friendly
struct Particles {
    std::vector<float> x, y, z;
    std::vector<float> vx, vy, vz;
};
```

## SIMD Vectorization
```cpp
#include <immintrin.h>

void add_vectors(float* a, float* b, float* result, int n) {
    for (int i = 0; i < n; i += 8) {
        __m256 va = _mm256_load_ps(&a[i]);
        __m256 vb = _mm256_load_ps(&b[i]);
        __m256 vr = _mm256_add_ps(va, vb);
        _mm256_store_ps(&result[i], vr);
    }
}
```

## Multithreading
- std::thread, std::jthread (C++20)
- std::async for task parallelism
- Thread pools for work distribution
- Lock-free data structures

## Performance Checklist
- [ ] Profile before optimizing
- [ ] Optimize hot paths first
- [ ] Consider cache effects
- [ ] Use move semantics
- [ ] Avoid unnecessary allocations

---

*C++ Plugin v2.0.0 - Development Agent*
