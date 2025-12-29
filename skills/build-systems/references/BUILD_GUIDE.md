# Build Systems Guide

## Modern CMake

```cmake
cmake_minimum_required(VERSION 3.20)
project(MyProject VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Library
add_library(mylib src/lib.cpp)
target_include_directories(mylib PUBLIC include)

# Executable
add_executable(myapp src/main.cpp)
target_link_libraries(myapp PRIVATE mylib)

# Tests
enable_testing()
add_subdirectory(tests)
```

## Package Managers

### Conan
```bash
# conanfile.txt
[requires]
fmt/10.0.0
spdlog/1.11.0

[generators]
CMakeDeps
CMakeToolchain

# Build
conan install . --build=missing
cmake -B build -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake
cmake --build build
```

### vcpkg
```bash
# Install packages
vcpkg install fmt spdlog

# CMake integration
cmake -B build -DCMAKE_TOOLCHAIN_FILE=$VCPKG_ROOT/scripts/buildsystems/vcpkg.cmake
```

## Build Commands

```bash
# Configure
cmake -B build -DCMAKE_BUILD_TYPE=Release

# Build
cmake --build build -j$(nproc)

# Install
cmake --install build --prefix /usr/local

# With Ninja
cmake -B build -G Ninja
ninja -C build
```

## Cross-Compilation

```cmake
# toolchain-arm.cmake
set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR arm)
set(CMAKE_C_COMPILER arm-linux-gnueabihf-gcc)
set(CMAKE_CXX_COMPILER arm-linux-gnueabihf-g++)
```

```bash
cmake -B build -DCMAKE_TOOLCHAIN_FILE=toolchain-arm.cmake
```

---

*C++ Plugin - Build Systems Skill*
