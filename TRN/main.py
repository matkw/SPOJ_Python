# TRN
m, n = map(int, input().split())
a = []
for x in range(m):
    a.append([int(j) for j in input().split()])
for i in range(n):
    for j in range(m):
        print(a[j][i]," ", end="")
    print()

# m, n = map(int, input().split())
# list_of_all_numbers = []
# for x in range(m):
#     datas = input()
#     data = datas.split(" ")
#     list_of_all_numbers.extend(data)
#     row_trans = []
# for i in range(n):
#     for j in range(len(list_of_all_numbers)):
#         if int(j) % n == i:
#             row_trans.append(list_of_all_numbers[j])
#     print(*row_trans)
#     row_trans.clear()
