# PP0602A
t = int(input())
for i in range(t):
    datas_ = input()
    data = datas_.split(" ")
    for j in range(2, int(data[0]) + 1, 2):
        print(data[j], " ", end="")
    for j in range(1, int(data[0]) + 1, 2):
        print(data[j], " ", end="")
    print()