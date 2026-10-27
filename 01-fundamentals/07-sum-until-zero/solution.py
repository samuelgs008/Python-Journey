# 07 - Sum Until Zero
total = 0
n = int(input().lower())
while n != 0:
    total += n
    n = int(input())
print(f"SUM = {total}")