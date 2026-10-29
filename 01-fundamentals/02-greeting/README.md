# 02 - Greeting

Write a program that reads a person's **name** and **age** and greets them.

## Input

The first line contains a name. The second line contains an integer **A** (0 ≤ A ≤ 150), the person's age.

## Output

Print `Hello, NAME! You are A years old.`

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
Ana
20
</pre></td>
<td><pre>
Hello, Ana! You are 20 years old.
</pre></td>
</tr>
<tr>
<td><pre>
Samuel
18
</pre></td>
<td><pre>
Hello, Samuel! You are 18 years old.
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `name = input()` reads one line and stores it in the variable `name`.
2. f-strings let you put variables inside text: `f"Hi, {name}"`.

</details>

## ⚡ Challenge

Already solved it? Now try again: solve it in **a single line**, without creating any variables.

### Input

The same as the main problem: a name on the first line and the age **A** on the second.

### Output

Print `Hello, NAME! You are A years old.`

### Sample

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
Ana
20
</pre></td>
<td><pre>
Hello, Ana! You are 20 years old.
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. Anything can go inside the `{}` of an f-string, even a call to `input()`.
2. Do you really need `int()` if you only print the age?

</details>
