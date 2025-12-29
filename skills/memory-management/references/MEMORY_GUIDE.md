# Memory Management Guide

## RAII Pattern

```cpp
class FileHandle {
    FILE* file;
public:
    FileHandle(const char* path) : file(fopen(path, "r")) {
        if (!file) throw std::runtime_error("Cannot open file");
    }

    ~FileHandle() {
        if (file) fclose(file);
    }

    // Disable copy
    FileHandle(const FileHandle&) = delete;
    FileHandle& operator=(const FileHandle&) = delete;

    // Enable move
    FileHandle(FileHandle&& other) noexcept : file(other.file) {
        other.file = nullptr;
    }
};
```

## Smart Pointers

```cpp
// Unique - exclusive ownership
auto widget = std::make_unique<Widget>();

// Shared - reference counted
auto shared = std::make_shared<Widget>();
auto copy = shared;  // ref count: 2

// Weak - non-owning observer
std::weak_ptr<Widget> weak = shared;
if (auto locked = weak.lock()) {
    // Use safely
}
```

## Custom Allocator

```cpp
template<typename T>
class PoolAllocator {
    std::vector<T*> pool;
    size_t next = 0;
public:
    T* allocate(size_t n) {
        if (next + n > pool.size()) {
            pool.resize(pool.size() + 1024);
        }
        T* ptr = &pool[next];
        next += n;
        return ptr;
    }

    void deallocate(T*, size_t) {
        // Pool deallocates all at once
    }
};
```

## Memory Sanitizers

```bash
# AddressSanitizer
g++ -fsanitize=address -g myfile.cpp

# MemorySanitizer (Clang only)
clang++ -fsanitize=memory -g myfile.cpp

# Valgrind
valgrind --leak-check=full ./myprogram
```

---

*C++ Plugin - Memory Management Skill*
