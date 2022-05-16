for _ in range(int(input())):
    (n,a,b,c) = [int(value) for value in input().split()]
    if b >= n and a + c >= n:
        print("YES")
    else:
        print("NO")