# 10 - Types and Conversions

Every value in Python has a **type**. The same characters can behave very differently depending on it: `"42" * 2` and `42 * 2` give completely different results.

Read an integer **A**, a decimal number **B** and a text **C**, then show the type of each value and what happens when you mix and convert them.

## Input

The first line contains an integer **A**. The second line contains a decimal number **B**. The third line contains a text **C** made only of digits.

## Output

Print seven lines, exactly as in the samples:

- `A = ` followed by A, ` -> ` and the type name of A
- `B = ` followed by B, ` -> ` and the type name of B
- `C = ` followed by C, ` -> ` and the type name of C
- `A + B = ` followed by the result, ` -> ` and the type name of the result
- `C * 2 = ` followed by C repeated twice (C is **text**!)
- `int(C) * 2 = ` followed by C converted to an integer, times 2
- `bool(A) = ` followed by A converted to `bool`

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
7
2.5
42
</pre></td>
<td><pre>
A = 7 -> int
B = 2.5 -> float
C = 42 -> str
A + B = 9.5 -> float
C * 2 = 4242
int(C) * 2 = 84
bool(A) = True
</pre></td>
</tr>
<tr>
<td><pre>
0
3.0
10
</pre></td>
<td><pre>
A = 0 -> int
B = 3.0 -> float
C = 10 -> str
A + B = 3.0 -> float
C * 2 = 1010
int(C) * 2 = 20
bool(A) = False
</pre></td>
</tr>
<tr>
<td><pre>
-3
0.5
007
</pre></td>
<td><pre>
A = -3 -> int
B = 0.5 -> float
C = 007 -> str
A + B = -2.5 -> float
C * 2 = 007007
int(C) * 2 = 14
bool(A) = True
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `type(x)` tells you the type of `x`, but it prints `<class 'int'>`. Try `type(x).__name__` to get only `int`.
2. Each value needs its own conversion: `int(...)`, `float(...)`, or none at all for text.
3. Why does `bool(0)` give `False` but `bool(-3)` gives `True`? Test some numbers in the terminal and find out.
4. Look at sample 3: why does `C` show `007`, but `int(C) * 2` gives `14`?

</details>
