#!/usr/bin/env python3
"""C++ Standard Version Detector."""

import re
import json
from pathlib import Path


CPP_FEATURES = {
    11: ["nullptr", "auto", "decltype", "constexpr", "override", "final",
         "unique_ptr", "shared_ptr", "lambda", "move\\(", "forward\\("],
    14: ["make_unique", "generic lambda", "'[0-9]+'s", "'[0-9]+'ms"],
    17: ["optional", "variant", "any", "string_view", "filesystem",
         "if constexpr", "structured binding", "\\[\\[nodiscard\\]\\]"],
    20: ["concept", "requires", "co_await", "co_yield", "co_return",
         "span", "jthread", "\\|", "ranges::", "<=>" ],
    23: ["expected", "mdspan", "print\\(", "this auto"]
}


def detect_cpp_standard(code: str) -> dict:
    """Detect minimum C++ standard required by code."""
    detected_features = {}
    min_standard = 98

    for standard, features in CPP_FEATURES.items():
        for feature in features:
            if re.search(feature, code, re.IGNORECASE):
                if standard not in detected_features:
                    detected_features[standard] = []
                detected_features[standard].append(feature)
                min_standard = max(min_standard, standard)

    return {
        "minimum_standard": f"C++{min_standard}",
        "detected_features": detected_features,
        "recommendation": f"-std=c++{min_standard}" if min_standard > 98 else "-std=c++11",
        "modern": min_standard >= 11
    }


def main():
    import sys
    if len(sys.argv) > 1:
        code = Path(sys.argv[1]).read_text()
    else:
        code = sys.stdin.read()
    print(json.dumps(detect_cpp_standard(code), indent=2))


if __name__ == "__main__":
    main()
