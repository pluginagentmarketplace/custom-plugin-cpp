---
# ═══════════════════════════════════════════════════════════════════════════════
# SKILL: Memory Management
# Version: 3.0.0 | SASMP v1.3.0 Compliant | Production-Grade
# ═══════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# IDENTITY
# ─────────────────────────────────────────────────────────────────────────────
name: memory-management
version: "3.0.0"
description: >
  Production-grade skill for safe and efficient C++ memory management.
  Covers RAII, smart pointers, custom allocators, memory pools, and
  leak detection techniques.

# ─────────────────────────────────────────────────────────────────────────────
# COMPLIANCE
# ─────────────────────────────────────────────────────────────────────────────
sasmp_version: "1.3.0"
skill_version: "3.0.0"

# ─────────────────────────────────────────────────────────────────────────────
# BONDING
# ─────────────────────────────────────────────────────────────────────────────
bonded_agent: 02-memory-specialist
bond_type: PRIMARY_BOND
category: learning

# ─────────────────────────────────────────────────────────────────────────────
# PARAMETERS
# ─────────────────────────────────────────────────────────────────────────────
parameters:
  topic:
    type: string
    required: true
    enum: [raii, smart_pointers, allocators, pools, debugging, ownership]
  issue_type:
    type: string
    required: false
    enum: [leak, corruption, dangling, overflow]

# ─────────────────────────────────────────────────────────────────────────────
# ERROR HANDLING
# ─────────────────────────────────────────────────────────────────────────────
error_handling:
  retry_logic:
    max_attempts: 3
    backoff: exponential
    initial_delay_ms: 500
    jitter: true
  fallback:
    on_leak_detected: "suggest_raii_wrapper"
    on_corruption: "run_with_sanitizer"
---

# Memory Management Skill

**Production-Grade Learning Skill** | Safe Resource Handling

Master C++ memory management for safe, efficient, and leak-free code.

---

## Core Principles

### The Golden Rule: RAII

**Resource Acquisition Is Initialization**

```cpp
// ─────────────────────────────────────────────────────
// RAII wrapper for file handles
// ─────────────────────────────────────────────────────
class FileHandle {
    FILE* handle_{nullptr};

public:
    explicit FileHandle(const char* path, const char* mode)
        : handle_(fopen(path, mode))
    {
        if (!handle_) {
            throw std::runtime_error("Failed to open file");
        }
    }

    ~FileHandle() {
        if (handle_) fclose(handle_);
    }

    // Non-copyable
    FileHandle(const FileHandle&) = delete;
    FileHandle& operator=(const FileHandle&) = delete;

    // Movable
    FileHandle(FileHandle&& other) noexcept
        : handle_(std::exchange(other.handle_, nullptr)) {}

    FileHandle& operator=(FileHandle&& other) noexcept {
        if (this != &other) {
            if (handle_) fclose(handle_);
            handle_ = std::exchange(other.handle_, nullptr);
        }
        return *this;
    }

    FILE* get() const { return handle_; }
};

// Usage: automatic cleanup guaranteed
void processFile(const char* path) {
    FileHandle file(path, "r");  // Acquired
    // ... use file ...
}  // Automatically closed, even if exception thrown
```

---

## Smart Pointers

### Ownership Hierarchy

```
┌─────────────────────────────────────────────────────────────────┐
│  std::unique_ptr  │  Exclusive ownership (default choice)       │
│  std::shared_ptr  │  Shared ownership (reference counted)       │
│  std::weak_ptr    │  Non-owning observer (breaks cycles)        │
└─────────────────────────────────────────────────────────────────┘
```

### unique_ptr (Prefer This)

```cpp
// Creation (ALWAYS use make_unique)
auto widget = std::make_unique<Widget>(arg1, arg2);

// Array version
auto arr = std::make_unique<int[]>(100);

// Custom deleter
auto file = std::unique_ptr<FILE, decltype(&fclose)>(
    fopen("data.txt", "r"), &fclose
);

// Transfer ownership
void takeOwnership(std::unique_ptr<Widget> w);
takeOwnership(std::move(widget));  // Explicit move required
```

### shared_ptr (Use When Truly Needed)

```cpp
// Creation
auto shared = std::make_shared<Resource>();  // Single allocation!

// Copy = increment reference count
auto copy = shared;  // ref_count: 2

// Custom deleter
auto custom = std::shared_ptr<Database>(
    new Database(),
    [](Database* db) {
        db->close();
        delete db;
    }
);
```

### weak_ptr (Break Cycles)

