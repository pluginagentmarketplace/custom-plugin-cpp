# C++ Plugin Architecture

## Version: 3.0.0 | SASMP v1.3.0 | EQHM Compliant

---

## Dependency Graph

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         C++ PLUGIN ARCHITECTURE                             │
│                            Version 3.0.0                                    │
└─────────────────────────────────────────────────────────────────────────────┘

                              ┌─────────────┐
                              │   COMMANDS  │
                              └──────┬──────┘
                                     │
        ┌────────────────────────────┼────────────────────────────┐
        │                            │                            │
        ▼                            ▼                            ▼
┌───────────────┐          ┌───────────────┐          ┌───────────────┐
│   cpp-new     │          │   cpp-learn   │          │  cpp-review   │
│   cpp-debug   │          │  cpp-practice │          │  cpp-optimize │
└───────┬───────┘          └───────┬───────┘          └───────┬───────┘
        │                          │                          │
        │         ┌────────────────┼────────────────┐         │
        │         │                │                │         │
        ▼         ▼                ▼                ▼         ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                                 AGENTS                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐          │
│  │ modern-cpp-expert│  │ memory-specialist│  │    stl-master    │          │
│  │     (01)         │  │     (02)         │  │     (03)         │          │
│  └────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘          │
│           │                     │                     │                     │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐          │
│  │  build-engineer  │  │performance-optim.│  │cpp-fundamentals  │          │
│  │     (04)         │  │     (05)         │  │    -agent        │          │
│  └────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘          │
│           │                     │                     │                     │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐          │
│  │   cpp-oop-agent  │  │cpp-algorithms    │  │ cpp-debugger     │          │
│  │                  │  │    -agent        │  │    -agent        │          │
│  └────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘          │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                                 SKILLS                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐           │
│  │  cpp-basics │ │ oop-patterns│ │memory-mgmt  │ │    stl      │           │
│  └──────┬──────┘ └──────┬──────┘ └──────┬──────┘ └──────┬──────┘           │
│         │               │               │               │                   │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐           │
│  │ algorithms  │ │ modern-cpp  │ │build-systems│ │ performance │           │
│  └──────┬──────┘ └──────┬──────┘ └──────┬──────┘ └──────┬──────┘           │
│         │               │               │               │                   │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐           │
│  │  debugging  │ │ concurrency │ │  templates  │ │   testing   │           │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘           │
│                                                                              │
│                           + reference guides                                │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Agent-Skill Bond Matrix

| Agent | Primary Skills | Fallback Agent |
|-------|----------------|----------------|
| `modern-cpp-expert` | modern-cpp, templates, concurrency | - |
| `memory-specialist` | memory-management | modern-cpp-expert |
| `stl-master` | stl | modern-cpp-expert |
| `build-engineer` | build-systems | modern-cpp-expert |
| `performance-optimizer` | performance | modern-cpp-expert |
| `cpp-fundamentals-agent` | cpp-basics | modern-cpp-expert |
| `cpp-oop-agent` | oop-patterns | modern-cpp-expert |
| `cpp-algorithms-agent` | algorithms | modern-cpp-expert |
| `cpp-debugger-agent` | debugging, testing | modern-cpp-expert |

---

