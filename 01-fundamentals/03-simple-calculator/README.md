# 03 - Simple Calculator

Read two integers **A** and **B** and print their sum, difference, product and quotient.

## Input

The input contains two integers **A** and **B**, one per line (B ≠ 0).

## Output

Print four lines, exactly as in the samples:

- `SUM = ` followed by A + B
- `DIFFERENCE = ` followed by A - B
- `PRODUCT = ` followed by A * B
- `QUOTIENT = ` followed by A / B **with 2 decimal places**

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
10
4
</pre></td>
<td><pre>
SUM = 14
DIFFERENCE = 6
PRODUCT = 40
QUOTIENT = 2.50
</pre></td>
</tr>
<tr>
<td><pre>
9
3
</pre></td>
<td><pre>
SUM = 12
DIFFERENCE = 6
PRODUCT = 27
QUOTIENT = 3.00
</pre></td>
</tr>
<tr>
<td><pre>
-7
2
</pre></td>
<td><pre>
SUM = -5
DIFFERENCE = -9
PRODUCT = -14
QUOTIENT = -3.50
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `input()` always returns **text** (`str`). `"10" + "4"` is `"104"`, not 14!
2. Convert it: `a = int(input())`.
3. To show 2 decimal places: `f"{value:.2f}"`.

</details>
