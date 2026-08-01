# Translators: CutePy to RISC-V Compiler

![Language](https://img.shields.io/badge/Language-Python-blue.svg)
![Target](https://img.shields.io/badge/Target-RISC--V_Assembly-red.svg)

## Project Overview

This repository contains the complete implementation of a compiler for **CutePy (cpy)**, an educational programming language featuring Python-like syntax. 

Unlike many introductory parsing projects that rely on tools like Lex, Yacc, or ANTLR, this compiler was built entirely from scratch in Python. It handles the full translation pipeline: reading raw source code, validating grammar, managing memory and scope, and ultimately generating low-level machine instructions for the RISC-V processor architecture.

## The CutePy Language

CutePy was designed to pose specific architectural challenges for compiler construction while stripping away superficial complexities. 

*   **Syntax & Control Flow:** Heavily inspired by Python, relying on strict block structures (denoted by custom bracket sequences like `#{` and `#}`) to manage `if`, `elif`, `else` statements and `while` loops.
*   **Data Types:** Operates exclusively on 16-bit integers (ranging from -32767 to 32767). Complex data types (floats, strings, arrays) were omitted to focus the engineering effort entirely on the compilation pipeline.
*   **Functions & Scope:** The language supports nested local functions, allowing functions to be declared inside one another to an arbitrary depth. It enforces strict Pascal-like scoping rules, supports parameter passing by value, and allows for recursive function calls.

## Compiler Architecture

The project was developed in four distinct, progressive phases, mirroring professional compiler design:

### 1. Lexical and Syntactical Analysis
*   **Lexer:** Reads the raw `.cpy` file character by character, utilizing a deterministic finite automaton (DFA) state machine to group characters into meaningful tokens (keywords, identifiers, operators) and catching illegal characters or out-of-bounds integers.
*   **Parser:** A custom Recursive Descent Parser built strictly according to the CutePy Context-Free Grammar (CFG). It processes the token stream to validate the structural correctness of the program.

### 2. Intermediate Code Generation
*   As the syntax is validated, the parser simultaneously generates a machine-independent intermediate representation of the code. This bridges the gap between high-level language constructs and low-level machine operations.

### 3. Semantic Analysis and Symbol Table
*   **Symbol Table:** A dynamic, stack-based data structure used to track variable declarations, function signatures, and memory offsets.
*   **Scope Management:** Handles the complexities of nested functions, ensuring that variables declared in outer scopes are accessible to inner scopes, and that localized variables correctly shadow global ones.

### 4. Final Code Generation
*   The intermediate code and symbol table data are translated into **RISC-V Assembly**. This phase handles low-level memory management, mapping variables to the RISC-V call stack, managing the program counter, and handling jumps/branches for loops and conditional statements.

## What was Learned

*   **Automata Theory in Practice:** Translating theoretical state machines into a functional lexical analyzer.
*   **Grammar Design:** How to read, interpret, and implement a Context-Free Grammar using recursive descent parsing to avoid ambiguity.
*   **Memory Management:** A deep understanding of how the call stack works under the hood, particularly how activation records are pushed and popped during recursive and nested function calls.
*   **Hardware-Level Translation:** Bridging the massive abstraction gap between a high-level `while` loop and low-level RISC-V branching instructions and register allocations.
*   **Software Engineering:** Structuring a complex, multi-phase software project where the output of one distinct component directly feeds the strict input requirements of the next.

## How to Run

```bash
# Clone the repository
git clone [https://github.com/YourUsername/Translators.git](https://github.com/YourUsername/Translators.git)

# Navigate to the directory
cd Translators

# Run the compiler on a CutePy source file
python translator.py test.cpy
