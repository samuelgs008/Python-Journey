# 09 - 🏆 Challenge: FizzBuzz
a,b = map(int,input().split())
for i in range(a,b+1): print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) + "Bazz" * (i % 7 == 0) or i)