---
name: cpp-review
description: Professional code review for C++ implementations
allowed-tools: Read, Grep, Glob
category: development
---

# /cpp-review

**🔧 Development Mode Command**

Professional code review with detailed feedback on your C++ implementation.

## Review Aspects

| Aspect | What's Checked |
|--------|----------------|
| **Correctness** | Does it work as intended? |
| **Efficiency** | Optimal algorithms and complexity |
| **Safety** | Memory safety, no UB |
| **Style** | C++ Core Guidelines compliance |
| **Readability** | Clear naming, good documentation |
| **Thread Safety** | Proper synchronization |

## Usage

```
/cpp-review [focus]
```

## Examples

```bash
/cpp-review                   # Full review
/cpp-review function          # Review single function
/cpp-review class             # Review class design
/cpp-review performance       # Focus on optimization
/cpp-review memory            # Focus on memory safety
/cpp-review thread            # Focus on concurrency
```

## Feedback Format

1. **Summary**: Overall quality assessment (A-F grade)
2. **Strengths**: What's done well
3. **Issues**: Problems with severity (Critical/Major/Minor)
4. **Suggestions**: Specific improvements
5. **Refactored Code**: How to improve

## Severity Levels

| Level | Meaning |
|-------|---------|
| 🔴 **Critical** | Security issue or crash |
| 🟠 **Major** | Logic error or performance issue |
| 🟡 **Minor** | Style or readability issue |
| 🟢 **Suggestion** | Optional improvement |

## Checklist Used

- [ ] No undefined behavior
- [ ] No memory leaks
- [ ] Const correctness
- [ ] RAII for resources
- [ ] Exception safety
- [ ] Thread safety (if applicable)
- [ ] Clear naming conventions
- [ ] Documented public API

---

*C++ Plugin v2.0.0 - Development Command*
