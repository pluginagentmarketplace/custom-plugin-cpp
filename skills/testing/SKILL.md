---
# ═══════════════════════════════════════════════════════════════════════════════
# SKILL: testing
# Version: 3.0.0 | SASMP v1.3.0 Compliant | Production-Grade
# ═══════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# IDENTITY
# ─────────────────────────────────────────────────────────────────────────────
name: testing
version: "3.0.0"
description: >
  Production-grade C++ testing expertise including unit testing, mocking, TDD,
  BDD, fuzzing, benchmark testing, coverage analysis, and CI integration.

# ─────────────────────────────────────────────────────────────────────────────
# COMPLIANCE
# ─────────────────────────────────────────────────────────────────────────────
sasmp_version: "1.3.0"
eqhm_compliant: true
last_audit: "2025-12-30"

# ─────────────────────────────────────────────────────────────────────────────
# AGENT BOND
# ─────────────────────────────────────────────────────────────────────────────
bonded_agent: cpp-debugger-agent
bond_type: PRIMARY_BOND
fallback_agent: modern-cpp-expert

# ─────────────────────────────────────────────────────────────────────────────
# CLASSIFICATION
# ─────────────────────────────────────────────────────────────────────────────
category: quality-assurance
complexity: intermediate-advanced
estimated_tokens: 3000

# ─────────────────────────────────────────────────────────────────────────────
# TRIGGERS
# ─────────────────────────────────────────────────────────────────────────────
activation_triggers:
  keywords:
    - "test"
    - "unit test"
    - "gtest"
    - "catch2"
    - "mock"
    - "gmock"
    - "tdd"
    - "bdd"
    - "coverage"
    - "fuzzing"
    - "benchmark"
  patterns:
    - "write tests for"
    - "how to test"
    - "test coverage"
    - "mock object"
    - "test fixture"

# ─────────────────────────────────────────────────────────────────────────────
# CAPABILITIES
# ─────────────────────────────────────────────────────────────────────────────
capabilities:
  primary:
    - Unit test writing with Google Test and Catch2
    - Mock object creation with Google Mock
    - Test fixture design and setup
    - Parameterized and data-driven tests
    - Test-driven development workflow
  secondary:
    - Fuzz testing with libFuzzer
    - Benchmark testing with Google Benchmark
    - Code coverage analysis (gcov, lcov)
    - CI/CD test pipeline setup
    - Property-based testing

# ─────────────────────────────────────────────────────────────────────────────
# INPUT/OUTPUT SCHEMA
# ─────────────────────────────────────────────────────────────────────────────
input_schema:
  type: object
  properties:
    code_to_test:
      type: string
      description: "C++ code or function to write tests for"
    framework:
      type: string
      enum: [gtest, catch2, boost_test, doctest]
      default: gtest
      description: "Testing framework to use"
    test_type:
      type: string
      enum: [unit, integration, benchmark, fuzz]
      default: unit
    coverage_target:
      type: number
      minimum: 0
      maximum: 100
      default: 80
      description: "Target coverage percentage"

output_schema:
  type: object
  properties:
    test_code:
      type: string
      description: "Generated test code"
    cmake_config:
      type: string
      description: "CMake configuration for tests"
    coverage_report:
      type: object
      description: "Coverage analysis results"
    recommendations:
      type: array
      items:
        type: string
      description: "Testing improvement suggestions"

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
    on_framework_error: "suggest_alternative_framework"
    on_compilation_error: "provide_build_guidance"
    on_coverage_error: "manual_coverage_check"

# ─────────────────────────────────────────────────────────────────────────────
# OBSERVABILITY
# ─────────────────────────────────────────────────────────────────────────────
observability:
  logging:
    level: INFO
    format: "[%(timestamp)s] [%(skill)s] %(message)s"
  metrics:
    - tests_generated
    - coverage_achieved
    - frameworks_used
---

# C++ Testing Skill

## Overview

Production-grade testing expertise for C++ applications. Master unit testing, mocking, TDD, and modern testing workflows.

---

## Testing Frameworks

### Google Test (gtest)

The most widely used C++ testing framework.

```cpp
#include <gtest/gtest.h>

// Basic test
TEST(CalculatorTest, Addition) {
    Calculator calc;
    EXPECT_EQ(calc.add(2, 3), 5);
    EXPECT_EQ(calc.add(-1, 1), 0);
}

// Test fixture
class StackTest : public ::testing::Test {
protected:
    void SetUp() override {
        stack.push(1);
        stack.push(2);
    }

    void TearDown() override {
        // Cleanup if needed
    }

    Stack<int> stack;
};

TEST_F(StackTest, PopReturnsTop) {
    EXPECT_EQ(stack.pop(), 2);
    EXPECT_EQ(stack.size(), 1);
}

// Parameterized test
class PrimeTest : public ::testing::TestWithParam<int> {};

TEST_P(PrimeTest, IsPrime) {
    EXPECT_TRUE(isPrime(GetParam()));
}

INSTANTIATE_TEST_SUITE_P(
    Primes,
    PrimeTest,
    ::testing::Values(2, 3, 5, 7, 11, 13)
);

// Death test
TEST(SecurityTest, NullPointerDeath) {
    EXPECT_DEATH(dereference(nullptr), ".*");
}
```

