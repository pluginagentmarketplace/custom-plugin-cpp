---
name: cpp-basics
description: Master C++ fundamentals - variables, data types, operators, control flow, and program structure
sasmp_version: "1.3.0"
bonded_agent: cpp-fundamentals-agent
bond_type: PRIMARY_BOND
version: "1.0.0"
category: learning
---

# C++ Basics Skill

**🎓 Learning Skill - Fundamentals**

Master the foundation of C++ programming.

## Topics Covered

### 1. Variables & Data Types
```cpp
// Integer types
int count = 42;
short small = 100;
long large = 1000000L;
long long huge = 9223372036854775807LL;

// Floating point
float price = 19.99f;
double precise = 3.14159265358979;

// Characters and strings
char letter = 'A';
std::string name = "C++";

// Boolean
bool isActive = true;
```

### 2. Operators
```cpp
// Arithmetic: +, -, *, /, %
int sum = 10 + 5;
int remainder = 10 % 3;  // 1

// Comparison: ==, !=, <, >, <=, >=
bool equal = (5 == 5);   // true

// Logical: &&, ||, !
bool both = true && false;  // false

// Bitwise: &, |, ^, ~, <<, >>
int masked = 0xFF & 0x0F;  // 0x0F
```

### 3. Control Flow
```cpp
// Conditionals
if (x > 0) {
    // positive
} else if (x < 0) {
    // negative
} else {
    // zero
}

// Switch
switch (grade) {
    case 'A': break;
    case 'B': break;
    default: break;
}

// Loops
for (int i = 0; i < n; ++i) { }
while (condition) { }
do { } while (condition);
```

### 4. Functions
```cpp
// Function declaration
int add(int a, int b);

// Function definition
int add(int a, int b) {
    return a + b;
}

// Default parameters
void greet(std::string name = "World") {
    std::cout << "Hello, " << name << "!" << std::endl;
}
```

## Learning Path

1. **Variables & Types** → 2 hours
2. **Operators** → 1 hour
3. **Control Flow** → 3 hours
4. **Functions** → 3 hours
5. **Arrays** → 2 hours
6. **Practice** → 5+ hours

## Resources

- [C++ Reference](https://en.cppreference.com/w/)
- [Learn C++](https://www.learncpp.com/)

---

*C++ Plugin v2.0.0 - Learning Skill*
