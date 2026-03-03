<p align="center">
  <img src="vscode-oduduwa/icon.png" alt="OduduwaLang Logo" width="100">
  <h1 align="center">OduduwaLang</h1>
</p>

A powerful, open-source programming language that allows you to write real software natively in Yoruba. Oduduwa stands as a bridge between profound cultural heritage and modern software engineering. 

It compiles directly to Python, meaning it has the full power of the Python ecosystem while maintaining Yoruba syntax and grammar.

---

## 🚀 Getting Started (How to Install)

To use OduduwaLang on any computer, follow these simple steps:

### 1. Install Python
OduduwaLang requires Python to run. If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/).

### 2. Install OduduwaLang
Open your terminal (Command Prompt, PowerShell, or macOS Terminal) and type the following command to download OduduwaLang from the global PyPI registry:

```bash
pip install oduduwalang
```

*(If you are on Mac/Linux, you may need to use `pip3 install oduduwalang` instead).*

### 3. Install the VS Code Extension
To get beautiful syntax highlighting and the official Ife Bronze Head icon for your `.odu` files:
1. Open Visual Studio Code.
2. Go to the **Extensions** tab (or press `Ctrl+Shift+X`).
3. Search for **OduduwaLang**.
4. Click **Install**.

---

## 💻 Writing Your First Code

Once installed, create a new file named `hello.odu` and open it in VS Code.

Type the following Yoruba code to print a message to the screen:

```oduduwa
tejade("E kaaro Aye! (Hello World)")
```

### Running the Code
Open your terminal inside the folder where you saved `hello.odu` and run:

```bash
python -m oduduwa.cli sise hello.odu
```

*(Or, if your Python Scripts folder is added to your Windows PATH, you can simply type: `oduduwa run hello.odu`)*

---

## ⚡ The Interactive REPL
Want to just test some Yoruba code quickly without creating a file? You can open the Oduduwa Interactive Shell!

Just open your terminal and type:
```bash
python -m oduduwa.cli
```

You will see the interactive prompt where you can type code line-by-line:
```
=======================================
 OduduwaLang REPL v0.1.0
 Tẹ 'iranlowo' (tabi 'help') fun itọsọna.
 Tẹ 'jade()' lati kuro (Type 'jade()' to exit)
=======================================
odu> tejade("Bawo ni?")
Bawo ni?
```

---

## 📚 Language Features

OduduwaLang supports variables, conditionals, loops, nested dictionaries, lists, object-oriented programming, and standard library modules!

### Variables & Conditionals
```oduduwa
odun = 20
ti odun > 18:
    tejade("O to lati se idibo!")
bibeeko:
    tejade("O ti kere ju.")
```

### OOP (Classes) & Functions
```oduduwa
egbe Aja:
    ise __ibere__(ara, oruko):
        ara.oruko = oruko
        
    ise gbo(ara):
        tejade(ara.oruko, "wipe: Gboyen gbo!")

aja_mi = Aja("Okin")
aja_mi.gbo()
```

### Error Handling
```oduduwa
gbiyanju:
    abajade = 10 / 0
mu_asise:
    tejade("A ti mu asise! O ko le pin pelu odo.")
ni_ipari:
    tejade("Eyi ma sise ni gbogbo igba.")
```

### Imports & Standard Library
```oduduwa
mu_wole onka
mu_wole akoko

tejade("100 l'ede Yoruba ni:", onka.yipada(100))
tejade("Asiko yii ni:", akoko.asiko_kika())
```

---

## 🛠️ CLI Tooling
OduduwaLang comes with built-in development tools to keep your code clean:
* **Format**: `oduduwa se_eto app.odu` (Perfectly indents your code)
* **Lint**: `oduduwa yewo app.odu` (Scans for syntax errors)
* **Run**: `oduduwa sise app.odu`
* **REPL**: `oduduwa soro`

## 📄 Documentation
For the full technical details on how to write OduduwaLang, view our guides:
- [Grammar Specification](docs/grammar.md)
- [How it Works (Architecture Overview)](docs/architecture.md)
- [Native Compilation Strategy](docs/native_compilation_research.md)

## 🤝 Contributing
This is an open-source project. We welcome Yoruba linguists and software engineers to join us in building this legacy. 
Feel free to open an issue or submit a Pull Request on our [GitHub Repository](https://github.com/AdediranAdedamola/OduduwaLang).
