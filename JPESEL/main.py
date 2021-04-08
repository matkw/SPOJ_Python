# JPESEL
t = int(input())
pesel_multipler = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
for i in range(t):
    pesel = input()
    pesel = list(map(int, pesel))
    sum_of_pesel_number = sum([int(a * b) for a, b in zip(pesel_multipler, pesel)])
    if sum_of_pesel_number % 10 == 0:
        print("D")
    else:
        print("N")
