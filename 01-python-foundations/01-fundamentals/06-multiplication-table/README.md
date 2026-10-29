# 06 - Multiplication Table

Read an integer **N** and print its multiplication table from 1 to 10.

## Input

The input contains an integer **N** (2 ≤ N ≤ 1000).

## Output

Print 10 lines in the format `I x N = R`, for I from 1 to 10.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
7
</pre></td>
<td><pre>
1 x 7 = 7
2 x 7 = 14
3 x 7 = 21
4 x 7 = 28
5 x 7 = 35
6 x 7 = 42
7 x 7 = 49
8 x 7 = 56
9 x 7 = 63
10 x 7 = 70
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `for i in range(1, 11):` repeats the block with `i` being 1, 2, ..., 10.
2. `range` stops **before** the second number.

</details>

## ⚡ Challenge

Now print the **whole** multiplication table as a grid, with the columns lined up. Here you learn **nested loops** and how to **align text** with f-strings.

Rules: don't count spaces by hand. Let the f-string do the alignment.

### Input

An integer **N** (1 ≤ N ≤ 12).

### Output

Print N lines. Line I has the results of I x 1, I x 2, ..., I x N. Each number takes exactly **4 characters**, aligned to the right.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
3
</pre></td>
<td><pre>
   1   2   3
   2   4   6
   3   6   9
</pre></td>
</tr>
<tr>
<td><pre>
4
</pre></td>
<td><pre>
   1   2   3   4
   2   4   6   8
   3   6   9  12
   4   8  12  16
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. A `for` can go inside another `for`. The inner one runs **completely** on each turn of the outer one.
2. `print(x, end="")` doesn't break the line. An empty `print()` only breaks it.
3. `f"{7:4}"` gives `"   7"`. Also try `f"{42:<4}"` and `f"{42:^4}"` in the terminal.

</details>
