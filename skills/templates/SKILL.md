---
# ═══════════════════════════════════════════════════════════════════════════════
# SKILL: Templates
# Version: 3.0.0 | SASMP v1.3.0 Compliant | Production-Grade
# ═══════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# IDENTITY
# ─────────────────────────────────────────────────────────────────────────────
name: templates
version: "3.0.0"
description: >
  Production-grade skill for C++ template programming and metaprogramming.
  Covers function/class templates, variadic templates, SFINAE, concepts,
  type traits, and compile-time computation.

# ─────────────────────────────────────────────────────────────────────────────
# COMPLIANCE
# ─────────────────────────────────────────────────────────────────────────────
sasmp_version: "1.3.0"
skill_version: "3.0.0"

# ─────────────────────────────────────────────────────────────────────────────
# BONDING
# ─────────────────────────────────────────────────────────────────────────────
bonded_agent: 01-modern-cpp-expert
bond_type: PRIMARY_BOND
category: development

# ─────────────────────────────────────────────────────────────────────────────
# PARAMETERS
# ─────────────────────────────────────────────────────────────────────────────
parameters:
  template_type:
    type: string
    required: false
    enum: [function, class, variable, alias, concept]
    description: "Type of template to work with"
  metaprogramming_level:
    type: string
    required: false
    enum: [basic, intermediate, advanced]
    default: intermediate
    description: "Complexity level of metaprogramming"
  cpp_standard:
    type: string
    required: false
    enum: [cpp11, cpp14, cpp17, cpp20, cpp23]
    default: cpp20
    description: "Target C++ standard"

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
    on_template_error: "simplify_and_retry"
    on_sfinae_failure: "use_concepts"
    on_compile_time_exceeded: "reduce_recursion"
    on_error_message_unclear: "add_static_assert"
  validation:
    check_template_instantiation: true
    verify_concept_satisfaction: true
    test_with_multiple_types: true
---

# Templates Skill

**Production-Grade Development Skill** | C++ Template Metaprogramming

Master C++ template programming from basics to advanced metaprogramming techniques.

---

## Template Basics

### Function Templates

```cpp
// Basic function template
template<typename T>
T max(T a, T b) {
    return (a > b) ? a : b;
}

// Multiple template parameters
template<typename T, typename U>
auto add(T a, U b) -> decltype(a + b) {
    return a + b;
}

// C++20: Abbreviated function template
auto multiply(auto a, auto b) {
    return a * b;
}

// Non-type template parameter
template<typename T, std::size_t N>
constexpr std::size_t array_size(T (&)[N]) {
    return N;
}

// Template argument deduction
max(1, 2);           // T = int
max(1.0, 2.0);       // T = double
max<double>(1, 2);   // Explicit: T = double
```

### Class Templates

```cpp
template<typename T, std::size_t Capacity = 64>
class FixedVector {
    std::array<T, Capacity> data_;
    std::size_t size_ = 0;

public:
    void push_back(const T& value) {
        if (size_ < Capacity) {
            data_[size_++] = value;
        }
    }

    T& operator[](std::size_t idx) { return data_[idx]; }
    const T& operator[](std::size_t idx) const { return data_[idx]; }
    std::size_t size() const { return size_; }
    static constexpr std::size_t capacity() { return Capacity; }
};

// Class Template Argument Deduction (CTAD) - C++17
FixedVector vec{1, 2, 3};  // Deduces FixedVector<int, 3>

// Deduction guide
template<typename T, typename... Args>
FixedVector(T, Args...) -> FixedVector<T, 1 + sizeof...(Args)>;
```

### Template Specialization

```cpp
// Primary template
template<typename T>
struct TypeInfo {
    static constexpr const char* name = "unknown";
};

// Full specialization
template<>
struct TypeInfo<int> {
    static constexpr const char* name = "int";
};

template<>
struct TypeInfo<double> {
    static constexpr const char* name = "double";
};

// Partial specialization
template<typename T>
struct TypeInfo<std::vector<T>> {
    static constexpr const char* name = "vector";
    using element_type = T;
};

// Partial specialization for pointers
template<typename T>
struct TypeInfo<T*> {
    static constexpr const char* name = "pointer";
    using pointed_type = T;
};
```

