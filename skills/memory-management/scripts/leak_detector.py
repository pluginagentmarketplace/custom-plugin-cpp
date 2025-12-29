#!/usr/bin/env python3
"""C++ Memory Leak Pattern Detector."""

import re
import json
from pathlib import Path


LEAK_PATTERNS = {
    "raw_new": {
        "pattern": r"\bnew\s+\w+",
        "risk": "high",
        "fix": "Use std::make_unique or std::make_shared"
    },
    "raw_delete": {
        "pattern": r"\bdelete\s+",
        "risk": "high",
        "fix": "Use smart pointers instead"
    },
    "malloc": {
        "pattern": r"\bmalloc\s*\(",
        "risk": "high",
        "fix": "Use C++ containers or smart pointers"
    },
    "free": {
        "pattern": r"\bfree\s*\(",
        "risk": "high",
        "fix": "Use C++ RAII patterns"
    },
    "missing_virtual_destructor": {
        "pattern": r"class\s+\w+\s*\{[^}]*public:[^}]*~\w+\(\)[^}]*\}",
        "risk": "medium",
        "fix": "Add virtual destructor for polymorphic base classes"
    }
}


def detect_leaks(code: str) -> dict:
    """Detect potential memory leak patterns."""
    issues = []

    for name, info in LEAK_PATTERNS.items():
        matches = re.findall(info["pattern"], code, re.MULTILINE)
        if matches:
            issues.append({
                "type": name,
                "count": len(matches),
                "risk": info["risk"],
                "fix": info["fix"]
            })

    # Positive patterns (smart pointer usage)
    smart_ptr_usage = len(re.findall(r"(unique_ptr|shared_ptr|make_unique|make_shared)", code))

    return {
        "issues": issues,
        "issue_count": len(issues),
        "smart_pointer_usage": smart_ptr_usage,
        "risk_level": "high" if any(i["risk"] == "high" for i in issues) else "low",
        "recommendation": "Consider using smart pointers" if issues else "Good memory practices"
    }


def main():
    import sys
    if len(sys.argv) > 1:
        code = Path(sys.argv[1]).read_text()
    else:
        code = sys.stdin.read()
    print(json.dumps(detect_leaks(code), indent=2))


if __name__ == "__main__":
    main()
