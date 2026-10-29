# 12 - Countdown

A rocket is about to launch! Read a number **N** and do the countdown.

Until now, your `range` always counted up, one by one. Here you learn to make it count **down**.

## Input

The input contains an integer **N** (1 ≤ N ≤ 100).

## Output

Print the numbers from N down to 1, one per line. Then print `Liftoff!`.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
5
</pre></td>
<td><pre>
5
4
3
2
1
Liftoff!
</pre></td>
</tr>
<tr>
<td><pre>
1
</pre></td>
<td><pre>
1
Liftoff!
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `range` accepts a third number, the **step**: `range(0, 10, 2)` gives 0, 2, 4, 6, 8. Try it.
2. The step can be negative. What does `range(5, 0, -1)` give?
3. Remember: `range` stops **before** the second number.

</details>

## ⚡ Challenge

Now print the whole countdown on **one line**. Here you learn the **unpacking operator** `*`, which spreads the values of a sequence.

Rules: **two lines** of code and **no `for`**.

### Input

The same as the main problem: an integer **N** (1 ≤ N ≤ 100).

### Output

Print the numbers from N down to 1 and then `Liftoff!`, all on the same line, separated by `, ` (comma and space).

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
5
</pre></td>
<td><pre>
5, 4, 3, 2, 1, Liftoff!
</pre></td>
</tr>
<tr>
<td><pre>
1
</pre></td>
<td><pre>
1, Liftoff!
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. Try `print(*"abc")` and `print(*range(3))` in the terminal. What does the `*` do?
2. `print()` accepts many values, and `sep` decides what goes between them.
3. `Liftoff!` can be just one more value in the same `print()`.

</details>
