for _ in range(int(input())):
    u,v,a,s = [int(val) for val in input().split()]
    if u ** 2 - 2 * a * s <= v ** 2:
        print("Yes")
    else:
        print("No")