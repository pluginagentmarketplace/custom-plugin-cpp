---
# ═══════════════════════════════════════════════════════════════════════════════
# SKILL: Performance
# Version: 3.0.0 | SASMP v1.3.0 Compliant | Production-Grade
# ═══════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# IDENTITY
# ─────────────────────────────────────────────────────────────────────────────
name: performance
version: "3.0.0"
description: >
  Production-grade skill for C++ performance optimization. Covers profiling,
  benchmarking, cache optimization, SIMD vectorization, multithreading, and
  lock-free programming techniques.

# ─────────────────────────────────────────────────────────────────────────────
# COMPLIANCE
# ─────────────────────────────────────────────────────────────────────────────
sasmp_version: "1.3.0"
skill_version: "3.0.0"

# ─────────────────────────────────────────────────────────────────────────────
# BONDING
# ─────────────────────────────────────────────────────────────────────────────
bonded_agent: 05-performance-optimizer
bond_type: PRIMARY_BOND
category: development

# ─────────────────────────────────────────────────────────────────────────────
# PARAMETERS
# ─────────────────────────────────────────────────────────────────────────────
parameters:
  optimization_target:
    type: string
    required: false
    enum: [throughput, latency, memory, cpu, all]
    default: all
    description: "Primary optimization target"
  profiling_tool:
    type: string
    required: false
    enum: [perf, vtune, valgrind, tracy, instruments]
    description: "Profiling tool to use"
  optimization_level:
    type: string
    required: false
    enum: [quick_wins, moderate, aggressive]
    default: moderate
    description: "Depth of optimization effort"
  maintain_readability:
    type: boolean
    required: false
    default: true
    description: "Whether to prioritize code readability"

# ─────────────────────────────────────────────────────────────────────────────
# ERROR HANDLING
# ─────────────────────────────────────────────────────────────────────────────
error_handling:
  retry_logic:
    max_attempts: 3
    backoff: exponential
    initial_delay_ms: 1000
    max_delay_ms: 16000
    jitter: true
  fallback:
    on_benchmark_unstable: "increase_iterations"
    on_profiling_fail: "use_alternative_tool"
    on_no_improvement: "try_different_approach"
    on_regression: "rollback_and_analyze"
  validation:
    verify_no_regression: true
    statistical_significance: true
    test_multiple_inputs: true
---

# Performance Skill

**Production-Grade Development Skill** | C++ Performance Engineering

Optimize C++ code for maximum performance through profiling, analysis, and targeted optimization.

---

## Golden Rules

```
┌─────────────────────────────────────────────────────────────────┐
│  1. MEASURE first - never optimize without profiling data       │
│  2. OPTIMIZE hotspots - focus on the 20% that takes 80% time   │
│  3. VERIFY improvements - benchmark before and after            │
│  4. MAINTAIN readability - premature optimization is evil       │
└─────────────────────────────────────────────────────────────────┘
```

---

## Profiling Tools

### Linux perf

```bash
# Record CPU profile
perf record -g ./program
perf report

# Flamegraph generation
perf script | stackcollapse-perf.pl | flamegraph.pl > flame.svg

# Hardware counters
perf stat -e cache-misses,cache-references,instructions,cycles ./program

# Specific function profiling
perf record -g -e cycles:u --call-graph dwarf ./program
```

### Valgrind Callgrind

```bash
# Instruction-level profiling
valgrind --tool=callgrind ./program
kcachegrind callgrind.out.*

# Cache simulation
valgrind --tool=cachegrind ./program
cg_annotate cachegrind.out.*
```

### Google Benchmark

```cpp
#include <benchmark/benchmark.h>

static void BM_VectorPushBack(benchmark::State& state) {
    for (auto _ : state) {
        std::vector<int> v;
        v.reserve(state.range(0));  // Fair comparison
        for (int i = 0; i < state.range(0); ++i) {
            v.push_back(i);
        }
        benchmark::DoNotOptimize(v.data());
        benchmark::ClobberMemory();
    }
    state.SetComplexityN(state.range(0));
}
BENCHMARK(BM_VectorPushBack)
    ->Range(8, 8 << 10)
    ->Complexity(benchmark::oN);

BENCHMARK_MAIN();
```

---

## Cache Optimization

### Data Layout: AoS vs SoA

