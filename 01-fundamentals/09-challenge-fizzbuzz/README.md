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
