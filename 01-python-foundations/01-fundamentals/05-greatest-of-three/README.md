# 05 - Greatest of Three

Read three integers and print the greatest one.

⚠️ Don't use the `max()` function — the goal is to practice `if`!

## Input

The input contains three integers **A**, **B** and **C** on the **same line**, separated by spaces.

## Output

Print `GREATEST = X`, where X is the greatest of the three numbers.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
4 9 2
</pre></td>
<td><pre>
GREATEST = 9
</pre></td>
</tr>
<tr>
<td><pre>
10 3 7
</pre></td>
<td><pre>
GREATEST = 10
</pre></td>
</tr>
<tr>
<td><pre>
-8 -3 -5
</pre></td>
<td><pre>
GREATEST = -3
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. To read three numbers from one line: `a, b, c = map(int, input().split())`. For now, just use it as a recipe — you'll understand it in Level 2.
2. `a` is the greatest if `a >= b and a >= c`.
3. Use `if` / `elif` / `else`.

</details>

## ⚡ Challenge

Three numbers is easy. What about **any** amount? Here you learn the **"greatest so far"** pattern, one of the most used ideas in programming.

Rules: still no `max()` or `min()`, and no lists. Your code must work the same for 1 number or 100 numbers.

### Input

The first line contains an integer **N** (1 ≤ N ≤ 100). Then come **N** integers, one per line.

### Output

Print two lines: `GREATEST = X` and `SMALLEST = Y`.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
3
4
9
2
</pre></td>
<td><pre>
GREATEST = 9
SMALLEST = 2
</pre></td>
</tr>
<tr>
<td><pre>
4
-8
-3
-5
-10
</pre></td>
<td><pre>
GREATEST = -3
SMALLEST = -10
</pre></td>
</tr>
<tr>
<td><pre>
1
7
</pre></td>
<td><pre>
GREATEST = 7
SMALLEST = 7
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. Keep a variable with the greatest number **seen so far**. For each new number, ask only: "is this one bigger?"
2. Why not start with `greatest = 0`? Look at sample 2.
3. The first number you read is a perfect starting value for both variables.
4. `for _ in range(N):` repeats N times. The `_` means "I don't need the counter".

</details>