---

## Variadic Templates

### Parameter Packs

```cpp
// Variadic function template
template<typename... Args>
void print(Args... args) {
    ((std::cout << args << ' '), ...);  // Fold expression (C++17)
    std::cout << '\n';
}

// Sizeof... operator
template<typename... Args>
constexpr std::size_t count_args() {
    return sizeof...(Args);
}

// Recursive unpacking (pre-C++17)
template<typename T>
void print_recursive(T t) {
    std::cout << t << '\n';
}

template<typename T, typename... Rest>
void print_recursive(T first, Rest... rest) {
    std::cout << first << ' ';
    print_recursive(rest...);
}
```

### Fold Expressions (C++17)

```cpp
// Unary right fold: (pack op ...)
template<typename... Args>
auto sum(Args... args) {
    return (args + ...);  // ((a + b) + c) + d...
}

// Unary left fold: (... op pack)
template<typename... Args>
auto sum_left(Args... args) {
    return (... + args);  // a + (b + (c + d...))
}

// Binary fold with init
template<typename... Args>
auto sum_with_init(Args... args) {
    return (0 + ... + args);  // 0 + a + b + c...
}

// Logical folds
template<typename... Args>
bool all(Args... args) {
    return (... && args);  // All true
}

template<typename... Args>
bool any(Args... args) {
    return (... || args);  // Any true
}

// Comma fold for side effects
template<typename F, typename... Args>
void for_each_arg(F f, Args&&... args) {
    (f(std::forward<Args>(args)), ...);
}
```

---

## SFINAE and enable_if

### SFINAE Basics

```cpp
#include <type_traits>

// Enable only for integral types
template<typename T>
typename std::enable_if<std::is_integral<T>::value, T>::type
safe_divide(T a, T b) {
    return b != 0 ? a / b : 0;
}

// C++14 style
template<typename T>
std::enable_if_t<std::is_floating_point_v<T>, T>
safe_divide(T a, T b) {
    return b != T{0} ? a / b : std::numeric_limits<T>::quiet_NaN();
}

// Using void_t for detection idiom
template<typename, typename = void>
struct has_size : std::false_type {};

template<typename T>
struct has_size<T, std::void_t<decltype(std::declval<T>().size())>>
    : std::true_type {};

// Usage
static_assert(has_size<std::vector<int>>::value);
static_assert(!has_size<int>::value);
```

### Detection Idiom

```cpp
// is_detected implementation
template<typename, template<typename...> class, typename...>
struct is_detected_impl : std::false_type {};

template<template<typename...> class Op, typename... Args>
struct is_detected_impl<std::void_t<Op<Args...>>, Op, Args...>
    : std::true_type {};

template<template<typename...> class Op, typename... Args>
using is_detected = is_detected_impl<void, Op, Args...>;

// Detection expressions
template<typename T>
using has_begin_t = decltype(std::declval<T>().begin());

template<typename T>
using has_end_t = decltype(std::declval<T>().end());

template<typename T>
constexpr bool is_container_v =
    is_detected<has_begin_t, T>::value &&
    is_detected<has_end_t, T>::value;
```

---

## Concepts (C++20)

### Standard Concepts

```cpp
#include <concepts>

// Using standard concepts
template<std::integral T>
T gcd(T a, T b) {
    while (b != 0) {
        T t = b;
        b = a % b;
        a = t;
    }
    return a;
}

// Common standard concepts
template<std::floating_point T>
T sqrt_approx(T x);

template<std::copyable T>
void process(T value);

template<std::invocable<int> F>
void apply(F&& func);

template<std::ranges::range R>
void iterate(R&& range);
```

### Custom Concepts

