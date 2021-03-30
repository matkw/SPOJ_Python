# VSR
t = int(input())
while t > 0:
    t -= 1
    v1, v2 = map(int, input().split())
    vsr = 2 * v1 * v2 / (v1 + v2)
    print(int(vsr))

