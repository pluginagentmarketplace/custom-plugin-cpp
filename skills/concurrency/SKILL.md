---
# ═══════════════════════════════════════════════════════════════════════════════
# SKILL: Concurrency
# Version: 3.0.0 | SASMP v1.3.0 Compliant | Production-Grade
# ═══════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# IDENTITY
# ─────────────────────────────────────────────────────────────────────────────
name: concurrency
version: "3.0.0"
description: >
  Production-grade skill for C++ concurrency and parallel programming. Covers
  threads, synchronization primitives, atomics, async programming, parallel
  algorithms, and lock-free data structures.

# ─────────────────────────────────────────────────────────────────────────────
# COMPLIANCE
# ─────────────────────────────────────────────────────────────────────────────
sasmp_version: "1.3.0"
skill_version: "3.0.0"

# ─────────────────────────────────────────────────────────────────────────────
# BONDING
# ─────────────────────────────────────────────────────────────────────────────
bonded_agent: modern-cpp-expert
bond_type: PRIMARY_BOND
category: development

# ─────────────────────────────────────────────────────────────────────────────
# PARAMETERS
# ─────────────────────────────────────────────────────────────────────────────
parameters:
  concurrency_model:
    type: string
    required: false
    enum: [threads, async, coroutines, parallel_stl]
    description: "Concurrency model to use"
  synchronization:
    type: string
    required: false
    enum: [mutex, atomic, lock_free, message_passing]
    description: "Synchronization strategy"
  thread_count:
    type: string
    required: false
    enum: [single, hardware, custom]
    default: hardware
    description: "Thread pool sizing strategy"

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
    on_deadlock: "timeout_and_retry"
    on_race_condition: "add_synchronization"
    on_thread_exhaustion: "queue_tasks"
    on_priority_inversion: "use_priority_inheritance"
  validation:
    detect_races_with_tsan: true
    check_deadlock_potential: true
    verify_memory_ordering: true
---

# Concurrency Skill

**Production-Grade Development Skill** | C++ Concurrent Programming

Master C++ concurrency from C++11 threads to C++20 coroutines and parallel algorithms.

---

## Thread Basics

### Creating and Managing Threads

```cpp
#include <thread>
#include <iostream>

// Basic thread creation
void worker(int id) {
    std::cout << "Worker " << id << " running\n";
}

int main() {
    std::thread t1(worker, 1);
    std::thread t2(worker, 2);

    t1.join();  // Wait for completion
    t2.join();

    // Or detach (careful: must ensure thread doesn't outlive resources)
    // t1.detach();
}

// Thread with return value using reference
void compute(int input, int& result) {
    result = input * input;
}

// RAII thread wrapper (C++20 jthread)
#include <stop_token>

void cancellable_work(std::stop_token st) {
    while (!st.stop_requested()) {
        // Do work
    }
}

std::jthread worker(cancellable_work);
// Automatically joins on destruction and can be stopped
```

### Thread-Local Storage

```cpp
// Thread-local variable
thread_local int tls_counter = 0;

void increment() {
    ++tls_counter;  // Each thread has its own copy
}

// Thread-local singleton pattern
class Logger {
    thread_local static Logger* instance_;
public:
    static Logger& instance() {
        if (!instance_) {
            instance_ = new Logger();
        }
        return *instance_;
    }
};
```

---

## Synchronization Primitives

### Mutex and Locks

```cpp
#include <mutex>
#include <shared_mutex>

std::mutex mtx;
std::shared_mutex shared_mtx;

// Basic locking
void exclusive_access() {
    std::lock_guard<std::mutex> lock(mtx);  // RAII lock
    // Critical section
}

// Deferred locking for deadlock avoidance
void transfer(Account& from, Account& to, int amount) {
    std::unique_lock lock1(from.mtx, std::defer_lock);
    std::unique_lock lock2(to.mtx, std::defer_lock);
    std::lock(lock1, lock2);  // Lock both without deadlock

    from.balance -= amount;
    to.balance += amount;
}

// C++17 scoped_lock (locks multiple mutexes safely)
void safe_transfer(Account& from, Account& to, int amount) {
    std::scoped_lock lock(from.mtx, to.mtx);
    from.balance -= amount;
    to.balance += amount;
}

// Reader-writer lock
void read_data() {
    std::shared_lock lock(shared_mtx);  // Multiple readers OK
    // Read data
}

void write_data() {
    std::unique_lock lock(shared_mtx);  // Exclusive access
    // Write data
}
```

### Condition Variables

