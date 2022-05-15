for _ in range(int(input())):
    d,l,r = [int(value) for value in input().split()]
    if l <= d <= r:
        print("Take second dose now")
    elif d < l:
        print("Too Early") 
    elif d > r:
        print("Too late")