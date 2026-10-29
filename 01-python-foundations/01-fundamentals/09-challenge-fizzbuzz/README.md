# 09 - 🏆 Challenge: FizzBuzz

Read an integer **N** and print the numbers from 1 to N, one per line, but:

- for multiples of 3, print `Fizz` instead of the number
- for multiples of 5, print `Buzz`
- for multiples of both 3 **and** 5, print `FizzBuzz`

## Input

The input contains an integer **N** (1 ≤ N ≤ 1000).

## Output

Print N lines following the rules above.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
15
</pre></td>
<td><pre>
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
</pre></td>
</tr>
<tr>
<td><pre>
5
</pre></td>
<td><pre>
1
2
Fizz
4
Buzz
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. The **order** of the `if`s matters! What happens to 15 if you check for 3 first?
2. A multiple of both 3 and 5 is a multiple of 15.

</details>

## ⚡ Challenge

A new rule arrived: **FizzBuzzBazz**! Multiples of 7 now add `Bazz`. Here you learn why some solutions **grow well** and others don't: with `if` / `elif`, every new rule doubles the number of cases.

Rules: **two lines** of code and **no `if`**.

### Input

Two integers **A** and **B** (1 ≤ A ≤ B ≤ 1000) on the same line, separated by a space.

### Output

Print the numbers from A to B, one per line, but:

- multiples of 3 add `Fizz`
- multiples of 5 add `Buzz`
- multiples of 7 add `Bazz`

The words always go in this order. If none of the rules apply, print the number.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
20 22
</pre></td>
<td><pre>
Buzz
FizzBazz
22
</pre></td>
</tr>
<tr>
<td><pre>
103 106
</pre></td>
<td><pre>
103
104
FizzBuzzBazz
106
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. Count it: how many `if` / `elif` branches would you need for 3 rules? And how many lines does a new rule cost if you build the word piece by piece?
2. What is `"Fizz" * True`? And `"Fizz" * False`?
3. `"" or 7` gives `7`. An empty string counts as `False`.

</details>
