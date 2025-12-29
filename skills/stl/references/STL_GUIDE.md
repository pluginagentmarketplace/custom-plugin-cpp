# STL Guide

## Container Selection

| Need | Use |
|------|-----|
| Default, random access | std::vector |
| Fast lookup by key | std::unordered_map |
| Ordered key-value | std::map |
| Unique elements | std::set |
| LIFO | std::stack |
| FIFO | std::queue |
| Priority access | std::priority_queue |

## Common Algorithms

```cpp
#include <algorithm>
#include <numeric>

std::vector<int> v = {5, 2, 8, 1, 9};

// Sorting
std::sort(v.begin(), v.end());

// Finding
auto it = std::find(v.begin(), v.end(), 8);

// Transform
std::transform(v.begin(), v.end(), v.begin(),
    [](int x) { return x * 2; });

// Accumulate
int sum = std::accumulate(v.begin(), v.end(), 0);

// Remove-erase idiom
v.erase(std::remove_if(v.begin(), v.end(),
    [](int x) { return x < 5; }), v.end());
```

## Modern STL (C++17+)

```cpp
// std::optional
std::optional<int> find_value(const std::vector<int>& v, int target) {
    auto it = std::find(v.begin(), v.end(), target);
    return it != v.end() ? std::optional(*it) : std::nullopt;
}

// std::variant
std::variant<int, std::string, double> value = "hello";
std::visit([](auto&& arg) { std::cout << arg; }, value);

// Parallel algorithms
std::sort(std::execution::par, v.begin(), v.end());
```

---

*C++ Plugin - STL Skill*
