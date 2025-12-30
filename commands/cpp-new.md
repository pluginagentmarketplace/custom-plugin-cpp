---
# ═══════════════════════════════════════════════════════════════════════════════
# COMMAND: cpp-new
# Version: 3.0.0 | SASMP v1.3.0 Compliant | Production-Grade
# ═══════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# IDENTITY
# ─────────────────────────────────────────────────────────────────────────────
name: cpp-new
version: "3.0.0"
description: Create a new C++ project with modern best-practice structure

# ─────────────────────────────────────────────────────────────────────────────
# CLASSIFICATION
# ─────────────────────────────────────────────────────────────────────────────
category: development
priority: 1

# ─────────────────────────────────────────────────────────────────────────────
# TOOLS & PERMISSIONS
# ─────────────────────────────────────────────────────────────────────────────
allowed_tools:
  - Read
  - Write
  - Bash
  - Glob

# ─────────────────────────────────────────────────────────────────────────────
# AGENT ROUTING
# ─────────────────────────────────────────────────────────────────────────────
routes_to: build-engineer
fallback_agent: modern-cpp-expert

# ─────────────────────────────────────────────────────────────────────────────
# INPUT VALIDATION
# ─────────────────────────────────────────────────────────────────────────────
input_schema:
  type: object
  properties:
    project_name:
      type: string
      required: true
      pattern: "^[a-zA-Z][a-zA-Z0-9_-]*$"
      description: "Project name (alphanumeric, hyphens, underscores)"
    template:
      type: string
      required: false
      enum: [cli, lib, app, test, full, minimal]
      default: full
      description: "Project template type"
    cpp_standard:
      type: integer
      required: false
      enum: [17, 20, 23]
      default: 20
      description: "C++ standard version"

# ─────────────────────────────────────────────────────────────────────────────
# EXIT CODES
# ─────────────────────────────────────────────────────────────────────────────
exit_codes:
  0: "Success - project created"
  1: "Invalid project name"
  2: "Directory already exists"
  3: "Template not found"
  4: "File system error"
  5: "CMake generation failed"

# ─────────────────────────────────────────────────────────────────────────────
# ERROR HANDLING
# ─────────────────────────────────────────────────────────────────────────────
error_handling:
  on_invalid_name: "suggest_valid_alternatives"
  on_dir_exists: "prompt_overwrite_or_rename"
  on_fs_error: "check_permissions"
  on_cmake_fail: "provide_manual_setup"
---

# /cpp-new

**Development Command** | Create New C++ Project

Generate a production-ready C++ project with modern CMake, testing, and tooling.

---

## Usage

```
/cpp-new <project-name> [template] [--std=20]
```

## Arguments

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `project-name` | string | Yes | Name of the project (alphanumeric, hyphens) |
| `template` | string | No | Project template (default: full) |
| `--std` | integer | No | C++ standard: 17, 20, 23 (default: 20) |

---

## Project Templates

| Template | Description | Includes |
|----------|-------------|----------|
| **cli** | Command-line application | argparse, logging, exit codes |
| **lib** | Library project | Header-only or static/shared lib |
| **app** | Application with GUI | Qt/SDL integration ready |
| **test** | Test-focused project | GTest, Catch2 setup |
| **full** | Complete project | All features, CI/CD ready |
| **minimal** | Bare minimum | Just CMake and main.cpp |

---

## Examples

```bash
# Full-featured project with C++20
/cpp-new my-project full

# CLI tool with C++23
/cpp-new my-cli cli --std=23

# Header-only library
/cpp-new my-lib lib

# Minimal starter
/cpp-new quick-test minimal
```

---

## Generated Structure

```
my-project/
├── CMakeLists.txt              # Modern CMake 3.20+
├── CMakePresets.json           # Build presets
├── src/
│   ├── main.cpp                # Entry point
│   └── lib/
│       └── core.cpp            # Library source
├── include/
│   └── my-project/
│       └── core.hpp            # Public headers
├── tests/
│   ├── CMakeLists.txt
│   └── test_core.cpp           # Unit tests
├── cmake/
│   ├── CompilerWarnings.cmake  # Warning flags
│   ├── Sanitizers.cmake        # ASan, UBSan config
│   └── CPM.cmake               # Package manager
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI
├── .clang-format               # Code formatting
├── .clang-tidy                 # Static analysis
├── .gitignore                  # Git ignore rules
├── LICENSE                     # MIT license
└── README.md                   # Project documentation
```

---

## CMake Features Included

### Core Configuration
```cmake
cmake_minimum_required(VERSION 3.20)
project(my-project VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
```

### Build Options
```cmake
option(BUILD_TESTING "Build tests" ON)
option(ENABLE_SANITIZERS "Enable ASan/UBSan" ON)
option(ENABLE_COVERAGE "Enable code coverage" OFF)
option(ENABLE_LTO "Enable link-time optimization" OFF)
```

### Compiler Warnings (Auto-configured)
- GCC/Clang: `-Wall -Wextra -Wpedantic -Werror`
- MSVC: `/W4 /WX`

---

## Quick Start After Creation

```bash
# Navigate to project
cd my-project

# Configure (Debug)
cmake --preset debug

# Build
cmake --build build/debug

# Run tests
ctest --test-dir build/debug --output-on-failure

# Configure (Release)
cmake --preset release
cmake --build build/release
```

---

## Validation Rules

| Rule | Validation |
|------|------------|
| Project name | Must start with letter, alphanumeric/hyphens only |
| Directory | Must not already exist (or confirm overwrite) |
| Template | Must be one of: cli, lib, app, test, full, minimal |
| C++ Standard | Must be 17, 20, or 23 |

---

## Error Messages

| Error | Cause | Solution |
|-------|-------|----------|
| "Invalid project name" | Name contains invalid characters | Use alphanumeric and hyphens |
| "Directory exists" | Project folder already present | Choose different name or use --force |
| "Template not found" | Unknown template name | Use one of: cli, lib, app, test, full |
| "CMake failed" | CMake configuration error | Check CMake version (need 3.20+) |

---

## Integration Points

| Component | Interface |
|-----------|-----------|
| `build-engineer` | CMake configuration |
| `modern-cpp-expert` | C++ standard features |
| `cpp-debugger-agent` | Sanitizer setup |
| `performance-optimizer` | Release build flags |

---

*C++ Plugin v3.0.0 - Production-Grade Development Command*