```cpp
class Node {
public:
    std::shared_ptr<Node> next;
    std::weak_ptr<Node> prev;  // Weak to prevent cycle
};

// Safe access through lock()
void useWeakPtr(std::weak_ptr<Resource> weak) {
    if (auto shared = weak.lock()) {  // Returns shared_ptr or nullptr
        shared->doSomething();
    }
}
```

---

## Memory Issues & Solutions

### Quick Reference

| Problem | Detection | Solution |
|---------|-----------|----------|
| Memory leak | Valgrind, ASan | Use smart pointers |
| Dangling pointer | ASan | weak_ptr, proper lifetime |
| Double free | ASan | unique_ptr ownership |
| Buffer overflow | ASan | std::vector, std::span |
| Use after free | ASan | RAII, smart pointers |

### Detecting Leaks

```bash
# Valgrind (runtime)
valgrind --leak-check=full --show-leak-kinds=all ./program

# AddressSanitizer (compile-time instrumentation)
g++ -fsanitize=address -fno-omit-frame-pointer -g program.cpp
```

### Common Patterns

```cpp
// ❌ BAD: Raw pointer ownership unclear
Widget* createWidget() {
    return new Widget();  // Who deletes this?
}

// ✅ GOOD: Ownership explicit
std::unique_ptr<Widget> createWidget() {
    return std::make_unique<Widget>();
}

// ❌ BAD: Exception unsafe
void process() {
    Resource* r = new Resource();
    doSomething();  // May throw!
    delete r;       // Never reached if exception
}

// ✅ GOOD: Exception safe
void process() {
    auto r = std::make_unique<Resource>();
    doSomething();  // Even if throws, r is deleted
}
```

---

## Custom Allocators

### Pool Allocator

```cpp
template<typename T, size_t BlockSize = 4096>
class PoolAllocator {
    struct Block {
        std::array<std::byte, sizeof(T)> data;
        Block* next;
    };

    Block* freeList_{nullptr};
    std::vector<std::unique_ptr<Block[]>> blocks_;

public:
    T* allocate() {
        if (!freeList_) {
            allocateBlock();
        }
        Block* block = freeList_;
        freeList_ = block->next;
        return reinterpret_cast<T*>(&block->data);
    }

    void deallocate(T* ptr) {
        Block* block = reinterpret_cast<Block*>(ptr);
        block->next = freeList_;
        freeList_ = block;
    }

private:
    void allocateBlock() {
        constexpr size_t count = BlockSize / sizeof(Block);
        auto newBlocks = std::make_unique<Block[]>(count);

        for (size_t i = 0; i < count - 1; ++i) {
            newBlocks[i].next = &newBlocks[i + 1];
        }
        newBlocks[count - 1].next = freeList_;
        freeList_ = &newBlocks[0];

        blocks_.push_back(std::move(newBlocks));
    }
};
```

---

## Troubleshooting

### Decision Tree

```
Memory issue?
├── Leak suspected
│   ├── Run Valgrind → Shows "definitely lost"
│   ├── Check for raw `new` → Replace with make_unique
│   └── Check cyclic references → Use weak_ptr
├── Crash/Corruption
│   ├── Segfault at nullptr → Add null checks
│   ├── Double free → Ensure single owner (unique_ptr)
│   └── Use after free → Check object lifetime
└── Performance
    ├── Too many allocations → Use pool allocator
    ├── Fragmentation → Use arena allocator
    └── False sharing → Align to cache line
```

---

## Unit Test Template

```cpp
#include <gtest/gtest.h>
#include <memory>

TEST(SmartPointerTest, UniquePtrOwnership) {
    auto ptr = std::make_unique<int>(42);
    EXPECT_NE(ptr, nullptr);
    EXPECT_EQ(*ptr, 42);

    auto ptr2 = std::move(ptr);
    EXPECT_EQ(ptr, nullptr);  // Ownership transferred
    EXPECT_EQ(*ptr2, 42);
}

TEST(SmartPointerTest, SharedPtrRefCount) {
    auto shared1 = std::make_shared<int>(100);
    EXPECT_EQ(shared1.use_count(), 1);

    auto shared2 = shared1;
    EXPECT_EQ(shared1.use_count(), 2);
}

TEST(SmartPointerTest, WeakPtrExpired) {
    std::weak_ptr<int> weak;
    {
        auto shared = std::make_shared<int>(42);
        weak = shared;
        EXPECT_FALSE(weak.expired());
    }
    EXPECT_TRUE(weak.expired());
}
```

---

*C++ Plugin v3.0.0 - Production-Grade Learning Skill*
