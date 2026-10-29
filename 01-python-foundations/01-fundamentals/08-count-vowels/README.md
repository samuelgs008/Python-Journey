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

## ⚡ Challenge

Now count the **vowels and the consonants**. Here you learn that `True` and `False` are numbers too, and that sometimes the best code is the one you **don't** write.

Rules: **no `if`** in the whole program.

### Input

The same as the main problem: a single line with a sentence (letters and spaces only).

### Output

Print two lines: `VOWELS = X` and `CONSONANTS = Y`.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
Programming in Python
</pre></td>
<td><pre>
VOWELS = 5
CONSONANTS = 14
</pre></td>
</tr>
<tr>
<td><pre>
AEIOU xyz
</pre></td>
<td><pre>
VOWELS = 5
CONSONANTS = 3
</pre></td>
</tr>
<tr>
<td><pre>
rhythm
</pre></td>
<td><pre>
VOWELS = 0
CONSONANTS = 6
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. What does `"a" in "aeiou"` give? And what is `5 + True`? Try both in the terminal.
2. Do you really need to count the consonants one by one? Every letter is either a vowel or a consonant...
3. `len("abc")` gives `3`, and `"a b".replace(" ", "")` gives `"ab"`.

</details>
