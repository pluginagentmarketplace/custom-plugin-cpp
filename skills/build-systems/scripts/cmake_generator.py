#!/usr/bin/env python3
"""CMake Project Generator."""

import json
from pathlib import Path


CMAKE_TEMPLATE = '''cmake_minimum_required(VERSION {cmake_version})
project({project_name} VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD {cxx_standard})
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Sources
file(GLOB_RECURSE SOURCES "src/*.cpp")
file(GLOB_RECURSE HEADERS "include/*.hpp")

# Target
add_{target_type}({project_name} ${{SOURCES}})
target_include_directories({project_name} PUBLIC include)

# Compiler warnings
target_compile_options({project_name} PRIVATE
    $<$<CXX_COMPILER_ID:GNU>:-Wall -Wextra -Wpedantic>
    $<$<CXX_COMPILER_ID:Clang>:-Wall -Wextra>
    $<$<CXX_COMPILER_ID:MSVC>:/W4>
)
'''


def generate_cmake(config: dict) -> str:
    """Generate CMakeLists.txt content."""
    return CMAKE_TEMPLATE.format(
        cmake_version=config.get("cmake_version", "3.20"),
        project_name=config.get("project_name", "MyProject"),
        cxx_standard=config.get("cxx_standard", 20),
        target_type="executable" if config.get("type") == "executable" else "library"
    )


def analyze_project(path: str) -> dict:
    """Analyze existing C++ project structure."""
    project = Path(path)

    has_cmake = (project / "CMakeLists.txt").exists()
    has_src = (project / "src").exists()
    has_include = (project / "include").exists()

    cpp_files = list(project.rglob("*.cpp"))
    hpp_files = list(project.rglob("*.hpp")) + list(project.rglob("*.h"))

    return {
        "has_cmake": has_cmake,
        "has_src_dir": has_src,
        "has_include_dir": has_include,
        "cpp_file_count": len(cpp_files),
        "header_file_count": len(hpp_files),
        "needs_cmake": not has_cmake and len(cpp_files) > 0
    }


def main():
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    print(json.dumps(analyze_project(path), indent=2))


if __name__ == "__main__":
    main()
