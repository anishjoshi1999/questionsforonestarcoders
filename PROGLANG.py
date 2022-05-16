for _ in range(int(input())):
    a,b,a1,b1,a2,b2 = [int(val) for val in input().split()]
    if a1 in [a,b] and b1 in [a,b]:
        print(1)
    elif a2 in [a,b] and b2 in [a,b]:
        print(2)
    else:
        print(0)
# Output
# 3
# 1 2 2 1 3 4
# 3 4 2 1 4 3
# 1 2 1 3 2 4