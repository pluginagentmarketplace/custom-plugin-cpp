---
# ═══════════════════════════════════════════════════════════════════════════════
# COMMAND: cpp-optimize
# Version: 3.0.0 | SASMP v1.3.0 Compliant | Production-Grade
# ═══════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# IDENTITY
# ─────────────────────────────────────────────────────────────────────────────
name: cpp-optimize
version: "3.0.0"
description: Optimize C++ code for maximum performance

# ─────────────────────────────────────────────────────────────────────────────
# CLASSIFICATION
# ─────────────────────────────────────────────────────────────────────────────
category: development
priority: 3

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
routes_to: performance-optimizer
fallback_agent: modern-cpp-expert

# ─────────────────────────────────────────────────────────────────────────────
# INPUT VALIDATION
# ─────────────────────────────────────────────────────────────────────────────
input_schema:
  type: object
  properties:
    focus:
      type: string
      required: false
      enum: [profile, cache, simd, parallel, algorithm, memory, all]
      default: all
      description: "Optimization focus area"
    target:
      type: string
      required: false
      enum: [throughput, latency, memory, binary_size]
      default: throughput
      description: "Primary optimization target"
    file:
      type: string
      required: false
      description: "Specific file to optimize"

# ─────────────────────────────────────────────────────────────────────────────
# EXIT CODES
# ─────────────────────────────────────────────────────────────────────────────
exit_codes:
  0: "Success - optimization applied"
  1: "No bottleneck found"
  2: "Optimization would break functionality"
  3: "Profiling tools unavailable"
  4: "Benchmark failed"

# ─────────────────────────────────────────────────────────────────────────────
# ERROR HANDLING
# ─────────────────────────────────────────────────────────────────────────────
error_handling:
  on_no_bottleneck: "suggest_algorithmic_review"
  on_tool_missing: "provide_installation_guide"
  on_regression: "rollback_and_analyze"
  on_minimal_gain: "explain_tradeoffs"
---

# /cpp-optimize

**Development Command** | Performance Optimization

Expert-guided performance optimization with profiling, analysis, and implementation.

---

## Usage

```
/cpp-optimize [focus] [--target=throughput] [--file=path]
```

## Arguments

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `focus` | string | No | profile, cache, simd, parallel, algorithm, memory |
| `--target` | string | No | throughput, latency, memory, binary_size |
| `--file` | string | No | Specific file to optimize |

---

## Focus Areas

| Focus | Description | Tools Used |
|-------|-------------|------------|
| **profile** | Find bottlenecks | perf, VTune, callgrind |
| **cache** | Improve cache utilization | cachegrind, perf stat |
| **simd** | Vectorize computations | compiler reports, intrinsics |
| **parallel** | Multi-threading | OpenMP, std::execution |
| **algorithm** | Better data structures | Complexity analysis |
| **memory** | Reduce allocations | Allocator profiling |

---

## Examples

```bash
# General optimization review
/cpp-optimize

# Find bottlenecks first
/cpp-optimize profile

# Cache optimization
/cpp-optimize cache

# Add parallelism
/cpp-optimize parallel

# Specific file
/cpp-optimize --file=src/engine.cpp

# Optimize for latency
/cpp-optimize --target=latency
```

---

## Optimization Workflow

```
┌─────────────┐    ┌──────────────┐    ┌───────────────┐
│   PROFILE   │───▶│   IDENTIFY   │───▶│   OPTIMIZE    │
│  (measure)  │    │  (hotspots)  │    │  (implement)  │
└─────────────┘    └──────────────┘    └───────────────┘
       ▲                                      │
       │                                      ▼
       │              ┌──────────────┐    ┌───────────────┐
       └──────────────│   VERIFY     │◀───│   BENCHMARK   │
                      │  (improved?) │    │   (measure)   │
                      └──────────────┘    └───────────────┘
```

---

## Profiling Commands

