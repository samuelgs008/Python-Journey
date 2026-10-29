# 07 - Sum Until Zero
total = 0
count = 0
while (n := int(input())) != 0:
    total += n
    count += 1

print(f"SUM = {total}\nCOUNT = {count}\nAVERAGE = {total / count:.2f}")

# while (line := input()) != "leave":
#    print(line)
