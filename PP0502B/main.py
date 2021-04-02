# PP0502B
t = int(input())
for i in range(t):
    data_input = input()
    data = data_input.split(" ")
    n = int(data.pop(0))
    data.reverse()
    for x in data:
        print(x, " ", end='')
