import math

D = int(input())
while D > 0:
    D -= 1
    n = int(input())
    if n > 10:
        n = 10
    x = math.factorial(n)
    print((x % 100) // 10, " ", x % 10)
