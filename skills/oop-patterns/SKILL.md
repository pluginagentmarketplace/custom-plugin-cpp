---
name: oop-patterns
description: Master Object-Oriented Programming in C++ - classes, inheritance, polymorphism, and design patterns
sasmp_version: "1.3.0"
bonded_agent: cpp-oop-agent
bond_type: PRIMARY_BOND
version: "1.0.0"
category: learning
---

# OOP Patterns Skill

**🎓 Learning Skill - Object-Oriented Programming**

Master C++ OOP concepts and design patterns.

## Core Concepts

### 1. Classes & Objects
```cpp
class Rectangle {
private:
    double width_;
    double height_;

public:
    // Constructor
    Rectangle(double w, double h) : width_(w), height_(h) {}

    // Methods
    double area() const { return width_ * height_; }
    double perimeter() const { return 2 * (width_ + height_); }

    // Getters
    double width() const { return width_; }
    double height() const { return height_; }
};
```

### 2. Inheritance
```cpp
class Shape {
public:
    virtual double area() const = 0;  // Pure virtual
    virtual ~Shape() = default;       // Virtual destructor
};

class Circle : public Shape {
    double radius_;
public:
    Circle(double r) : radius_(r) {}
    double area() const override {
        return 3.14159 * radius_ * radius_;
    }
};
```

### 3. Polymorphism
```cpp
void printArea(const Shape& shape) {
    std::cout << "Area: " << shape.area() << "\n";
}

// Works with any Shape subclass
Circle c(5);
Rectangle r(3, 4);
printArea(c);  // Dynamic dispatch
printArea(r);  // Dynamic dispatch
```

### 4. SOLID Principles

| Principle | Description |
|-----------|-------------|
| **S**ingle Responsibility | One class, one job |
| **O**pen/Closed | Open for extension, closed for modification |
| **L**iskov Substitution | Subtypes replaceable for base types |
| **I**nterface Segregation | Many specific interfaces > one general |
| **D**ependency Inversion | Depend on abstractions, not concretions |

## Design Patterns

### Creational
- **Factory**: Create objects without exposing creation logic
- **Singleton**: Ensure single instance
- **Builder**: Construct complex objects step by step

### Structural
- **Adapter**: Convert interface to another
- **Decorator**: Add behavior dynamically
- **Facade**: Simplified interface to complex system

### Behavioral
- **Observer**: Notify dependents of state changes
- **Strategy**: Interchangeable algorithms
- **Command**: Encapsulate request as object

## Resources

- [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/)
- [Design Patterns (GoF)](https://refactoring.guru/design-patterns/cpp)

---

*C++ Plugin v2.0.0 - Learning Skill*
