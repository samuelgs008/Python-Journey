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

## ⚡ Challenge

Already solved it? Now learn Python's **one-line `if`** and make your code work for **negative numbers** too.

Rules: **two lines** of code and **no `if` / `else` block**.

### Input

A single integer **N**, which can be negative.

### Output

Print `N is even` or `N is odd`.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
-4
</pre></td>
<td><pre>
-4 is even
</pre></td>
</tr>
<tr>
<td><pre>
-7
</pre></td>
<td><pre>
-7 is odd
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. Python has a one-line `if`, called a **conditional expression**: `value_if_true if condition else value_if_false`. It can go right inside an f-string.
2. In many languages, `-7 % 2` gives `-1`. Test it in Python: what does it give? Would `n % 2 == 1` be safe here?
3. Bonus: `n % 2` is already `0` or `1`, and `bool(0)` is `False` (you'll see this in exercise 10). Can you write the condition without `==`?

</details>
