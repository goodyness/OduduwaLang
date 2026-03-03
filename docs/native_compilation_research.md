# OduduwaLang Native Compilation Research (Phase 10)

Lọwọlọwọ (Currently), OduduwaLang is a **Transpiled Language**. It reads `.odu` files, processes them into an Abstract Syntax Tree (AST), and strictly transpiles the AST into Python logic that is executed by the CPython interpreter. 

While this creates massive flexibility and easy access to Python's incredible global ecosystem, it introduces dependencies:
1. Users **must** have Python installed locally to run Oduduwa.
2. Oduduwa executes at Python speeds (which has Global Interpreter Lock constraints).

To make Oduduwa a truly independent, world-class programming language that can be distributed as a single `.exe` (Windows) or binary (Mac/Linux), we must detach from Python.

## Pathway to Native Compilation

### 1. The LLVM Backend Approach
LLVM is the compiler framework powering modern blazing-fast languages like Rust, Swift, and Julia. 
Instead of mapping our AST into a Python string:
* We pass Oduduwa's AST through `llvmlite` (or a native C compiler frontend).
* The Oduduwa AST emits LLVM Intermediate Representation (IR).
* LLVM optimally compiles that IR into true machine code (binary) for the target CPU. 
* Result: A `hello.odu` file compiles directly to a `hello.exe` native desktop app.

### 2. The C-Transpiler Approach
Similar to Nim or V, OduduwaLang can transpile to highly optimized `C` code instead of `Python` code.
1. `oduduwa kiko app.odu` builds an `app.c` file.
2. Oduduwa secretly triggers `gcc` or `clang` in the background.
3. The C code is instantly compiled into a binary executable.

## Next Steps for v2.0
1. Create a `transpiler_c.py` variant.
2. Remap the Oduduwa Standard Library (`iro`, `akoko`) to C-native libraries (`<math.h>`, `<time.h>`).
3. Ditch the Python globals dictionary and implement static memory typing.

This is the ultimate roadmap for OduduwaLang's evolution!
