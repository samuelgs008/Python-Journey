# Python-Journey 🐍

A Python journey made with [Claude](https://claude.com/claude-code) to study Python from scratch. The exercises are inspired by beecrowd: each one has a problem statement, input/output descriptions and sample cases. They don't follow beecrowd 100%, though: some of them, especially in the later levels, are bigger projects. The path goes from the basics all the way to automation and artificial intelligence applied to real processes, one exercise at a time.

Claude creates the exercises and acts only as a **tutor**: it never writes the solutions or gives the answers. All the code in the `solution.py` files is written by me. When I get stuck, Claude gives hints, explains concepts and errors, and reviews my code after I solve it.

## How it works

1. Open the exercise folder and read its `README.md` (press **Ctrl + Shift + V** in VS Code to preview it).
2. Write your code in `solution.py`.
3. Run it in the terminal (**Ctrl + '** in VS Code):

   ```
   python 01-python-foundations/01-fundamentals/02-greeting/solution.py
   ```

4. Type the **Sample Input** and check that what appears is **exactly the same** as the **Sample Output**.
5. Works for every sample? Now try the **⚡ Challenge** at the end of the README. It teaches something new and asks for better, shorter code.
6. Check it off in the progress list below and move on to the next one.

### Solving is only half of it

The first solution that works is rarely the best one. After solving, always ask yourself:

- Can I write it with **fewer lines**, without making it hard to read?
- Is there a part I **repeat**? Can a loop or a variable remove it?
- Would my code still work if the problem **grew** (more numbers, more rules)?

### Important (just like beecrowd)

- **Don't write messages inside `input()`.** Use `input()`, not `input("Enter your name: ")`. The output must match the sample exactly.
- Pay attention to uppercase letters, spaces and punctuation: `SUM = 14` is not the same as `Sum: 14`.

### Golden rules

- **Type the code, don't copy and paste.** Your fingers learn too.
- **Errors are normal.** Read the error message calmly — it almost always tells you the line and the problem.
- **Try for at least 15 minutes** before opening the hints.
- **A little every day beats a lot once a week.** 30 minutes a day makes a big difference.
- Stuck? Ask Claude, but ask for **a hint**, not the answer.

## Roadmap

The goal: **improve real processes with Python and AI, and learn to build AI**. The journey is split into phases, and each phase ends with a **project** for my portfolio.

| Phase | Focus | Project |
|---|---|---|
| [1 — Python foundations](01-python-foundations/) | the language itself: syntax, data, functions, files, OOP | folder organizer |
| 2 — My first AI | call an LLM from Python | terminal chatbot |
| 3 — Coding like a developer | the tools professionals use: Git, tests, logging | chatbot with tests |
| 4 — Automation | make Python do repetitive work | a manual report, automated |
| 5 — Measuring processes | data, SQL, statistics and dashboards | process dashboard |
| 6 — AI in processes | LLMs that read documents and act | document-reading assistant |
| 7 — Building AI | train my own machine learning models | predictive model |
| Final | everything together | end-to-end AI automation |

Each phase below opens with the details.

<details>
<summary><b>Phase 1 — Python foundations</b></summary>

| Level | Topic | What you will learn |
|---|---|---|
| 01 | [Fundamentals](01-python-foundations/01-fundamentals/) | `print`, `input`, variables, types, `if`, `for`, `while`, `//` and `%`, `range` with steps, nested loops, `break` and `continue`, input validation |
| 02 | Strings | concatenation, indexing, slicing, methods (`split`, `join`, `replace`...), formatting, immutability |
| 03 | Data structures | lists, tuples, dictionaries, sets, comprehensions |
| 04 | Functions | `def`, parameters, return values, scope, `import`, `lambda`, `*args`/`**kwargs`, generators, decorators, type hints |
| 05 | Files and errors | reading/writing files, CSV, JSON, `try`/`except` |
| 06 | Object-oriented programming | classes, objects, inheritance |

🎯 **Project:** a tool that organizes the files in a folder automatically.

</details>

<details>
<summary><b>Phase 2 — My first AI</b></summary>

| Level | Topic | What you will learn |
|---|---|---|
| 07 | APIs and my first AI | HTTP, `requests`, JSON, calling an LLM API, writing prompts, getting structured (JSON) answers |

🎯 **Project:** a terminal chatbot that remembers the conversation.

</details>

<details>
<summary><b>Phase 3 — Coding like a developer</b></summary>

| Level | Topic | What you will learn |
|---|---|---|
| 08 | Tools | `pip`, virtual environments (`venv`), Git branches, tests with `pytest`, logging, the debugger |

🎯 **Project:** refactor the chatbot with real tests.

</details>

<details>
<summary><b>Phase 4 — Automation</b></summary>

| Level | Topic | What you will learn |
|---|---|---|
| 09 | Office automation | Excel (`openpyxl`), PDF, e-mail, scheduling scripts to run on their own |
| 10 | Web automation | consuming public APIs, basic web scraping |

🎯 **Project:** a report that is done by hand today, generated on its own.

</details>

<details>
<summary><b>Phase 5 — Measuring processes</b></summary>

| Level | Topic | What you will learn |
|---|---|---|
| 11 | SQL | SQLite, `SELECT`, `JOIN`, aggregations |
| 12 | NumPy and math | arrays, vectors, matrices, the math behind AI |
| 13 | Pandas and charts | data tables, filtering, grouping, Matplotlib and Seaborn |
| 14 | Statistics and dashboards | mean, variation, control charts, dashboards with Streamlit |

🎯 **Project:** a dashboard with a process's indicators (time, bottlenecks, errors).

</details>

<details>
<summary><b>Phase 6 — AI in processes</b></summary>

| Level | Topic | What you will learn |
|---|---|---|
| 15 | LLMs in practice | classify text, extract data from documents, structured output |
| 16 | Agents and RAG | AI that runs tasks and reads internal documents to answer |

🎯 **Project:** an assistant that reads e-mails or documents and fills a spreadsheet.

</details>

<details>
<summary><b>Phase 7 — Building AI</b></summary>

| Level | Topic | What you will learn |
|---|---|---|
| 17 | Machine learning | scikit-learn: prediction, classification, anomaly detection |
| 18 | Neural networks | PyTorch: build and train your own neural network |

🎯 **Project:** a model that predicts something about the process (delays, volume, demand).

</details>

<details>
<summary><b>Final project</b></summary>

A complete AI automation, end to end, with the **before and after measured**.

</details>

## Progress

| Phase | Status |
|---|---|
| 1 — Python foundations | 🟢 in progress |
| 2 — My first AI | ⚪ not started |
| 3 — Coding like a developer | ⚪ not started |
| 4 — Automation | ⚪ not started |
| 5 — Measuring processes | ⚪ not started |
| 6 — AI in processes | ⚪ not started |
| 7 — Building AI | ⚪ not started |
| Final | ⚪ not started |

<details>
<summary><b>Phase 1 · Fundamentals — 3 / 16 done</b></summary>

- [x] 01 Hello World
- [x] 02 Greeting
- [x] 03 Simple Calculator
- [ ] 04 Even or Odd
- [ ] 05 Greatest of Three
- [ ] 06 Multiplication Table
- [ ] 07 Sum Until Zero
- [ ] 08 Count Vowels
- [ ] 09 Challenge: FizzBuzz
- [ ] 10 Types and Conversions
- [ ] 11 Time Converter
- [ ] 12 Countdown
- [ ] 13 Star Triangle
- [ ] 14 Grade Validator
- [ ] 15 Prime Number
- [ ] 16 Final Challenge: Reverse Number

</details>
