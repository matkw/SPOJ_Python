def nwd(a, b):
    while a != b:
        if a < b:
            b -= a
        else:
            a -= b
    return a


def nww(a, b):
    return (a * b) / nwd(a, b)


T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(int(nww(a, b)))