### Catch2

Modern, header-only testing framework.

```cpp
#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>

TEST_CASE("Vector operations", "[vector]") {
    std::vector<int> v;

    SECTION("pushing increases size") {
        v.push_back(1);
        REQUIRE(v.size() == 1);
    }

    SECTION("popping decreases size") {
        v.push_back(1);
        v.pop_back();
        REQUIRE(v.empty());
    }
}

// BDD-style
SCENARIO("Bank account operations", "[account]") {
    GIVEN("An account with $100") {
        Account account(100);

        WHEN("$50 is withdrawn") {
            account.withdraw(50);

            THEN("balance is $50") {
                REQUIRE(account.balance() == 50);
            }
        }
    }
}

// Matchers
TEST_CASE("String matchers") {
    REQUIRE_THAT("Hello World", Catch::Contains("World"));
    REQUIRE_THAT("Hello", Catch::StartsWith("Hel"));
}
```

---

## Google Mock (gmock)

### Creating Mocks

```cpp
#include <gmock/gmock.h>

// Interface to mock
class Database {
public:
    virtual ~Database() = default;
    virtual bool connect(const std::string& url) = 0;
    virtual std::string query(const std::string& sql) = 0;
    virtual void disconnect() = 0;
};

// Mock class
class MockDatabase : public Database {
public:
    MOCK_METHOD(bool, connect, (const std::string& url), (override));
    MOCK_METHOD(std::string, query, (const std::string& sql), (override));
    MOCK_METHOD(void, disconnect, (), (override));
};

// Using mocks
TEST(UserServiceTest, FetchesUserFromDatabase) {
    MockDatabase db;
    UserService service(&db);

    EXPECT_CALL(db, connect("db://localhost"))
        .WillOnce(Return(true));

    EXPECT_CALL(db, query("SELECT * FROM users WHERE id = 1"))
        .WillOnce(Return(R"({"name": "John"})"));

    EXPECT_CALL(db, disconnect());

    auto user = service.getUser(1);
    EXPECT_EQ(user.name, "John");
}
```

### Advanced Mocking

```cpp
// Matchers
EXPECT_CALL(mock, method(
    AllOf(Gt(0), Lt(100)),   // Range check
    HasSubstr("test"),        // String contains
    _                         // Any value
));

// Actions
EXPECT_CALL(mock, method(_))
    .WillOnce(Return(42))
    .WillOnce(Throw(std::runtime_error("error")))
    .WillRepeatedly(ReturnArg<0>());

// Sequences
Sequence s;
EXPECT_CALL(mock, first()).InSequence(s);
EXPECT_CALL(mock, second()).InSequence(s);

// Cardinality
EXPECT_CALL(mock, method())
    .Times(AtLeast(1))
    .Times(AtMost(5))
    .Times(Between(2, 4));
```

---

## Test-Driven Development (TDD)

### Red-Green-Refactor Cycle

```
┌─────────────────────────────────────────────────────────────┐
│                    TDD WORKFLOW                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│     ┌───────┐     ┌───────┐     ┌──────────┐              │
│     │  RED  │────▶│ GREEN │────▶│ REFACTOR │              │
│     └───────┘     └───────┘     └──────────┘              │
│         │                             │                    │
│         │         ┌───────────────────┘                    │
│         │         │                                        │
│         ▼         ▼                                        │
│     Write failing test ─▶ Make it pass ─▶ Clean up code   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### TDD Example

```cpp
// Step 1: RED - Write failing test
TEST(StringUtilsTest, ReverseString) {
    EXPECT_EQ(reverse("hello"), "olleh");  // Fails - function doesn't exist
}

// Step 2: GREEN - Minimal implementation
std::string reverse(const std::string& s) {
    std::string result = s;
    std::reverse(result.begin(), result.end());
    return result;
}

// Step 3: REFACTOR - Improve if needed
// Add string_view support, constexpr, etc.
```

---

## Fuzzing with libFuzzer

```cpp
// fuzz_target.cpp
#include <cstdint>
#include <cstddef>

