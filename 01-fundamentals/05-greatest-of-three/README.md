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
