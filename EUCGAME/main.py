# EUCGAME
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print(a + b)