extern "C" int LLVMFuzzerTestOneInput(const uint8_t* data, size_t size) {
    if (size < 4) return 0;

    std::string input(reinterpret_cast<const char*>(data), size);

    // Call function under test
    try {
        parseJson(input);  // May crash on invalid input
    } catch (...) {
        // Expected for invalid inputs
    }

    return 0;
}
```

Build and run:
```bash
clang++ -fsanitize=fuzzer,address -g fuzz_target.cpp -o fuzzer
./fuzzer corpus/ -max_len=1024 -jobs=4
```

---

## Benchmark Testing

```cpp
#include <benchmark/benchmark.h>

static void BM_VectorPushBack(benchmark::State& state) {
    for (auto _ : state) {
        std::vector<int> v;
        for (int i = 0; i < state.range(0); ++i) {
            v.push_back(i);
        }
        benchmark::DoNotOptimize(v);
    }
}
BENCHMARK(BM_VectorPushBack)->Range(8, 8<<10);

static void BM_VectorReserve(benchmark::State& state) {
    for (auto _ : state) {
        std::vector<int> v;
        v.reserve(state.range(0));
        for (int i = 0; i < state.range(0); ++i) {
            v.push_back(i);
        }
        benchmark::DoNotOptimize(v);
    }
}
BENCHMARK(BM_VectorReserve)->Range(8, 8<<10);

BENCHMARK_MAIN();
```

---

## Code Coverage

### Setup with CMake

```cmake
option(ENABLE_COVERAGE "Enable coverage reporting" OFF)

if(ENABLE_COVERAGE)
    add_compile_options(--coverage -fprofile-arcs -ftest-coverage)
    add_link_options(--coverage)
endif()
```

### Generate Report

```bash
# Build with coverage
cmake -B build -DENABLE_COVERAGE=ON
cmake --build build
cd build && ctest

# Generate report
lcov --capture --directory . --output-file coverage.info
lcov --remove coverage.info '/usr/*' --output-file coverage.info
genhtml coverage.info --output-directory coverage_report
```

---

## CMake Test Configuration

```cmake
cmake_minimum_required(VERSION 3.14)
project(MyProject)

# Enable testing
enable_testing()

# Fetch Google Test
include(FetchContent)
FetchContent_Declare(
    googletest
    GIT_REPOSITORY https://github.com/google/googletest.git
    GIT_TAG v1.14.0
)
FetchContent_MakeAvailable(googletest)

# Add test executable
add_executable(tests
    test_main.cpp
    test_calculator.cpp
    test_parser.cpp
)

target_link_libraries(tests
    PRIVATE
        GTest::gtest
        GTest::gmock
        GTest::gtest_main
        mylib
)

# Register tests with CTest
include(GoogleTest)
gtest_discover_tests(tests)
```

---

## CI Integration

### GitHub Actions

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Configure
        run: cmake -B build -DENABLE_COVERAGE=ON

      - name: Build
        run: cmake --build build

      - name: Test
        run: ctest --test-dir build --output-on-failure

      - name: Coverage
        run: |
          lcov --capture --directory build --output-file coverage.info
          bash <(curl -s https://codecov.io/bash)
```

---

## Troubleshooting Decision Tree

```
Test Failure
├── Compilation Error?
│   ├── Yes → Check includes, link libraries
│   └── No ↓
├── Assertion Failed?
│   ├── Yes → Debug actual vs expected values
│   └── No ↓
├── Segmentation Fault?
│   ├── Yes → Run with ASan, check pointers
│   └── No ↓
├── Timeout?
│   ├── Yes → Check infinite loops, deadlocks
│   └── No ↓
└── Flaky Test?
    ├── Yes → Check race conditions, random seeds
    └── No → Check test isolation
```

---

## Quick Reference

| Framework | Header | Main Macro | Assertion |
|-----------|--------|------------|-----------|
| GTest | `<gtest/gtest.h>` | `TEST()` | `EXPECT_*`, `ASSERT_*` |
| Catch2 | `<catch2/catch.hpp>` | `TEST_CASE()` | `REQUIRE()`, `CHECK()` |
| doctest | `<doctest/doctest.h>` | `TEST_CASE()` | `CHECK()`, `REQUIRE()` |

---

## Unit Test Template

```cpp
#include <gtest/gtest.h>
#include "testing_skill.hpp"

class TestingSkillTest : public ::testing::Test {
protected:
    void SetUp() override {
        // Initialize test fixtures
    }
};

TEST_F(TestingSkillTest, GeneratesValidTests) {
    // Arrange
    std::string code = "int add(int a, int b) { return a + b; }";

    // Act
    auto tests = generateTests(code);

    // Assert
    EXPECT_FALSE(tests.empty());
    EXPECT_THAT(tests, HasSubstr("EXPECT_EQ"));
}

TEST_F(TestingSkillTest, HandlesEmptyInput) {
    EXPECT_THROW(generateTests(""), std::invalid_argument);
}
```

---

*C++ Plugin v3.0.0 - Production-Grade Testing Skill*
