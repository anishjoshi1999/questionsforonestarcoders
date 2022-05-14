for _ in range(int(input())):
    n,s = [int(val) for val in input().split()]
    if(n>=s):
        print(s)
    else:
        print(2*n - s)