```cpp
#include <condition_variable>
#include <queue>

template<typename T>
class ThreadSafeQueue {
    std::queue<T> queue_;
    mutable std::mutex mtx_;
    std::condition_variable cv_;

public:
    void push(T value) {
        {
            std::lock_guard lock(mtx_);
            queue_.push(std::move(value));
        }
        cv_.notify_one();  // Notify outside lock
    }

    T pop() {
        std::unique_lock lock(mtx_);
        cv_.wait(lock, [this] { return !queue_.empty(); });
        T value = std::move(queue_.front());
        queue_.pop();
        return value;
    }

    // Non-blocking try_pop
    bool try_pop(T& value) {
        std::lock_guard lock(mtx_);
        if (queue_.empty()) return false;
        value = std::move(queue_.front());
        queue_.pop();
        return true;
    }
};
```

### C++20 Synchronization

```cpp
#include <semaphore>
#include <latch>
#include <barrier>

// Counting semaphore
std::counting_semaphore<10> sem(10);  // Max 10 permits

void limited_access() {
    sem.acquire();  // Wait for permit
    // Access limited resource
    sem.release();  // Return permit
}

// Latch - single-use barrier
std::latch start_latch(1);
std::latch done_latch(num_workers);

void worker() {
    start_latch.wait();    // Wait for start signal
    // Do work
    done_latch.count_down();  // Signal completion
}

// Barrier - reusable synchronization point
std::barrier sync_point(num_threads, []() noexcept {
    // Called by last thread to arrive (optional)
});

void iteration_worker() {
    for (int i = 0; i < iterations; ++i) {
        // Do phase work
        sync_point.arrive_and_wait();
    }
}
```

---

## Atomic Operations

### Atomic Types

```cpp
#include <atomic>

std::atomic<int> counter{0};
std::atomic<bool> flag{false};
std::atomic<std::shared_ptr<Data>> shared_data;

// Basic operations
counter.fetch_add(1);  // Atomic increment
counter.store(0);      // Atomic store
int val = counter.load();  // Atomic load

// Compare-and-swap
int expected = 0;
bool success = counter.compare_exchange_strong(expected, 1);
// If counter == expected, set to 1 and return true
// Otherwise, set expected to current value and return false

// Weak version (can fail spuriously, use in loops)
while (!counter.compare_exchange_weak(expected, expected + 1)) {
    // expected is updated to current value
}
```

### Memory Ordering

```cpp
// Memory order options (weakest to strongest):
// memory_order_relaxed - No synchronization, just atomicity
// memory_order_acquire - Prevents reordering after load
// memory_order_release - Prevents reordering before store
// memory_order_acq_rel - Both acquire and release
// memory_order_seq_cst - Total ordering (default)

std::atomic<int> data{0};
std::atomic<bool> ready{false};

// Producer
void produce() {
    data.store(42, std::memory_order_relaxed);
    ready.store(true, std::memory_order_release);
    // release ensures data store is visible before ready
}

// Consumer
void consume() {
    while (!ready.load(std::memory_order_acquire)) {
        // Spin wait
    }
    // acquire ensures we see data store after ready
    assert(data.load(std::memory_order_relaxed) == 42);
}
```

---

## Async Programming

### std::async and Futures

```cpp
#include <future>

// Launch async task
std::future<int> result = std::async(std::launch::async, []() {
    return expensive_computation();
});

// Do other work...

// Get result (blocks if not ready)
int value = result.get();

// Check if ready without blocking
if (result.wait_for(std::chrono::seconds(0)) == std::future_status::ready) {
    int value = result.get();
}

// Launch policy options
auto f1 = std::async(std::launch::async, func);    // New thread
auto f2 = std::async(std::launch::deferred, func); // Lazy evaluation
auto f3 = std::async(std::launch::async | std::launch::deferred, func); // Default
```

### Promise and Future

```cpp
void worker(std::promise<int> promise) {
    try {
        int result = compute();
        promise.set_value(result);
    } catch (...) {
        promise.set_exception(std::current_exception());
    }
}

std::promise<int> promise;
std::future<int> future = promise.get_future();
std::thread t(worker, std::move(promise));

try {
    int result = future.get();
} catch (const std::exception& e) {
    // Handle exception from worker
}
t.join();
```

### Packaged Task

```cpp
std::packaged_task<int(int, int)> task([](int a, int b) {
    return a + b;
});

std::future<int> result = task.get_future();

// Execute task
std::thread t(std::move(task), 2, 3);
t.join();

int sum = result.get();  // 5
```

---

## Parallel Algorithms (C++17)

```cpp
#include <execution>
#include <algorithm>
#include <numeric>

std::vector<int> v(1'000'000);

// Parallel sort
std::sort(std::execution::par, v.begin(), v.end());

// Parallel sort with vectorization hint
std::sort(std::execution::par_unseq, v.begin(), v.end());

// Parallel transform
std::transform(std::execution::par, v.begin(), v.end(), v.begin(),
               [](int x) { return x * 2; });

// Parallel reduce (unlike accumulate, allows reordering)
long sum = std::reduce(std::execution::par, v.begin(), v.end(), 0L);

// Parallel transform-reduce
long dot_product = std::transform_reduce(
    std::execution::par,
    v1.begin(), v1.end(),
    v2.begin(),
    0L
);

// Parallel for_each
std::for_each(std::execution::par_unseq, v.begin(), v.end(),
              [](int& x) { x = process(x); });
```

