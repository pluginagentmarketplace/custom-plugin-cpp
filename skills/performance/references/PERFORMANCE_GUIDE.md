# Performance Optimization Guide

## Cache Optimization

### Data Layout
```cpp
// Bad: Array of Structures (cache unfriendly)
struct Particle { float x, y, z, vx, vy, vz; };
std::vector<Particle> particles;

// Good: Structure of Arrays (cache friendly)
struct Particles {
    std::vector<float> x, y, z;
    std::vector<float> vx, vy, vz;
};
```

### Memory Alignment
```cpp
struct alignas(64) CacheAligned {
    std::array<float, 16> data;  // Fits in cache line
};
```

## SIMD Vectorization

```cpp
#include <immintrin.h>

void add_vectors_avx(float* a, float* b, float* result, int n) {
    for (int i = 0; i < n; i += 8) {
        __m256 va = _mm256_loadu_ps(&a[i]);
        __m256 vb = _mm256_loadu_ps(&b[i]);
        __m256 vr = _mm256_add_ps(va, vb);
        _mm256_storeu_ps(&result[i], vr);
    }
}
```

## Multithreading

```cpp
#include <thread>
#include <future>

// std::async for task parallelism
auto future = std::async(std::launch::async, expensive_computation);
auto result = future.get();

// Thread pool pattern
class ThreadPool {
    std::vector<std::thread> workers;
    std::queue<std::function<void()>> tasks;
    // ...
};
```

## Benchmarking

```cpp
#include <benchmark/benchmark.h>

static void BM_VectorPush(benchmark::State& state) {
    for (auto _ : state) {
        std::vector<int> v;
        for (int i = 0; i < 1000; ++i)
            v.push_back(i);
    }
}
BENCHMARK(BM_VectorPush);

static void BM_VectorReserve(benchmark::State& state) {
    for (auto _ : state) {
        std::vector<int> v;
        v.reserve(1000);
        for (int i = 0; i < 1000; ++i)
            v.push_back(i);
    }
}
BENCHMARK(BM_VectorReserve);

BENCHMARK_MAIN();
```

## Quick Wins
- Use `reserve()` for vectors
- Pass by `const&` or `std::string_view`
- Use `emplace` instead of `push`
- Enable compiler optimizations (`-O3`)
- Use `noexcept` where applicable

---

*C++ Plugin - Performance Skill*