```cpp
// Define concept with requires expression
template<typename T>
concept Hashable = requires(T a) {
    { std::hash<T>{}(a) } -> std::convertible_to<std::size_t>;
};

template<typename T>
concept Printable = requires(std::ostream& os, T value) {
    { os << value } -> std::same_as<std::ostream&>;
};

template<typename T>
concept Container = requires(T c) {
    typename T::value_type;
    typename T::iterator;
    { c.begin() } -> std::same_as<typename T::iterator>;
    { c.end() } -> std::same_as<typename T::iterator>;
    { c.size() } -> std::convertible_to<std::size_t>;
};

// Compound concepts
template<typename T>
concept Numeric = std::integral<T> || std::floating_point<T>;

// Use in function
template<Container C>
void process(const C& container) {
    for (const auto& item : container) {
        // ...
    }
}

// Constrained auto
void print_hashable(Hashable auto const& value) {
    std::cout << std::hash<std::decay_t<decltype(value)>>{}(value);
}
```

### Requires Clauses

```cpp
// Requires clause in template
template<typename T>
    requires std::is_arithmetic_v<T>
T average(std::span<const T> values) {
    return std::reduce(values.begin(), values.end()) / values.size();
}

// Trailing requires
template<typename T>
T* find(T* first, T* last, const T& value)
    requires std::equality_comparable<T>
{
    while (first != last && *first != value) {
        ++first;
    }
    return first;
}

// Concept subsumption for overloading
template<typename T>
void process(T val) requires std::integral<T> {
    std::cout << "integral\n";
}

template<typename T>
void process(T val) requires std::signed_integral<T> {  // More specific
    std::cout << "signed integral\n";
}
```

---

## Type Traits

### Standard Type Traits

```cpp
#include <type_traits>

// Type categories
static_assert(std::is_integral_v<int>);
static_assert(std::is_floating_point_v<double>);
static_assert(std::is_class_v<std::string>);
static_assert(std::is_pointer_v<int*>);

// Type properties
static_assert(std::is_const_v<const int>);
static_assert(std::is_trivially_copyable_v<int>);
static_assert(std::is_default_constructible_v<std::string>);

// Type transformations
using NoConst = std::remove_const_t<const int>;  // int
using Pointer = std::add_pointer_t<int>;         // int*
using Decayed = std::decay_t<int&>;              // int
using Common = std::common_type_t<int, double>;  // double

// Conditional type
template<typename T>
using storage_type = std::conditional_t<
    sizeof(T) <= sizeof(void*),
    T,                // Small: store by value
    std::unique_ptr<T>  // Large: store by pointer
>;
```

### Custom Type Traits

```cpp
// Custom type trait
template<typename T>
struct is_smart_pointer : std::false_type {};

template<typename T>
struct is_smart_pointer<std::unique_ptr<T>> : std::true_type {};

template<typename T>
struct is_smart_pointer<std::shared_ptr<T>> : std::true_type {};

template<typename T>
constexpr bool is_smart_pointer_v = is_smart_pointer<T>::value;

// Type transformation
template<typename T>
struct remove_all_pointers {
    using type = T;
};

template<typename T>
struct remove_all_pointers<T*> {
    using type = typename remove_all_pointers<T>::type;
};

template<typename T>
using remove_all_pointers_t = typename remove_all_pointers<T>::type;

// Usage
static_assert(std::is_same_v<remove_all_pointers_t<int***>, int>);
```

---

## Compile-Time Computation

### constexpr Functions

```cpp
// Compile-time factorial
constexpr int factorial(int n) {
    return n <= 1 ? 1 : n * factorial(n - 1);
}

static_assert(factorial(5) == 120);

// constexpr class
class ConstexprString {
    const char* data_;
    std::size_t size_;

public:
    constexpr ConstexprString(const char* str)
        : data_(str), size_(0) {
        while (str[size_] != '\0') ++size_;
    }

    constexpr std::size_t size() const { return size_; }
    constexpr char operator[](std::size_t i) const { return data_[i]; }
};

constexpr auto hello = ConstexprString("Hello");
static_assert(hello.size() == 5);
```

### consteval (C++20)

