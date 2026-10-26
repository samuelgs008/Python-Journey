# Python-Journey

A Python journey made with [Claude](https://claude.com/claude-code) to study Python from scratch, beecrowd-style: each exercise has a problem statement, input/output descriptions and sample cases. The path goes from the basics all the way to charts and artificial intelligence, one exercise at a time.

Claude creates the exercises and acts only as a **tutor**: it never writes the solutions or gives the answers. All the code in the `solution.py` files is written by me. When I get stuck, Claude gives hints, explains concepts and errors, and reviews my code after I solve it.

## How it works

1. Open the exercise folder and read its `README.md` (press **Ctrl + Shift + V** in VS Code to preview it).
2. Write your code in `solution.py`.
3. Run it in the terminal (**Ctrl + '** in VS Code):

   ```
   python 01-fundamentals/02-greeting/solution.py
   ```

4. Type the **Sample Input** and check that what appears is **exactly the same** as the **Sample Output**.
5. Works for every sample? Check it off in the progress list below and move on to the next one.

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

| Level | Topic | What you will learn | Status |
|---|---|---|---|
| 01 | [Fundamentals](01-fundamentals/) | `print`, `input`, variables, types, `if`, `for`, `while`, strings | Available |
| 02 | Data structures | lists, tuples, dictionaries, sets, list comprehensions | Locked |
| 03 | Functions and modules | `def`, parameters, return values, scope, `import` | Locked |
| 04 | Files and errors | reading/writing files, CSV, JSON, `try/except` | Locked |
| 05 | Object-oriented programming | classes, objects, inheritance | Locked |
| 06 | Tools | `pip`, virtual environments (`venv`), libraries | Locked |
| 07 | NumPy | arrays and fast math | Locked |
| 08 | Pandas | data tables, filtering, grouping | Locked |
| 09 | Charts | Matplotlib and Seaborn: line, bar, scatter, histograms | Locked |
| 10 | Machine learning | scikit-learn: regression, classification, model evaluation | Locked |
| 11 | Neural networks | PyTorch: build and train your own neural network | Locked |
| 12 | Final project | a complete AI project, from data to charts to model | Locked |

Levels unlock as you progress: when you finish one, ask Claude to create the next.

## My progress — Level 01

- [ ] 01 Hello World
- [ ] 02 Greeting
- [ ] 03 Simple Calculator
- [ ] 04 Even or Odd
- [ ] 05 Greatest of Three
- [ ] 06 Multiplication Table
- [ ] 07 Sum Until Zero
- [ ] 08 Count Vowels
- [ ] 09 Challenge: FizzBuzz
