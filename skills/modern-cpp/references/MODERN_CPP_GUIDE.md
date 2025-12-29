# Modern C++ Guide

## Move Semantics

```cpp
class Widget {
    std::string data;
public:
    // Move constructor
    Widget(Widget&& other) noexcept
        : data(std::move(other.data)) {}

    // Move assignment
    Widget& operator=(Widget&& other) noexcept {
        data = std::move(other.data);
        return *this;
    }
};

// Usage
Widget w1;
Widget w2 = std::move(w1);  // w1 is now in moved-from state
```

## Smart Pointers

```cpp
// Unique ownership
auto ptr = std::make_unique<Widget>();
auto ptr2 = std::move(ptr);  // Transfer ownership

// Shared ownership
auto shared = std::make_shared<Widget>();
auto copy = shared;  // Reference count: 2

// Weak reference
std::weak_ptr<Widget> weak = shared;
if (auto locked = weak.lock()) {
    // Use locked
}
```

## Lambda Expressions

```cpp
// Basic lambda
auto add = [](int a, int b) { return a + b; };

// Capture by value
int x = 10;
auto f = [x]() { return x * 2; };

// Capture by reference
auto g = [&x]() { x++; };

// Generic lambda (C++14)
auto print = [](auto value) { std::cout << value; };

// Init capture (C++14)
auto h = [y = std::move(x)]() { return y; };
```

## Concepts (C++20)

```cpp
template<typename T>
concept Numeric = std::integral<T> || std::floating_point<T>;

template<Numeric T>
T add(T a, T b) {
    return a + b;
}

// Or with requires clause
template<typename T>
    requires Numeric<T>
T multiply(T a, T b) {
    return a * b;
}
```

## Ranges (C++20)

```cpp
#include <ranges>

std::vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

auto result = nums
    | std::views::filter([](int n) { return n % 2 == 0; })
    | std::views::transform([](int n) { return n * n; })
    | std::views::take(3);

// Result: 4, 16, 36
```

---

*C++ Plugin - Modern C++ Skill*