### Linux perf
```bash
# CPU profiling
perf record -g ./program
perf report

# Hardware counters
perf stat -e cache-misses,cache-references,cycles ./program

# Flamegraph
perf script | stackcollapse-perf.pl | flamegraph.pl > flame.svg
```

### Valgrind Callgrind
```bash
valgrind --tool=callgrind ./program
kcachegrind callgrind.out.*
```

### Google Benchmark
```cpp
#include <benchmark/benchmark.h>

static void BM_Function(benchmark::State& state) {
    for (auto _ : state) {
        // Code to benchmark
        benchmark::DoNotOptimize(result);
    }
}
BENCHMARK(BM_Function);
```

---

## Quick Wins Checklist

### Immediate Optimizations
- [ ] Use `reserve()` for vectors with known size
- [ ] Prefer `emplace_back()` over `push_back()`
- [ ] Move instead of copy when possible
- [ ] Use `string_view` for read-only strings
- [ ] Avoid allocations in hot loops
- [ ] Use `[[likely]]`/`[[unlikely]]` for branch hints

### Data Layout
- [ ] Consider SoA vs AoS for large datasets
- [ ] Align hot data to cache lines (64 bytes)
- [ ] Separate hot and cold data
- [ ] Reduce struct padding

### Algorithmic
- [ ] Choose right container for access pattern
- [ ] Use binary search on sorted data
- [ ] Consider lookup tables for expensive functions
- [ ] Eliminate redundant computation

---

## Optimization Techniques

### Cache Optimization
```cpp
// SoA for better cache utilization
struct ParticlesSoA {
    std::vector<float> x, y, z;  // Contiguous access

    void update(float dt) {
        for (size_t i = 0; i < x.size(); ++i) {
            x[i] += vx[i] * dt;  // Cache-friendly
        }
    }
};
```

### SIMD Vectorization
```cpp
// Help compiler auto-vectorize
void add(float* __restrict a, float* __restrict b,
         float* __restrict c, size_t n) {
    #pragma omp simd
    for (size_t i = 0; i < n; ++i) {
        c[i] = a[i] + b[i];
    }
}
```

### Parallelization
```cpp
#include <execution>

// Parallel sort
std::sort(std::execution::par_unseq, v.begin(), v.end());

// Parallel reduce
auto sum = std::reduce(std::execution::par, v.begin(), v.end());
```

---

## Compiler Flags

| Purpose | GCC/Clang | MSVC |
|---------|-----------|------|
| Max optimization | `-O3` | `/O2` |
| Native CPU | `-march=native` | `/arch:AVX2` |
| LTO | `-flto` | `/GL /LTCG` |
| No exceptions | `-fno-exceptions` | `/EHs-c-` |
| Fast math | `-ffast-math` | `/fp:fast` |

### Profile-Guided Optimization
```bash
# Step 1: Instrument
g++ -fprofile-generate -O3 program.cpp -o program

# Step 2: Run with typical workload
./program typical_input.txt

# Step 3: Optimize with profile
g++ -fprofile-use -O3 program.cpp -o program_optimized
```

---

## Troubleshooting

| Symptom | Likely Cause | Investigation |
|---------|--------------|---------------|
| High CPU, low throughput | Cache misses | `perf stat -e cache-misses` |
| Variable latency | Lock contention | Check mutex wait times |
| Memory growing | Allocator pressure | Profile allocations |
| Single core maxed | No parallelism | Add `std::execution` |

---

## Error Messages

| Error | Cause | Solution |
|-------|-------|----------|
| "No bottleneck found" | Code already optimal | Focus on algorithms |
| "perf not found" | Missing profiler | `apt install linux-tools-generic` |
| "Regression detected" | Optimization broke something | Rollback, investigate |
| "Minimal improvement" | Amdahl's Law | Parallelize different section |

---

## Integration Points

| Component | Interface |
|-----------|-----------|
| `performance-optimizer` | Primary optimization agent |
| `build-engineer` | Compiler flags |
| `modern-cpp-expert` | Move semantics |
| `stl-master` | Container selection |

---

*C++ Plugin v3.0.0 - Production-Grade Development Command*
