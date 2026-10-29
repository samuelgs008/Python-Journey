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
6. Mark it done in the progress table inside the level's `README.md` and move on to the next one.

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

The goal: **improve real processes with Python and AI, and grow toward Machine Learning Engineering**. The journey is split into phases, and each phase ends with a **project** for my portfolio.

| Phase | Focus | Project | Status |
|---|---|---|---|
| [1 — Python foundations](01-python-foundations/) | the language itself: syntax, data, functions, recursion, algorithms, files, OOP | expense tracker (CLI) | 🟢 in progress |
| 2 — Tools & good practices | the tools professionals use: `venv`, Git, tests, logging | tested, packaged project | ⚪ Locked |
| 3 — My first AI | call an LLM from Python | terminal chatbot | ⚪ Locked |
| 4 — Automation | make Python do repetitive work | a manual report, automated | ⚪ Locked |
| 5 — Data analysis | turn data into insight: SQL, pandas, stats, dashboards | data dashboard | ⚪ Locked |
| 6 — AI in processes | LLMs that read documents and act | document-reading assistant | ⚪ Locked |
| 7 — Machine Learning | train and properly evaluate models (scikit-learn, XGBoost) | well-evaluated prediction model | ⚪ Locked |
| 8 — Deep Learning | PyTorch, computer vision, transformers, reinforcement learning | the red-ball AI + a fine-tuned model | ⚪ Locked |
| 9 — ML Engineering | put a model in production (FastAPI, Docker, cloud, MLflow) | a deployed model with an API & monitoring | ⚪ Locked |
| Final | everything together | end-to-end AI automation | ⚪ Locked |

Each phase below opens with the details.

<details>
<summary><b>Phase 1 — Python foundations</b></summary>

| Level | Topic | What you will learn |
|---|---|---|
| 01 | [Fundamentals](01-python-foundations/01-fundamentals/) | `print`, `input`, variables, types, `if`, `for`, `while`, `//` and `%`, `range` with steps, nested loops, `break` and `continue`, input validation |
| 02 | Strings | concatenation, indexing, slicing, methods (`split`, `join`, `replace`...), formatting, immutability |
| 03 | Data structures | lists, tuples, dictionaries, sets, comprehensions |
| 04 | Functions and recursion | `def`, parameters, return values, scope, `import`, `lambda`, `*args`/`**kwargs`, generators, decorators, type hints, and recursion: factorial, Fibonacci, Tower of Hanoi |
| 05 | Algorithms | searching, sorting, Big O (how fast code is), greedy algorithms and dynamic programming |
| 06 | Files and errors | reading/writing files, CSV, JSON, `try`/`except` |
| 07 | Object-oriented programming | classes, objects, inheritance |

🎯 **Project:** a command-line expense tracker — add expenses, save them to a file, show totals and the biggest ones. (You'll analyze this same data in Phase 5.)

</details>

<details>
<summary><b>Phase 2 — Tools & good practices</b></summary>

| Level | Topic | What you will learn |
|---|---|---|
| 08 | Tools | `pip`, virtual environments (`venv`), Git branches, tests with `pytest`, logging, the debugger, the Linux terminal (WSL) |

🎯 **Project:** turn the expense tracker into a real project — a virtual environment, tests with `pytest`, and a clean Git history.

</details>

<details>
<summary><b>Phase 3 — My first AI</b></summary>

| Level | Topic | What you will learn |
|---|---|---|
| 09 | APIs and my first AI | HTTP, `requests`, JSON, calling an LLM API, writing prompts, getting structured (JSON) answers |

🎯 **Project:** a terminal chatbot that remembers the conversation.

</details>

<details>
<summary><b>Phase 4 — Automation</b></summary>

| Level | Topic | What you will learn |
|---|---|---|
| 10 | Office automation | Excel (`openpyxl`), PDF, e-mail, scheduling scripts to run on their own |
| 11 | Web automation | consuming public APIs, basic web scraping |

🎯 **Project:** a report that is done by hand today, generated on its own.

</details>

<details>
<summary><b>Phase 5 — Data analysis</b></summary>

| Level | Topic | What you will learn |
|---|---|---|
| 12 | SQL | SQLite, `SELECT`, `JOIN`, aggregations |
| 13 | NumPy & math for ML | arrays, vectors and matrices (linear algebra), derivatives and the gradient idea, probability — the math behind ML |
| 14 | Pandas and charts | data tables, filtering, grouping, Matplotlib and Seaborn |
| 15 | Statistics and dashboards | mean, variation, control charts, dashboards with Streamlit |

🎯 **Project:** a dashboard with a process's indicators (time, bottlenecks, errors).

</details>

<details>
<summary><b>Phase 6 — AI in processes</b></summary>

| Level | Topic | What you will learn |
|---|---|---|
| 16 | LLMs in practice | classify text, extract data from documents, structured output |
| 17 | Agents and RAG | AI that runs tasks and reads internal documents to answer |

🎯 **Project:** an assistant that reads e-mails or documents and fills a spreadsheet.

</details>

<details>
<summary><b>Phase 7 — Machine Learning</b></summary>

| Level | Topic | What you will learn |
|---|---|---|
| 18 | ML foundations | scikit-learn: train/test split, cross-validation, overfitting, feature engineering, choosing the right metric |
| 19 | Gradient boosting | XGBoost and LightGBM — the models that win most real tabular problems |

🎯 **Project:** a prediction model (e.g. process delays) that is trained and **properly evaluated**, not just `.fit()`.

</details>

<details>
<summary><b>Phase 8 — Deep Learning</b></summary>

| Level | Topic | What you will learn |
|---|---|---|
| 20 | Neural networks | PyTorch: tensors, autograd, build and train your own network |
| 21 | Computer vision | CNNs: teach a model to recognize images |
| 22 | Transformers & Hugging Face | attention, embeddings, using and fine-tuning pretrained models (LoRA) |
| 23 | Reinforcement learning | an agent that learns by trial and error (Gymnasium, Stable-Baselines3) |

🎯 **Project:** the **red-ball agent** — an AI that learns to reach a random target as fast as it can. (Plus a fine-tuned Hugging Face model.)

</details>

<details>
<summary><b>Phase 9 — ML Engineering</b></summary>

| Level | Topic | What you will learn |
|---|---|---|
| 24 | Serve a model | wrap a model in a FastAPI API and package it with Docker |
| 25 | Cloud & MLOps | deploy to a free cloud tier, track experiments with MLflow, monitor the model |

🎯 **Project:** a model of mine **live on the internet**, with an API and basic monitoring.

</details>

<details>
<summary><b>Final project</b></summary>

A complete AI automation, end to end, with the **before and after measured**.

</details>
