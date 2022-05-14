for _ in range(int(input())):
    value = [int(val) for val in input().split()]
    result = (value[1] - value[0]) // value[2]
    print(result)