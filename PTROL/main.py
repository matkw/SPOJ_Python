# PTROL
t = int(input())
for i in range(t):
    input_ = input()
    data = input_.split(" ")
    data.pop(0)
    data.append(data.pop(0))
    for x in data:
        print(x, " ", end="")
