# 07 - Sum Until Zero

Read integers one by one until a **0** appears. Then print the sum of all the numbers read.

## Input

The input contains several integers, one per line. The last one is always **0**.

## Output

Print `SUM = X`.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
5
3
2
0
</pre></td>
<td><pre>
SUM = 10
</pre></td>
</tr>
<tr>
<td><pre>
0
</pre></td>
<td><pre>
SUM = 0
</pre></td>
</tr>
<tr>
<td><pre>
10
-4
100
0
</pre></td>
<td><pre>
SUM = 106
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. Create a variable `total = 0` **before** the loop.
2. `while condition:` repeats while the condition is true.
3. `break` exits the loop immediately.

</details>

## ⚡ Challenge

Now also show **how many** numbers were read and their **average**. Here you learn the **walrus operator** `:=` and how to avoid dividing by zero.

Rules: call `input()` **only once** in the whole program.

### Input

The same as the main problem: several integers, one per line. The last one is always **0** (it doesn't count).

### Output

Print three lines: `SUM = X`, `COUNT = Y` and `AVERAGE = Z` with 2 decimal places. If no number was read before the 0, the average is `0.00`.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
5
3
2
0
</pre></td>
<td><pre>
SUM = 10
COUNT = 3
AVERAGE = 3.33
</pre></td>
</tr>
<tr>
<td><pre>
10
-4
100
0
</pre></td>
<td><pre>
SUM = 106
COUNT = 3
AVERAGE = 35.33
</pre></td>
</tr>
<tr>
<td><pre>
0
</pre></td>
<td><pre>
SUM = 0
COUNT = 0
AVERAGE = 0.00
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. The walrus operator **saves a value and uses it at the same time**: `while (n := int(input())) != 0:` reads `n` and checks it in one line.
2. What happens with `0 / 0`? Try it. Look at sample 3: you need to protect the average from this.
3. The one-line `if` from the exercise 04 challenge works great here.

</details>
