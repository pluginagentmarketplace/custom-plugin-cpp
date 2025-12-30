---
# ═══════════════════════════════════════════════════════════════════════════════
# COMMAND: cpp-review
# Version: 3.0.0 | SASMP v1.3.0 Compliant | Production-Grade
# ═══════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# IDENTITY
# ─────────────────────────────────────────────────────────────────────────────
name: cpp-review
version: "3.0.0"
description: Professional code review for C++ implementations

# ─────────────────────────────────────────────────────────────────────────────
# CLASSIFICATION
# ─────────────────────────────────────────────────────────────────────────────
category: development
priority: 2

# ─────────────────────────────────────────────────────────────────────────────
# TOOLS & PERMISSIONS
# ─────────────────────────────────────────────────────────────────────────────
allowed_tools:
  - Read
  - Grep
  - Glob

# ─────────────────────────────────────────────────────────────────────────────
# AGENT ROUTING
# ─────────────────────────────────────────────────────────────────────────────
routes_to:
  default: modern-cpp-expert
  focus:
    performance: performance-optimizer
    memory: memory-specialist
    thread: modern-cpp-expert
    security: modern-cpp-expert
    style: modern-cpp-expert

# ─────────────────────────────────────────────────────────────────────────────
# INPUT VALIDATION
# ─────────────────────────────────────────────────────────────────────────────
input_schema:
  type: object
  properties:
    focus:
      type: string
      required: false
      enum: [full, performance, memory, thread, security, style]
      default: full
      description: "Review focus area"
    scope:
      type: string
      required: false
      enum: [file, function, class, project]
      default: file
      description: "Scope of the review"
    file:
      type: string
      required: false
      description: "Specific file to review"

# ─────────────────────────────────────────────────────────────────────────────
# EXIT CODES
# ─────────────────────────────────────────────────────────────────────────────
exit_codes:
  0: "Success - review completed, no critical issues"
  1: "Critical issues found"
  2: "Major issues found"
  3: "File not found"
  4: "Parse error"

# ─────────────────────────────────────────────────────────────────────────────
# ERROR HANDLING
# ─────────────────────────────────────────────────────────────────────────────
error_handling:
  on_file_not_found: "request_correct_path"
  on_parse_error: "report_syntax_issues"
  on_large_file: "review_in_sections"
  on_complex_code: "break_into_components"
---

# /cpp-review

**Development Command** | Professional Code Review

Comprehensive code review with detailed feedback on C++ implementations.

---

## Usage

```
/cpp-review [focus] [--scope=file] [--file=path]
```

## Arguments

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `focus` | string | No | full, performance, memory, thread, security, style |
| `--scope` | string | No | file, function, class, project |
| `--file` | string | No | Specific file to review |

---

## Review Aspects

| Aspect | What's Checked |
|--------|----------------|
| **Correctness** | Logic errors, edge cases, undefined behavior |
| **Efficiency** | Algorithm choice, complexity, redundant operations |
| **Safety** | Memory safety, null checks, bounds checking |
| **Style** | C++ Core Guidelines, naming, formatting |
| **Readability** | Clear code, good naming, documentation |
| **Thread Safety** | Race conditions, proper synchronization |
| **Security** | Input validation, buffer overflows, injection |

---

## Examples

```bash
# Full review of current file
/cpp-review

# Performance-focused review
/cpp-review performance

# Memory safety review
/cpp-review memory

# Thread safety review
/cpp-review thread

# Review specific file
/cpp-review --file=src/parser.cpp

# Review entire class
/cpp-review --scope=class
```

---

## Feedback Format

### 1. Summary
```
Grade: B+
Files Reviewed: 3
Total Issues: 7 (0 Critical, 2 Major, 5 Minor)
```

### 2. Strengths
- Good use of RAII
- Clear function naming
- Proper const-correctness

### 3. Issues (by Severity)

#### Critical Issues
```cpp
// Line 42: Use after free
auto* ptr = obj.get();
obj.reset();
ptr->method();  // 🔴 CRITICAL: Use after free
```

#### Major Issues
```cpp
// Line 78: Potential null dereference
void process(Widget* w) {
    w->run();  // 🟠 MAJOR: No null check
}
```

#### Minor Issues
```cpp
// Line 95: Prefer emplace_back
vec.push_back(Widget{});  // 🟡 MINOR: Use emplace_back
```

### 4. Suggestions
```cpp
// Line 120: Consider using string_view
void log(const std::string& msg);  // 🟢 Consider: string_view
```

---

## Severity Levels

| Level | Symbol | Meaning | Action Required |
|-------|--------|---------|-----------------|
| **Critical** | 🔴 | Security issue, crash, UB | Must fix immediately |
| **Major** | 🟠 | Logic error, performance issue | Should fix |
| **Minor** | 🟡 | Style, readability issue | Nice to fix |
| **Suggestion** | 🟢 | Optional improvement | Consider for future |

---

## Review Checklist

### Correctness
- [ ] No undefined behavior
- [ ] All paths return a value
- [ ] Correct operator precedence
- [ ] No integer overflow in arithmetic
- [ ] Edge cases handled

### Memory Safety
- [ ] No memory leaks
- [ ] No use after free
- [ ] No double free
- [ ] Smart pointers used appropriately
- [ ] RAII for all resources

### Performance
- [ ] Appropriate algorithm complexity
- [ ] No unnecessary copies
- [ ] Containers reserved when size known
- [ ] No redundant allocations

### Thread Safety
- [ ] Shared data properly synchronized
- [ ] No data races
- [ ] No deadlock potential
- [ ] Atomic operations where needed

### Style & Readability
- [ ] Consistent naming convention
- [ ] Functions under 50 lines
- [ ] Clear variable names
- [ ] Appropriate comments
- [ ] No magic numbers

### Modern C++
- [ ] Smart pointers over raw
- [ ] Range-based for loops
- [ ] auto where appropriate
- [ ] constexpr where possible
- [ ] noexcept where applicable

---

## Common Issues Found

| Issue | Frequency | Severity | Fix |
|-------|-----------|----------|-----|
| Missing null check | Very Common | Major | Add guard |
| Raw new/delete | Common | Major | Use smart ptr |
| Copy instead of move | Common | Minor | Add std::move |
| Unused variable | Common | Minor | Remove or use |
| Magic numbers | Common | Minor | Use named const |
| Missing const | Very Common | Minor | Add const |
| Poor naming | Common | Minor | Rename clearly |

---

## Refactoring Examples

### Before
```cpp
void process(Widget* w) {
    if (w != NULL) {
        vector<int> v;
        for (int i = 0; i < 100; i++) {
            v.push_back(i);
        }
        w->run();
    }
}
```

### After
```cpp
void process(Widget* widget) {
    if (!widget) return;  // Early return

    std::vector<int> values;
    values.reserve(100);  // Reserve known size

    for (int i = 0; i < 100; ++i) {
        values.emplace_back(i);  // emplace_back
    }

    widget->run();
}
```

---

## Error Messages

| Error | Cause | Solution |
|-------|-------|----------|
| "File not found" | Wrong path | Provide correct file path |
| "Parse error" | Invalid C++ syntax | Fix syntax errors first |
| "Too large" | File exceeds limit | Review in sections |

---

## Integration Points

| Component | Interface |
|-----------|-----------|
| `modern-cpp-expert` | General review |
| `performance-optimizer` | Performance focus |
| `memory-specialist` | Memory focus |
| `build-engineer` | Build configuration |

---

*C++ Plugin v3.0.0 - Production-Grade Development Command*