```cpp
// Guaranteed compile-time evaluation
consteval int square(int n) {
    return n * n;
}

constexpr int x = square(5);  // OK: compile-time
// int y = square(runtime_value);  // Error: must be compile-time

// Compile-time string hashing
consteval std::size_t hash_string(std::string_view str) {
    std::size_t hash = 0;
    for (char c : str) {
        hash = hash * 31 + static_cast<std::size_t>(c);
    }
    return hash;
}

// Use in switch
switch (hash_string(input)) {
    case hash_string("foo"): /* ... */ break;
    case hash_string("bar"): /* ... */ break;
}
```

---

## Template Error Messages

### Better Error Messages with Concepts

```cpp
// Without concepts - cryptic error
template<typename T>
void sort_container(T& container) {
    std::sort(container.begin(), container.end());
}
// Error with int: no member named 'begin' in 'int'

// With concepts - clear error
template<typename T>
concept Sortable = requires(T c) {
    { c.begin() } -> std::random_access_iterator;
    { c.end() } -> std::random_access_iterator;
};

template<Sortable T>
void sort_container(T& container) {
    std::sort(container.begin(), container.end());
}
// Error with int: constraints not satisfied [Sortable]
```

### Static Assert for Custom Messages

```cpp
template<typename T>
class NumericContainer {
    static_assert(std::is_arithmetic_v<T>,
        "NumericContainer requires an arithmetic type (int, float, etc.)");

    // ...
};

// Clear error:
// error: static assertion failed: NumericContainer requires an arithmetic type
```

---

## Troubleshooting Decision Tree

```
Template error?
├── "no matching function"
│   ├── Check template parameter deduction
│   ├── Check SFINAE conditions
│   └── Add explicit template arguments
├── "ambiguous call"
│   ├── Make one overload more specific
│   ├── Use concepts for disambiguation
│   └── Add explicit template arguments
├── "incomplete type"
│   ├── Forward declare issue
│   ├── Move implementation to .cpp (explicit instantiation)
│   └── Check circular dependencies
├── "exceeds maximum depth"
│   ├── Add base case to recursion
│   ├── Increase compiler limit
│   └── Use fold expressions instead
└── "constraint not satisfied"
    ├── Check concept requirements
    └── Add missing operations to type
```

---

## Unit Test Template

```cpp
#include <gtest/gtest.h>
#include <type_traits>

class TemplateTest : public ::testing::Test {};

// Test type traits
TEST_F(TemplateTest, TypeTraitsWork) {
    static_assert(std::is_integral_v<int>);
    static_assert(!std::is_integral_v<double>);
    static_assert(is_smart_pointer_v<std::unique_ptr<int>>);
}

// Test concepts
TEST_F(TemplateTest, ConceptsSatisfied) {
    static_assert(Hashable<int>);
    static_assert(Hashable<std::string>);
    static_assert(Container<std::vector<int>>);
    static_assert(!Container<int>);
}

// Test variadic templates
TEST_F(TemplateTest, VariadicSum) {
    EXPECT_EQ(sum(1, 2, 3, 4, 5), 15);
    EXPECT_DOUBLE_EQ(sum(1.0, 2.5, 3.5), 7.0);
}

// Test constexpr
TEST_F(TemplateTest, ConstexprComputation) {
    constexpr auto result = factorial(5);
    EXPECT_EQ(result, 120);

    constexpr auto hash = hash_string("test");
    EXPECT_NE(hash, 0);
}

// Test template specialization
TEST_F(TemplateTest, Specialization) {
    EXPECT_STREQ(TypeInfo<int>::name, "int");
    EXPECT_STREQ(TypeInfo<double>::name, "double");
    EXPECT_STREQ(TypeInfo<std::vector<int>>::name, "vector");
}
```

---

## Integration Points

| Component | Interface |
|-----------|-----------|
| `stl-master` | Generic containers |
| `modern-cpp-expert` | Concepts, constexpr |
| `performance-optimizer` | Compile-time optimization |
| `cpp-algorithms-agent` | Generic algorithms |

---

*C++ Plugin v3.0.0 - Production-Grade Development Skill*
