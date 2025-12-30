---
name: concurrency
description: C++ multi-threading, parallel algorithms, and concurrent programming patterns
sasmp_version: "1.3.0"
bonded_agent: 01-modern-cpp-expert
bond_type: PRIMARY_BOND
---

# C++ Concurrency Skill

## Overview
Master C++ concurrency features from C++11 through C++20, including threads, atomics, futures, and parallel algorithms.

## Topics Covered

### Thread Basics
- std::thread creation and management
- Thread joining and detaching
- Thread-local storage
- Thread identification
- Hardware concurrency

### Synchronization Primitives
- std::mutex and std::lock_guard
- std::unique_lock and std::shared_lock
- std::condition_variable
- std::counting_semaphore (C++20)
- std::latch and std::barrier (C++20)

### Atomic Operations
- std::atomic types
- Memory ordering semantics
- Compare-and-swap operations
- Lock-free programming basics
- std::atomic_ref (C++20)

### Async Programming
- std::future and std::promise
- std::async and launch policies
- std::packaged_task
- Future continuations
- Coroutines (C++20)

### Parallel Algorithms
- Execution policies (seq, par, par_unseq)
- Parallel STL algorithms
- std::reduce and std::transform_reduce
- Custom parallel patterns

## Prerequisites
- Modern C++ fundamentals
- Memory management understanding
- STL familiarity

## Learning Outcomes
- Write thread-safe code
- Use synchronization correctly
- Implement parallel algorithms
- Avoid common concurrency bugs
