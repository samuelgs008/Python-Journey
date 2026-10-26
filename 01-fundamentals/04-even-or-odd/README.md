# 04 - Even or Odd

Read an integer **N** and tell whether it is even or odd.

## Input

The input contains a single integer **N**.

## Output

Print `N is even` or `N is odd`.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
8
</pre></td>
<td><pre>
8 is even
</pre></td>
</tr>
<tr>
<td><pre>
7
</pre></td>
<td><pre>
7 is odd
</pre></td>
</tr>
<tr>
<td><pre>
0
</pre></td>
<td><pre>
0 is even
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `a % b` gives the **remainder** of `a` divided by `b`. Example: `7 % 2` is `1`.
2. A number is even when the remainder of dividing it by 2 is 0.
3. Equality comparison uses `==` (two signs), not `=`.

</details>
