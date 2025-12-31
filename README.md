<div align="center">

<!-- Animated Typing Banner -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=2E9EF7&center=true&vCenter=true&multiline=true&repeat=true&width=600&height=100&lines=C%2B%2B+Programming+System;9+Agents+%7C+12+Skills;Claude+Code+Plugin" alt="C++ Programming System" />

<br/>

<!-- Badge Row 1: Status Badges -->
[![Version](https://img.shields.io/badge/Version-2.0.0-blue?style=for-the-badge)](https://github.com/pluginagentmarketplace/custom-plugin-cpp/releases)
[![License](https://img.shields.io/badge/License-Custom-yellow?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production-brightgreen?style=for-the-badge)](#)
[![SASMP](https://img.shields.io/badge/SASMP-v1.3.0-blueviolet?style=for-the-badge)](#)

<!-- Badge Row 2: Content Badges -->
[![Agents](https://img.shields.io/badge/Agents-9-orange?style=flat-square&logo=robot)](#-agents)
[![Skills](https://img.shields.io/badge/Skills-12-purple?style=flat-square&logo=lightning)](#-skills)
[![Commands](https://img.shields.io/badge/Commands-6-green?style=flat-square&logo=terminal)](#-commands)

<br/>

<!-- Quick CTA Row -->
[📦 **Install Now**](#-quick-start) · [🤖 **Explore Agents**](#-agents) · [📖 **Documentation**](#-documentation) · [⭐ **Star this repo**](https://github.com/pluginagentmarketplace/custom-plugin-cpp)

---

### What is this?

> **C++ Programming System** is a Claude Code plugin with **9 agents** and **12 skills** for C++ development. Learn AND Develop with expert AI agents - master fundamentals, OOP, STL, and modern C++ while building real projects.

</div>

---

## 📑 Table of Contents

<details>
<summary>Click to expand</summary>

- [Quick Start](#-quick-start)
- [Features](#-features)
- [Agents](#-agents)
- [Skills](#-skills)
- [Commands](#-commands)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)

</details>

---

## 🚀 Quick Start

### Prerequisites

- Claude Code CLI v2.0.27+
- Active Claude subscription

### Installation (Choose One)

<details open>
<summary><strong>Option 1: From Marketplace (Recommended)</strong></summary>

```bash
# Step 1️⃣ Add the marketplace
/plugin add marketplace pluginagentmarketplace/custom-plugin-cpp

# Step 2️⃣ Install the plugin
/plugin install custom-plugin-cpp@pluginagentmarketplace-cpp

# Step 3️⃣ Restart Claude Code
# Close and reopen your terminal/IDE
```

</details>

<details>
<summary><strong>Option 2: Local Installation</strong></summary>

```bash
# Clone the repository
git clone https://github.com/pluginagentmarketplace/custom-plugin-cpp.git
cd custom-plugin-cpp

# Load locally
/plugin load .

# Restart Claude Code
```

</details>

### ✅ Verify Installation

After restart, you should see these agents:

```
custom-plugin-cpp:01-modern-cpp-expert
custom-plugin-cpp:02-memory-specialist
custom-plugin-cpp:03-stl-master
custom-plugin-cpp:04-build-engineer
custom-plugin-cpp:05-performance-optimizer
custom-plugin-cpp:cpp-algorithms-agent
custom-plugin-cpp:cpp-debugger-agent
custom-plugin-cpp:cpp-fundamentals-agent
custom-plugin-cpp:cpp-oop-agent
```

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 **9 Agents** | Specialized AI agents for C++ tasks |
| 🛠️ **12 Skills** | Reusable capabilities with Golden Format |
| ⌨️ **6 Commands** | Quick slash commands |
| 🔄 **SASMP v1.3.0** | Full protocol compliance |
| 🎓 **Hybrid Mode** | Learn AND Develop with expert agents |

---

## 🤖 Agents

### 9 Specialized Agents

| # | Agent | Purpose |
|---|-------|---------|
| 1 | **01-modern-cpp-expert** | Modern C++ (11/14/17/20/23) features and best practices |
| 2 | **02-memory-specialist** | Memory management, smart pointers, RAII patterns |
| 3 | **03-stl-master** | STL containers, algorithms, iterators |
| 4 | **04-build-engineer** | CMake, build systems, project configuration |
| 5 | **05-performance-optimizer** | Performance tuning, profiling, optimization |
| 6 | **cpp-algorithms-agent** | Data structures and algorithm implementation |
| 7 | **cpp-debugger-agent** | Debugging techniques and error resolution |
| 8 | **cpp-fundamentals-agent** | C++ basics, syntax, control flow |
| 9 | **cpp-oop-agent** | Object-oriented programming patterns |

---

## 🛠️ Skills

### Available Skills

| Skill | Description | Invoke |
|-------|-------------|--------|
| `algorithms` | Algorithm design and implementation | `Skill("custom-plugin-cpp:algorithms")` |
| `build-systems` | CMake and build configuration | `Skill("custom-plugin-cpp:build-systems")` |
| `concurrency` | Multi-threading and parallel programming | `Skill("custom-plugin-cpp:concurrency")` |
| `cpp-basics` | C++ fundamentals and syntax | `Skill("custom-plugin-cpp:cpp-basics")` |
| `debugging` | Debugging techniques and tools | `Skill("custom-plugin-cpp:debugging")` |
| `memory-management` | Smart pointers and RAII | `Skill("custom-plugin-cpp:memory-management")` |
| `modern-cpp` | C++11/14/17/20/23 features | `Skill("custom-plugin-cpp:modern-cpp")` |
| `oop-patterns` | OOP design patterns | `Skill("custom-plugin-cpp:oop-patterns")` |
| `performance` | Optimization and profiling | `Skill("custom-plugin-cpp:performance")` |
| `stl` | Standard Template Library | `Skill("custom-plugin-cpp:stl")` |
| `templates` | Template metaprogramming | `Skill("custom-plugin-cpp:templates")` |
| `testing` | Unit testing and TDD | `Skill("custom-plugin-cpp:testing")` |

---

## ⌨️ Commands

| Command | Description |
|---------|-------------|
| `/cpp-debug` | Debug C++ code and resolve errors |
| `/cpp-learn` | Learn C++ topics with structured lessons |
| `/cpp-new` | Create new C++ project with templates |
| `/cpp-optimize` | Optimize C++ code for performance |
| `/cpp-practice` | Practice C++ with coding exercises |
| `/cpp-review` | Code review and best practices check |

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [CHANGELOG.md](CHANGELOG.md) | Version history |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute |
| [LICENSE](LICENSE) | License information |

---

## 📁 Project Structure

<details>
<summary>Click to expand</summary>

```
custom-plugin-cpp/
├── 📁 .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── 📁 agents/              # 9 agents
├── 📁 skills/              # 12 skills (Golden Format)
├── 📁 commands/            # 6 commands
├── 📁 hooks/
├── 📄 README.md
├── 📄 CHANGELOG.md
└── 📄 LICENSE
```

</details>

---

## 📅 Metadata

| Field | Value |
|-------|-------|
| **Version** | 2.0.0 |
| **Last Updated** | 2025-12-31 |
| **Status** | Production Ready |
| **SASMP** | v1.3.0 |
| **Agents** | 9 |
| **Skills** | 12 |
| **Commands** | 6 |

---

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md).

1. Fork the repository
2. Create your feature branch
3. Follow the Golden Format for new skills
4. Submit a pull request

---

## ⚠️ Security

> **Important:** This repository contains third-party code and dependencies.
>
> - ✅ Always review code before using in production
> - ✅ Check dependencies for known vulnerabilities
> - ✅ Follow security best practices
> - ✅ Report security issues privately via [Issues](../../issues)

---

## 📝 License

Copyright © 2025 **Dr. Umit Kacar** & **Muhsin Elcicek**

Custom License - See [LICENSE](LICENSE) for details.

---

## 👥 Contributors

<table>
<tr>
<td align="center">
<strong>Dr. Umit Kacar</strong><br/>
Senior AI Researcher & Engineer
</td>
<td align="center">
<strong>Muhsin Elcicek</strong><br/>
Senior Software Architect
</td>
</tr>
</table>

---

<div align="center">

**Made with ❤️ for the Claude Code Community**

[![GitHub](https://img.shields.io/badge/GitHub-pluginagentmarketplace-black?style=for-the-badge&logo=github)](https://github.com/pluginagentmarketplace)

</div>