```cpp
// ❌ Array of Structures (AoS) - cache unfriendly for iteration
struct ParticleAoS {
    float x, y, z;       // Position
    float vx, vy, vz;    // Velocity
    float mass;
    int id;
};
std::vector<ParticleAoS> particles;  // 32 bytes per particle

// ✅ Structure of Arrays (SoA) - cache friendly
struct ParticlesSoA {
    std::vector<float> x, y, z;      // Contiguous positions
    std::vector<float> vx, vy, vz;   // Contiguous velocities
    std::vector<float> mass;
    std::vector<int> id;

    void update_positions(float dt) {
        const size_t n = x.size();
        for (size_t i = 0; i < n; ++i) {
            x[i] += vx[i] * dt;  // Full cache line utilization
            y[i] += vy[i] * dt;
            z[i] += vz[i] * dt;
        }
    }
};
```

### Cache Line Alignment

```cpp
// Avoid false sharing with cache line alignment
struct alignas(64) CacheAlignedCounter {
    std::atomic<long> count{0};
    char padding[56];  // Ensure 64-byte alignment
};

// Per-thread counters without false sharing
std::array<CacheAlignedCounter, 8> thread_counters;

// Hot/cold data separation
struct HotData {
    int frequently_accessed;
    int also_frequent;
};

struct ColdData {
    std::string rarely_used;
    std::vector<int> debug_info;
};

struct OptimizedNode {
    HotData hot;
    ColdData* cold;  // Pointer to cold data (loaded on demand)
};
```

---

## SIMD Vectorization

### Auto-vectorization Hints

```cpp
// Help compiler vectorize with restrict and pragmas
void add_arrays(float* __restrict a, float* __restrict b,
                float* __restrict result, size_t n) {
    #pragma omp simd
    for (size_t i = 0; i < n; ++i) {
        result[i] = a[i] + b[i];
    }
}

// Alignment for better vectorization
void process_aligned(float* data, size_t n) {
    float* __restrict aligned_data =
        std::assume_aligned<32>(data);  // C++20

    for (size_t i = 0; i < n; ++i) {
        aligned_data[i] *= 2.0f;
    }
}
```

### Explicit SIMD (AVX)

```cpp
#include <immintrin.h>

void add_vectors_avx(const float* a, const float* b,
                     float* result, size_t n) {
    size_t i = 0;

    // Process 8 floats at a time with AVX
    for (; i + 8 <= n; i += 8) {
        __m256 va = _mm256_loadu_ps(&a[i]);
        __m256 vb = _mm256_loadu_ps(&b[i]);
        __m256 vr = _mm256_add_ps(va, vb);
        _mm256_storeu_ps(&result[i], vr);
    }

    // Handle remainder
    for (; i < n; ++i) {
        result[i] = a[i] + b[i];
    }
}

// Horizontal sum with AVX
float horizontal_sum_avx(__m256 v) {
    __m128 lo = _mm256_castps256_ps128(v);
    __m128 hi = _mm256_extractf128_ps(v, 1);
    lo = _mm_add_ps(lo, hi);
    lo = _mm_hadd_ps(lo, lo);
    lo = _mm_hadd_ps(lo, lo);
    return _mm_cvtss_f32(lo);
}
```

---

## Multithreading

### Parallel Algorithms (C++17)

```cpp
#include <execution>
#include <algorithm>
#include <numeric>

std::vector<int> data(1'000'000);

// Parallel sort
std::sort(std::execution::par_unseq, data.begin(), data.end());

// Parallel transform
std::transform(std::execution::par, data.begin(), data.end(),
               data.begin(), [](int x) { return x * 2; });

// Parallel reduce
long sum = std::reduce(std::execution::par,
                       data.begin(), data.end(), 0L);

// Parallel for_each
std::for_each(std::execution::par_unseq, data.begin(), data.end(),
              [](int& x) { x = process(x); });
```

### Thread Pool

