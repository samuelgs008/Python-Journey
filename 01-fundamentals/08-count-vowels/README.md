# 08 - Count Vowels

Read a sentence and count how many vowels (a, e, i, o, u) it has. Uppercase and lowercase letters count the same.

## Input

The input contains a single line with a sentence (letters and spaces only).

## Output

Print the number of vowels.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
Programming in Python
</pre></td>
<td><pre>
5
</pre></td>
</tr>
<tr>
<td><pre>
AEIOU xyz
</pre></td>
<td><pre>
5
</pre></td>
</tr>
<tr>
<td><pre>
rhythm
</pre></td>
<td><pre>
0
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `for letter in sentence:` goes through each character.
2. `"a" in "aeiou"` is `True`.
3. `sentence.lower()` makes everything lowercase.

</details>
