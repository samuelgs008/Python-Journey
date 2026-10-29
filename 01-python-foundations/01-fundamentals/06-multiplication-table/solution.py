# 06 - Multiplication Table

n = int(input())
#columns
for row in range(1,n + 1):
    for col in range(1,n + 1):
        print(row * col, end=" ")
    print("")
    
    