# Python-Journey

A Python journey made with [Claude](https://claude.com/claude-code) to study Python from scratch. The exercises are inspired by beecrowd: each one has a problem statement, input/output descriptions and sample cases. They don't follow beecrowd 100%, though: some of them, especially in the later levels, are bigger projects. The path goes from the basics all the way to charts and artificial intelligence, one exercise at a time.

Claude creates the exercises and acts only as a **tutor**: it never writes the solutions or gives the answers. All the code in the `solution.py` files is written by me. When I get stuck, Claude gives hints, explains concepts and errors, and reviews my code after I solve it.

## How it works

1. Open the exercise folder and read its `README.md` (press **Ctrl + Shift + V** in VS Code to preview it).
2. Write your code in `solution.py`.
3. Run it in the terminal (**Ctrl + '** in VS Code):

   ```
   python 01-fundamentals/02-greeting/solution.py
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

| Level | Topic | What you will learn | Status |
|---|---|---|---|
| 01 | [Fundamentals](01-fundamentals/) | `print`, `input`, variables, types, `if`, `for`, `while` | Available |
| 02 | Strings | concatenation, indexing, slicing, methods (`split`, `join`, `replace`...), formatting, immutability and how strings are stored | Locked |
| 03 | Data structures | lists, tuples, dictionaries, sets, list comprehensions | Locked |
| 04 | Functions and recursion | `def`, parameters, return values, scope, `import`, recursion: factorial, Fibonacci, Tower of Hanoi | Locked |
| 05 | Algorithms | searching, sorting, greedy algorithms, dynamic programming, complexity (Big O) | Locked |
| 06 | Files and errors | reading/writing files, CSV, JSON, `try/except` | Locked |
| 07 | Object-oriented programming | classes, objects, inheritance | Locked |
| 08 | Tools | `pip`, virtual environments (`venv`), libraries | Locked |
| 09 | NumPy | arrays and fast math | Locked |
| 10 | Pandas | data tables, filtering, grouping | Locked |
| 11 | Charts | Matplotlib and Seaborn: line, bar, scatter, histograms | Locked |
| 12 | Machine learning | scikit-learn: regression, classification, model evaluation | Locked |
| 13 | Neural networks | PyTorch: build and train your own neural network | Locked |
| 14 | Final project | a complete AI project, from data to charts to model | Locked |

Levels 01–05 build the problem-solving and logic foundation (the kind of thing beecrowd trains). Levels 06–14 lead to data, charts and artificial intelligence.

Levels unlock as you progress: when you finish one, ask Claude to create the next.

## My progress — Level 01

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
