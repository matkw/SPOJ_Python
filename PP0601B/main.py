# PP0601B
# n - range of number
# x - divisible_number
# y - indivisible_number
t = int(input())
for i in range(t):
    n, x, y = map(int, input().split())
    list_of_answers_ = []
    # print(n, x, y)
    if n > x:
        for j in range(x, n, x):
            if j % y != 0:
                print(j, " ", end='')
        print()
