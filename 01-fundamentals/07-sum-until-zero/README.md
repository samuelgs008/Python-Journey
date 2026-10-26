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
