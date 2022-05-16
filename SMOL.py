# using recursion
# 3
# 5 2
# 4 4
# 2 5
def calcualte(n,k):
    if n < k:
        return n 
    else:
        return calcualte(n-k,k)

for _ in range(int(input())):
    n,k = [int(val) for val in input().split()]
    print(calcualte(n,k))
# using iteration
for _ in range(int(input())):
    n,k = [int(val)for val in input().split()]
    while not n < k:
        n = n - k 
    print(n)

# correct method
for _ in range(int(input())):
    n,k = [int(val)for val in input().split()]
    if k == 0:
        print(n)
    else:
        print(n % k)