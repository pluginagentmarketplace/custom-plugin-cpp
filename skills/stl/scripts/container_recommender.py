#!/usr/bin/env python3
"""STL Container Recommender."""

import json


CONTAINERS = {
    "vector": {
        "access": "O(1)",
        "insert_end": "O(1) amortized",
        "insert_mid": "O(n)",
        "search": "O(n)",
        "best_for": ["random access", "cache friendly", "default choice"]
    },
    "deque": {
        "access": "O(1)",
        "insert_end": "O(1)",
        "insert_front": "O(1)",
        "best_for": ["double-ended operations", "queue implementation"]
    },
    "list": {
        "access": "O(n)",
        "insert": "O(1)",
        "best_for": ["frequent insertions", "splice operations"]
    },
    "map": {
        "access": "O(log n)",
        "insert": "O(log n)",
        "ordered": True,
        "best_for": ["ordered key-value", "range queries"]
    },
    "unordered_map": {
        "access": "O(1) average",
        "insert": "O(1) average",
        "ordered": False,
        "best_for": ["fast lookup", "hash-based access"]
    },
    "set": {
        "access": "O(log n)",
        "insert": "O(log n)",
        "best_for": ["unique ordered elements", "range queries"]
    }
}


def recommend_container(requirements: dict) -> dict:
    """Recommend best STL container based on requirements."""
    scores = {}

    for name, props in CONTAINERS.items():
        score = 0
        if requirements.get("random_access") and props.get("access") == "O(1)":
            score += 2
        if requirements.get("fast_lookup") and "O(1)" in props.get("access", ""):
            score += 3
        if requirements.get("ordered") and props.get("ordered"):
            score += 2
        if requirements.get("frequent_insert") and "O(1)" in props.get("insert", ""):
            score += 2
        scores[name] = score

    best = max(scores, key=scores.get)
    return {
        "recommendation": best,
        "properties": CONTAINERS[best],
        "all_scores": scores
    }


def main():
    # Example usage
    requirements = {
        "random_access": True,
        "fast_lookup": False,
        "ordered": False,
        "frequent_insert": True
    }
    print(json.dumps(recommend_container(requirements), indent=2))


if __name__ == "__main__":
    main()