```cpp
#include <thread>
#include <queue>
#include <functional>
#include <future>
#include <condition_variable>

class ThreadPool {
    std::vector<std::thread> workers_;
    std::queue<std::function<void()>> tasks_;
    std::mutex mutex_;
    std::condition_variable cv_;
    std::atomic<bool> stop_{false};

public:
    explicit ThreadPool(size_t threads = std::thread::hardware_concurrency()) {
        for (size_t i = 0; i < threads; ++i) {
            workers_.emplace_back([this] {
                while (true) {
                    std::function<void()> task;
                    {
                        std::unique_lock lock(mutex_);
                        cv_.wait(lock, [this] {
                            return stop_ || !tasks_.empty();
                        });
                        if (stop_ && tasks_.empty()) return;
                        task = std::move(tasks_.front());
                        tasks_.pop();
                    }
                    task();
                }
            });
        }
    }

    template<typename F, typename... Args>
    auto enqueue(F&& f, Args&&... args)
        -> std::future<std::invoke_result_t<F, Args...>> {
        using return_type = std::invoke_result_t<F, Args...>;

        auto task = std::make_shared<std::packaged_task<return_type()>>(
            std::bind(std::forward<F>(f), std::forward<Args>(args)...)
        );

        std::future<return_type> res = task->get_future();
        {
            std::lock_guard lock(mutex_);
            tasks_.emplace([task]() { (*task)(); });
        }
        cv_.notify_one();
        return res;
    }

    ~ThreadPool() {
        stop_ = true;
        cv_.notify_all();
        for (auto& worker : workers_) {
            worker.join();
        }
    }
};
```

---

## Quick Wins Checklist

### Immediate Optimizations
- [ ] Use `reserve()` for vectors with known size
- [ ] Prefer `emplace_back()` over `push_back()`
- [ ] Move instead of copy when possible
- [ ] Use `string_view` for read-only strings
- [ ] Avoid unnecessary allocations in loops
- [ ] Use `[[likely]]` / `[[unlikely]]` for branch hints

### Data Layout
- [ ] Profile cache misses first
- [ ] Consider SoA vs AoS for large datasets
- [ ] Align hot data to cache lines
- [ ] Separate hot and cold data

### Algorithmic
- [ ] Choose right container for access pattern
- [ ] Use binary search on sorted data
- [ ] Avoid redundant computation
- [ ] Consider lookup tables for expensive functions

---

## Performance Workflow

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

## Troubleshooting Decision Tree

```
Performance issue?
├── High CPU, low throughput
│   ├── Check cache misses → perf stat -e cache-misses
│   ├── Check branch mispredictions → perf stat -e branch-misses
│   └── Profile hotspots → perf record + flamegraph
├── High latency spikes
│   ├── Check for locks → Look for mutex contention
│   ├── Check allocations → Use custom allocator
│   └── Check I/O blocking → Use async I/O
├── Memory growing
│   ├── Memory leak → Valgrind / ASan
│   ├── Fragmentation → Custom allocator
│   └── Retained references → Check lifetimes
└── Inconsistent performance
    ├── CPU throttling → Check power management
    ├── NUMA effects → Pin threads to cores
    └── Context switches → Reduce thread count
```

---

## Unit Test Template

```cpp
#include <gtest/gtest.h>
#include <benchmark/benchmark.h>
#include <chrono>

class PerformanceTest : public ::testing::Test {
protected:
    static constexpr size_t ITERATIONS = 1000;

    template<typename Func>
    auto measure(Func&& f) {
        auto start = std::chrono::high_resolution_clock::now();
        for (size_t i = 0; i < ITERATIONS; ++i) {
            f();
        }
        auto end = std::chrono::high_resolution_clock::now();
        return std::chrono::duration_cast<std::chrono::microseconds>(
            end - start).count() / ITERATIONS;
    }
};

TEST_F(PerformanceTest, VectorReserveIsFaster) {
    auto without_reserve = measure([]{
        std::vector<int> v;
        for (int i = 0; i < 1000; ++i) v.push_back(i);
    });

    auto with_reserve = measure([]{
        std::vector<int> v;
        v.reserve(1000);
        for (int i = 0; i < 1000; ++i) v.push_back(i);
    });

    EXPECT_LT(with_reserve, without_reserve);
}

TEST_F(PerformanceTest, SoAFasterThanAoS) {
    // Test cache efficiency
    auto aos_time = measure([this]{ process_aos(); });
    auto soa_time = measure([this]{ process_soa(); });

    EXPECT_LT(soa_time, aos_time * 0.8);  // At least 20% faster
}
```

---

## Integration Points

| Component | Interface |
|-----------|-----------|
| `build-engineer` | Optimization flags |
| `modern-cpp-expert` | Move semantics |
| `memory-specialist` | Allocation patterns |
| `cpp-debugger-agent` | Performance debugging |

---

*C++ Plugin v3.0.0 - Production-Grade Development Skill*
