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