## Command Routing

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           COMMAND ROUTING                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  /cpp-new ────────────────────────────────────────▶ build-engineer          │
│                                                                              │
│  /cpp-learn ──┬─ fundamentals ────────────────────▶ cpp-fundamentals-agent  │
│               ├─ oop ─────────────────────────────▶ cpp-oop-agent           │
│               ├─ memory ──────────────────────────▶ memory-specialist       │
│               ├─ stl ─────────────────────────────▶ stl-master              │
│               ├─ algorithms ──────────────────────▶ cpp-algorithms-agent    │
│               └─ modern ──────────────────────────▶ modern-cpp-expert       │
│                                                                              │
│  /cpp-debug ──────────────────────────────────────▶ cpp-debugger-agent      │
│                                                                              │
│  /cpp-optimize ───────────────────────────────────▶ performance-optimizer   │
│                                                                              │
│  /cpp-practice ─┬─ easy ──────────────────────────▶ cpp-fundamentals-agent  │
│                 ├─ medium ────────────────────────▶ cpp-oop-agent           │
│                 └─ hard/interview ────────────────▶ cpp-algorithms-agent    │
│                                                                              │
│  /cpp-review ──┬─ default ────────────────────────▶ modern-cpp-expert       │
│                ├─ performance ────────────────────▶ performance-optimizer   │
│                └─ memory ─────────────────────────▶ memory-specialist       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Component Statistics

| Category | Count | Version |
|----------|-------|---------|
| Agents | 9 | 3.0.0 |
| Skills | 13 | 3.0.0 |
| Commands | 6 | 3.0.0 |
| Reference Guides | 5 | - |
| Total Components | 33 | - |

---

## Skill Categories

| Category | Skills | Count |
|----------|--------|-------|
| Fundamentals | cpp-basics | 1 |
| Design Patterns | oop-patterns | 1 |
| Core | memory-management | 1 |
| Standard Library | stl | 1 |
| Algorithms | algorithms | 1 |
| Modern Features | modern-cpp | 1 |
| Tooling | build-systems, debugging | 2 |
| Optimization | performance | 1 |
| Advanced | concurrency, templates | 2 |
| Quality Assurance | testing | 1 |

---

## Error Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            ERROR HANDLING FLOW                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Error Occurs                                                                │
│       │                                                                      │
│       ▼                                                                      │
│  ┌─────────────┐                                                            │
│  │ Log Error   │──────────────────────────────────▶ Observability           │
│  └──────┬──────┘                                                            │
│         │                                                                    │
│         ▼                                                                    │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐                   │
│  │ Is Transient│─Yes─▶│   Retry    │─Fail─▶│  Fallback  │                   │
│  └──────┬──────┘     │  (3x exp)  │      │   Agent    │                    │
│         │No          └─────────────┘      └─────────────┘                   │
│         ▼                                                                    │
│  ┌─────────────┐                                                            │
│  │ Escalate to │                                                            │
│  │    User     │                                                            │
│  └─────────────┘                                                            │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Integrity Verification

### Checksum Validation

All component files should be validated at load time:

```bash
# Generate checksums
find . -name "*.md" -type f | xargs sha256sum > checksums.txt

# Verify integrity
sha256sum -c checksums.txt
```

### Schema Validation

All YAML frontmatter must conform to SASMP v1.3.0 schema:

| Field | Required | Type |
|-------|----------|------|
| name | Yes | string |
| version | Yes | string (semver) |
| description | Yes | string |
| sasmp_version | Yes | string |

### Bond Validation

Every skill must have a valid `bonded_agent` reference:

```
✓ cpp-basics → cpp-fundamentals-agent
✓ oop-patterns → cpp-oop-agent
✓ memory-management → memory-specialist
✓ stl → stl-master
✓ algorithms → cpp-algorithms-agent
✓ modern-cpp → modern-cpp-expert
✓ build-systems → build-engineer
✓ performance → performance-optimizer
✓ debugging → cpp-debugger-agent
✓ concurrency → modern-cpp-expert
✓ templates → modern-cpp-expert
✓ testing → cpp-debugger-agent
```

---

## SASMP v1.3.0 Compliance Checklist

- [x] All agents have version 3.0.0
- [x] All skills have version 3.0.0
- [x] All commands have version 3.0.0
- [x] Input/output schemas defined
- [x] Error handling with retry logic
- [x] Exponential backoff with jitter
- [x] Fallback agent configuration
- [x] Observability hooks
- [x] Activation triggers defined
- [x] Exit codes documented

---

*Architecture Document - C++ Plugin v3.0.0*
