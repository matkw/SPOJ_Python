def nwd(a, b):
    while a != b:
        if a < b:
            b -= a
        else:
            a -= b
    print(a)


t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    nwd(a, b)
