# C++ Programming System

[![SASMP v1.3.0](https://img.shields.io/badge/SASMP-v1.3.0-blue.svg)](https://github.com/pluginagentmarketplace)
[![EQHM Compliant](https://img.shields.io/badge/EQHM-Compliant-green.svg)](https://github.com/pluginagentmarketplace)
[![Version](https://img.shields.io/badge/Version-3.0.0-purple.svg)](CHANGELOG.md)
[![C++](https://img.shields.io/badge/C++-11%2F14%2F17%2F20%2F23-orange?logo=cplusplus)](https://isocpp.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Production-Grade C++ Development Plugin** - Complete agent-skill architecture for learning and professional development.

---

## Plugin Overview

| Metric | Count | Status |
|--------|-------|--------|
| **Agents** | 9 | Production-Grade |
| **Skills** | 12 | Production-Grade |
| **Commands** | 6 | Production-Grade |
| **SASMP Version** | 1.3.0 | Compliant |
| **Plugin Version** | 3.0.0 | Current |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    COMMAND LAYER                            │
│  /cpp-new  /cpp-learn  /cpp-debug  /cpp-optimize           │
│  /cpp-practice  /cpp-review                                 │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    AGENT LAYER (9)                          │
├─────────────────────────────────────────────────────────────┤
│  modern-cpp-expert    memory-specialist    stl-master       │
│  build-engineer       performance-optimizer                 │
│  cpp-fundamentals     cpp-oop-agent       cpp-algorithms    │
│  cpp-debugger-agent                                         │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    SKILL LAYER (12)                         │
├─────────────────────────────────────────────────────────────┤
│  cpp-basics    oop-patterns    memory-management    stl     │
│  algorithms    modern-cpp      build-systems                │
│  performance   debugging       concurrency                  │
│  templates     testing                                      │
└─────────────────────────────────────────────────────────────┘
```

---

## Agents

### Learning Agents

| Agent | Primary Skill | Expertise |
|-------|---------------|-----------|
| `cpp-fundamentals-agent` | cpp-basics | Variables, types, control flow, functions |
| `cpp-oop-agent` | oop-patterns | Classes, inheritance, polymorphism, SOLID |
| `cpp-algorithms-agent` | algorithms | Complexity, sorting, graphs, DP |

### Development Agents

| Agent | Primary Skills | Expertise |
|-------|----------------|-----------|
| `modern-cpp-expert` | modern-cpp, templates, concurrency | C++11-23, metaprogramming |
| `memory-specialist` | memory-management | RAII, smart pointers, allocation |
| `stl-master` | stl | Containers, algorithms, iterators |
| `build-engineer` | build-systems | CMake, Conan, vcpkg, CI/CD |
| `performance-optimizer` | performance | Profiling, SIMD, cache optimization |
| `cpp-debugger-agent` | debugging, testing | GDB, sanitizers, unit testing |

---

## Commands

| Command | Routes To | Description |
|---------|-----------|-------------|
| `/cpp-new <name> <type>` | build-engineer | Create new C++ project |
| `/cpp-learn <topic>` | topic-based routing | Interactive learning |
| `/cpp-practice <difficulty>` | difficulty-based routing | Coding exercises |
| `/cpp-debug <issue>` | cpp-debugger-agent | Debug assistance |
| `/cpp-optimize <focus>` | performance-optimizer | Performance tuning |
| `/cpp-review <focus>` | modern-cpp-expert | Code review |

### Project Templates

```bash
/cpp-new my-app cli      # Command-line application
/cpp-new my-lib lib      # Static/shared library
/cpp-new my-app app      # GUI application
/cpp-new my-test test    # Test project
/cpp-new my-proj full    # Full project structure
```

---

## Skills

### Core Skills

| Skill | Agent | Category |
|-------|-------|----------|
| `cpp-basics` | cpp-fundamentals-agent | Fundamentals |
| `oop-patterns` | cpp-oop-agent | Design Patterns |
| `memory-management` | memory-specialist | Core |
| `stl` | stl-master | Standard Library |
| `algorithms` | cpp-algorithms-agent | Algorithms |

### Advanced Skills

| Skill | Agent | Category |
|-------|-------|----------|
| `modern-cpp` | modern-cpp-expert | Modern Features |
| `build-systems` | build-engineer | Tooling |
| `performance` | performance-optimizer | Optimization |
| `debugging` | cpp-debugger-agent | Tooling |
| `concurrency` | modern-cpp-expert | Advanced |
| `templates` | modern-cpp-expert | Advanced |
| `testing` | cpp-debugger-agent | QA |

---

## Production-Grade Features

### SASMP v1.3.0 Compliance

- Type-safe input/output schemas
- Activation triggers (keywords + patterns)
- Error handling with exponential backoff
- Fallback agent configuration
- Observability hooks

### Error Handling

```yaml
error_handling:
  retry_logic:
    max_attempts: 3
    backoff: exponential
    initial_delay_ms: 500
    max_delay_ms: 8000
    jitter: true
```

### Observability

- Structured logging
- Metrics collection
- Distributed tracing support

---

## Quick Start

### Learning Flow

```bash
# Start with fundamentals
/cpp-learn fundamentals

# Practice with exercises
/cpp-practice easy

# Progress to OOP
/cpp-learn oop

# Challenge yourself
/cpp-practice hard algorithms
```

### Development Flow

```bash
# Create project
/cpp-new my-service cli

# Write code...

# Review
/cpp-review

# Debug if needed
/cpp-debug

# Optimize
/cpp-optimize profile
```

---

## File Structure

```
custom-plugin-cpp/
├── plugin.json              # Plugin manifest
├── ARCHITECTURE.md          # Dependency graph
├── CHANGELOG.md             # Version history
├── agents/                  # 9 agent definitions
│   ├── 01-modern-cpp-expert.md
│   ├── 02-memory-specialist.md
│   ├── 03-stl-master.md
│   ├── 04-build-engineer.md
│   ├── 05-performance-optimizer.md
│   ├── cpp-fundamentals-agent.md
│   ├── cpp-oop-agent.md
│   ├── cpp-algorithms-agent.md
│   └── cpp-debugger-agent.md
├── skills/                  # 12 skill definitions
│   ├── cpp-basics/
│   ├── oop-patterns/
│   ├── memory-management/
│   ├── stl/
│   ├── algorithms/
│   ├── modern-cpp/
│   ├── build-systems/
│   ├── performance/
│   ├── debugging/
│   ├── concurrency/
│   ├── templates/
│   └── testing/
├── commands/                # 6 command definitions
│   ├── cpp-new.md
│   ├── cpp-learn.md
│   ├── cpp-practice.md
│   ├── cpp-debug.md
│   ├── cpp-optimize.md
│   └── cpp-review.md
└── hooks/
    └── hooks.json           # Lifecycle hooks
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| **3.0.0** | 2025-12-30 | Production-grade upgrade, EQHM compliance |
| 2.0.0 | 2025-12-29 | Hybrid mode, merged plugins |
| 1.0.0 | 2025-12-29 | Initial release |

See [CHANGELOG.md](CHANGELOG.md) for detailed history.

---

## Resources

- [C++ Reference](https://en.cppreference.com/)
- [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/)
- [Learn C++](https://www.learncpp.com/)
- [ARCHITECTURE.md](ARCHITECTURE.md) - Plugin architecture details

---

## License

MIT License - See [LICENSE](LICENSE) for details.

---

**Maintained by:** Dr. Umit Kacar & Muhsin Elcicek
