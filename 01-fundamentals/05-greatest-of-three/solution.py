# 05 - Greatest of Three
A, B, C = map(int,input().split())
if(A > B and A > C):
    print(f"GREATEST = {A}")
elif(B > C):
    print(f"GREATEST = {B}")
else:
    print(f"GREATEST = {C}")

    #GR = MAX(A, B, C)