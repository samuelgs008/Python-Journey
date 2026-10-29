# 13 - Star Triangle

Read a number **N** and draw a triangle of stars with N lines.

Here you practice **nested loops**: a loop inside another loop. They are the base of tables, grids, games and many algorithms.

## Input

The input contains an integer **N** (1 ≤ N ≤ 50).

## Output

Print N lines. Line 1 has 1 star, line 2 has 2 stars, and so on.

⚠️ Print **one star at a time**: no `"*" * i` for now. The goal is to practice the loop inside the loop!

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
3
</pre></td>
<td><pre>
*
**
***
</pre></td>
</tr>
<tr>
<td><pre>
5
</pre></td>
<td><pre>
*
**
***
****
*****
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. The outer loop chooses the **line**. The inner loop prints the **stars** of that line.
2. `print("*", end="")` prints a star without breaking the line. An empty `print()` only breaks it.
3. On line `i`, how many stars are there? Use that in the `range` of the inner loop.

</details>

## ⚡ Challenge

Now draw a **pyramid**, centered. Here you learn to find the **formula** behind a pattern, and you'll see how string multiplication can replace a whole loop.

Rules: **only one `for`**, no loop inside it. Now `"*" * i` is allowed!

### Input

An integer **N** (1 ≤ N ≤ 50).

### Output

Print a pyramid with N lines. The last line has no spaces at the start, and no line has spaces at the end.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
3
</pre></td>
<td><pre>
  *
 ***
*****
</pre></td>
</tr>
<tr>
<td><pre>
4
</pre></td>
<td><pre>
   *
  ***
 *****
*******
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. Make a little table for N = 4. Line 1: 3 spaces and 1 star. Line 2: 2 spaces and 3 stars... Do you see the pattern?
2. The number of spaces goes **down** by 1 each line, and the number of stars goes **up** by 2.
3. You can add strings: `" " * 2 + "*" * 3` gives `"  ***"`.

</details>
