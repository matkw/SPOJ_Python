# PTCLTZ
t = int(input())
for x in range(t):
    s = int(input())
    iteration = 0
    while s != 1:
        if s % 2 == 0:
            s = s/2
        else:
            s = 3*s + 1
        iteration += 1
    print(iteration)
