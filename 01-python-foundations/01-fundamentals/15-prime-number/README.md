# 15 - Prime Number

A number is **prime** when it has exactly two divisors: 1 and itself. 7 is prime. 12 is not (it can be divided by 2, 3, 4 and 6).

Read a number and say whether it is prime. Here you learn to stop a loop early with `break`.

## Input

The input contains an integer **N** (1 ≤ N ≤ 100000).

## Output

Print `N is prime` or `N is not prime`.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
7
</pre></td>
<td><pre>
7 is prime
</pre></td>
</tr>
<tr>
<td><pre>
12
</pre></td>
<td><pre>
12 is not prime
</pre></td>
</tr>
<tr>
<td><pre>
1
</pre></td>
<td><pre>
1 is not prime
</pre></td>
</tr>
<tr>
<td><pre>
2
</pre></td>
<td><pre>
2 is prime
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. Test every number from 2 to N - 1: does any of them divide N? (`%` again!)
2. Create a variable like `is_prime = True` before the loop, and change it when you find a divisor.
3. Found one divisor? You already know the answer. `break` stops the loop right there.
4. Look at sample 3: 1 is **not** prime. Does your code agree?

</details>

## ⚡ Challenge

Now N can be as big as **1 000 000 000 000** (a trillion). Your solution would test almost a trillion numbers: that takes hours! Here you learn to make code **fast** by thinking before typing, and you meet `for ... else`.

Rules: answer in less than 1 second, and **no `is_prime` variable**.

### Input

An integer **N** (1 ≤ N ≤ 1000000000000).

### Output

Print `N is prime` or `N is not prime`.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
97
</pre></td>
<td><pre>
97 is prime
</pre></td>
</tr>
<tr>
<td><pre>
999999999989
</pre></td>
<td><pre>
999999999989 is prime
</pre></td>
</tr>
<tr>
<td><pre>
1000000000000
</pre></td>
<td><pre>
1000000000000 is not prime
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. If N = a × b, one of the two is always **small**: at most the square root of N. So you only need to test up to √N. For a trillion, that is only a million tests.
2. `n ** 0.5` is the square root of `n`. Remember that `range` needs an `int`.
3. A `for` can have an `else`! It runs **only if the loop finished without a `break`**. Try it with a small loop in the terminal.

</details>