---

## Lock-Free Programming

### Lock-Free Stack

```cpp
template<typename T>
class LockFreeStack {
    struct Node {
        T data;
        Node* next;
        Node(T val) : data(std::move(val)), next(nullptr) {}
    };

    std::atomic<Node*> head_{nullptr};

public:
    void push(T value) {
        Node* new_node = new Node(std::move(value));
        new_node->next = head_.load(std::memory_order_relaxed);

        while (!head_.compare_exchange_weak(
                   new_node->next, new_node,
                   std::memory_order_release,
                   std::memory_order_relaxed)) {
            // Retry with updated head
        }
    }

    std::optional<T> pop() {
        Node* old_head = head_.load(std::memory_order_relaxed);

        while (old_head && !head_.compare_exchange_weak(
                              old_head, old_head->next,
                              std::memory_order_acquire,
                              std::memory_order_relaxed)) {
            // Retry with updated head
        }

        if (!old_head) return std::nullopt;

        T value = std::move(old_head->data);
        delete old_head;  // Careful: ABA problem!
        return value;
    }
};
```

---

## Common Concurrency Pitfalls

| Pitfall | Description | Solution |
|---------|-------------|----------|
| Data Race | Unsynchronized access | Use mutex or atomic |
| Deadlock | Circular lock dependency | Lock ordering, std::scoped_lock |
| Livelock | Threads can't progress | Backoff, randomization |
| Priority Inversion | High priority blocked | Priority inheritance |
| False Sharing | Cache line contention | alignas(64) padding |
| ABA Problem | CAS sees same value | Hazard pointers, epoch-based |

---

## Troubleshooting Decision Tree

```
Concurrency issue?
├── Crash or corruption
│   ├── Data race? → Run with ThreadSanitizer
│   ├── Use after free? → Check thread lifetimes
│   └── Iterator invalidation? → Copy or lock
├── Deadlock (program hangs)
│   ├── Get thread stacks: gdb -p <pid>, thread apply all bt
│   ├── Check lock ordering
│   └── Use std::scoped_lock for multiple locks
├── Performance issues
│   ├── Too much contention? → Reduce critical section
│   ├── False sharing? → Align to cache line
│   └── Lock convoy? → Use reader-writer lock
└── Inconsistent behavior
    ├── Memory ordering? → Use stronger ordering
    ├── Visibility? → Use proper synchronization
    └── Race condition? → Add mutex protection
```

---

## Unit Test Template

```cpp
#include <gtest/gtest.h>
#include <thread>
#include <vector>
#include <atomic>

class ConcurrencyTest : public ::testing::Test {
protected:
    static constexpr int NUM_THREADS = 8;
    static constexpr int ITERATIONS = 10000;
};

TEST_F(ConcurrencyTest, AtomicCounterIsThreadSafe) {
    std::atomic<int> counter{0};
    std::vector<std::thread> threads;

    for (int i = 0; i < NUM_THREADS; ++i) {
        threads.emplace_back([&counter]() {
            for (int j = 0; j < ITERATIONS; ++j) {
                counter.fetch_add(1);
            }
        });
    }

    for (auto& t : threads) t.join();

    EXPECT_EQ(counter.load(), NUM_THREADS * ITERATIONS);
}

TEST_F(ConcurrencyTest, MutexProtectsSharedData) {
    int counter = 0;
    std::mutex mtx;
    std::vector<std::thread> threads;

    for (int i = 0; i < NUM_THREADS; ++i) {
        threads.emplace_back([&]() {
            for (int j = 0; j < ITERATIONS; ++j) {
                std::lock_guard lock(mtx);
                ++counter;
            }
        });
    }

    for (auto& t : threads) t.join();

    EXPECT_EQ(counter, NUM_THREADS * ITERATIONS);
}

TEST_F(ConcurrencyTest, ThreadSafeQueueWorks) {
    ThreadSafeQueue<int> queue;
    std::atomic<int> sum{0};

    std::thread producer([&]() {
        for (int i = 1; i <= 100; ++i) {
            queue.push(i);
        }
    });

    std::thread consumer([&]() {
        for (int i = 0; i < 100; ++i) {
            sum += queue.pop();
        }
    });

    producer.join();
    consumer.join();

    EXPECT_EQ(sum.load(), 5050);  // Sum of 1..100
}
```

---

## Integration Points

| Component | Interface |
|-----------|-----------|
| `performance-optimizer` | Parallel optimization |
| `memory-specialist` | Thread-safe allocation |
| `cpp-debugger-agent` | Race detection (TSan) |
| `stl-master` | Parallel algorithms |

---

*C++ Plugin v3.0.0 - Production-Grade Development Skill*
