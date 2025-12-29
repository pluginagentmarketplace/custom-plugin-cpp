#!/usr/bin/env python3
"""C++ Performance Pattern Analyzer."""

import re
import json
from pathlib import Path


PERF_PATTERNS = {
    "virtual_call": {
        "pattern": r"\bvirtual\b",
        "impact": "medium",
        "note": "Virtual calls prevent inlining"
    },
    "heap_allocation": {
        "pattern": r"\bnew\s+\w+",
        "impact": "high",
        "note": "Heap allocations are expensive"
    },
    "exception_handling": {
        "pattern": r"\b(try|throw|catch)\b",
        "impact": "medium",
        "note": "Exceptions have runtime cost"
    },
    "string_copy": {
        "pattern": r"std::string\s+\w+\s*=",
        "impact": "medium",
        "note": "Consider string_view or references"
    },
    "shared_ptr": {
        "pattern": r"shared_ptr",
        "impact": "low",
        "note": "Atomic ref counting overhead"
    }
}

GOOD_PATTERNS = {
    "move_semantics": r"std::move\(",
    "reserve": r"\.reserve\(",
    "emplace": r"\.emplace",
    "constexpr": r"\bconstexpr\b",
    "inline": r"\binline\b",
    "noexcept": r"\bnoexcept\b"
}


def analyze_performance(code: str) -> dict:
    """Analyze code for performance patterns."""
    issues = []
    optimizations = []

    for name, info in PERF_PATTERNS.items():
        matches = len(re.findall(info["pattern"], code))
        if matches > 0:
            issues.append({
                "pattern": name,
                "count": matches,
                "impact": info["impact"],
                "note": info["note"]
            })

    for name, pattern in GOOD_PATTERNS.items():
        matches = len(re.findall(pattern, code))
        if matches > 0:
            optimizations.append({"pattern": name, "count": matches})

    return {
        "potential_issues": issues,
        "good_practices": optimizations,
        "performance_score": max(0, 100 - len(issues) * 10 + len(optimizations) * 5),
        "recommendation": "Profile before optimizing" if issues else "Code looks performant"
    }


def main():
    import sys
    if len(sys.argv) > 1:
        code = Path(sys.argv[1]).read_text()
    else:
        code = sys.stdin.read()
    print(json.dumps(analyze_performance(code), indent=2))


if __name__ == "__main__":
    main()
