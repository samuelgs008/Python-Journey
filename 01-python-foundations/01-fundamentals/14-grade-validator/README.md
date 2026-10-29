# 14 - Grade Validator

Users make mistakes, and a good program doesn't break because of them. Read grades until you have **two valid ones**, then show their average.

Here you learn to **validate input** with `while` and to skip a loop turn with `continue`.

## Input

The input contains several decimal numbers, one per line. There are always at least two valid grades.

## Output

- For each **invalid** grade (lower than 0 or greater than 10), print `invalid grade`.
- When you have two valid grades, print `AVERAGE = X` with 2 decimal places and stop reading.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
-3.5
3.5
11.0
10.0
</pre></td>
<td><pre>
invalid grade
invalid grade
AVERAGE = 6.75
</pre></td>
</tr>
<tr>
<td><pre>
8.0
7.0
</pre></td>
<td><pre>
AVERAGE = 7.50
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. You don't know how many grades will come, so use `while`. What should the condition be? Think about how many **valid** grades you have.
2. `continue` skips the rest of the loop and goes straight back to the condition. Use it to ignore an invalid grade.
3. Python lets you chain comparisons: `0 <= g <= 10`. Try it in the terminal.

</details>

## ⚡ Challenge

Now the program asks if the user wants **another calculation**, and the answer must be validated too. Here you learn to write a program that **keeps running** until the user decides to stop, with a loop inside another loop.

Rules: use the same validation idea for the grades and for the menu answer.

### Input

Grades like in the main problem. After each average, there is the answer to the menu: `1` (yes) or `2` (no). Invalid answers may appear.

### Output

The same as the main problem. After each average, print `new calculation (1-yes 2-no)`. Print it **again** after each invalid answer. With `1`, start a new calculation. With `2`, end the program.

### Sample

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
-3.5
3.5
11.0
10.0
4
1
9.1
2.3
2
</pre></td>
<td><pre>
invalid grade
invalid grade
AVERAGE = 6.75
new calculation (1-yes 2-no)
new calculation (1-yes 2-no)
AVERAGE = 5.70
new calculation (1-yes 2-no)
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. The whole main problem goes **inside** a bigger loop. `while True:` and `break` are a good fit for the outer one.
2. Reading the menu answer is the same problem as reading a grade: repeat while it is invalid.
3. Don't forget to reset the grades and the counter at the start of each new calculation.

</details>
