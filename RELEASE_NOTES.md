# OduduwaLang Release Notes

## 🚀 Version 0.2.2 (The Isiro & Automation Update)
**Release Date:** March 2026 (Mid-month Update)

This update expands the language's core capabilities, adding essential math functions, easier string formatting, and a new build system for standalone scripts.

### ➕ Standard Library: `isiro`
A new native module for mathematics simplifies calculations with Yoruba-named functions:
- `isiro.apapo()`: Calculate sums of lists/numbers.
- `isiro.iwon()`: Calculate averages.
- `isiro.gbere_square()`: Native square root.
- `isiro.agbara()`: Exponents/Powers.
- `isiro.to_bi_ju()` / `isiro.kere_ju()`: Find maximum and minimum values.

- Example: `tejade(f"Oruko mi ni {oruko}")`

### 📥 User Input (`gba_wole`)
Programs can now be interactive! Use `gba_wole()` to capture user input from the terminal:
- Example: `oruko = gba_wole("Kini oruko re? ")`

### 🔀 Enhanced Conditionals (`tabi`)
Support for multiple decision branches has been added with `tabi` (alias for `si_ti` or `elif`):
- Example logic: `ti ... tabi ... tabi ... bibeeko`

### 🏗️ Build Command: `kiko` (or `ko`)
Oduduwa scripts can now be bundled into single, standalone `.py` files that include their dependencies:
- Command: `oduduwa kiko app.odu -o standalone_app.py`
- This makes distribution much easier as users won't need the `oduduwalang` package installed to run your generated scripts!

### 🔧 Better Error Reporting
Expanded the Yoruba exception map to handle attributes, imports, and file system errors with clearer native guidance.

---


## 🎉 Version 0.1.0 / 0.1.1 (Initial Public Release)
**Release Date:** March 2026

We are incredibly proud to announce the official release of OduduwaLang, a powerful, Yoruba-first programming language built to fuse modern software engineering with rich cultural heritage.

### 🚀 Major Milestones
- **PyPI Publishing**: OduduwaLang is now officially available on the global Python Package Index. Anyone can install it via `pip install oduduwalang`.
- **VS Code Extension**: The official OduduwaLang extension is live on the Visual Studio Marketplace. It provides full syntax highlighting for `.odu` files and features the iconic Ifẹ Bronze Head logo.

### 💻 Language Core
OduduwaLang compiles directly to Python and safely brings native Yoruba grammar into software logic:
- **Keywords**: Native support for variable assignment, function definition (`ise`), and returns (`pada`).
- **Conditionals**: Full support for `ti` (if), `si_ti` (elif), and `bibeeko` (else).
- **Loops**: Implemented `fun` (for loops with `lati/de`) and `nigbati` (while loops).
- **Data Structures**: Native support for complex nested Dictionaries `{}` and Lists `[]`.

### 🛠️ Developer Tools & Ecosystem
- **Interactive REPL**: A native Yoruba interactive shell! Run `oduduwa` in the terminal to experiment with code. Includes customized `iranlowo` (help) and `pare` (clear screen) commands.
- **Yoruba Error Reporting**: Goodbye to confusing Python stack traces! Oduduwa intercepts errors (like Syntax errors or missing variables) and presents them natively in an `IPADE AṢIṢE` block with the exact line number to help learners debug faster.
- **Standard Library**: Introduced the first native module, `iro` (Math), mapping functions like `iro.gbongbo()` for square roots.

### 📖 Documentation
- Authored a comprehensive `README.md` for fast onboarding.
- Published `docs/grammar.md` as the official language specification.

---
*Ẹ se gan, ẹyin akanda eda! (Thank you, brilliant creators!)*
