# PA05_POT
list_2 = [6, 2, 4, 8]
list_3 = [1, 3, 9, 7]
list_4 = [6, 4, 6, 4]
list_7 = [1, 7, 9, 3]
list_8 = [6, 8, 4, 2]
list_9 = [1, 9, 1, 9]


def return_last_number_of_power(a, b):
    return {
        '0': 0,
        '1': 1,
        '2': (list_2[b]),
        '3': (list_3[b]),
        '4': (list_4[b]),
        '5': 5,
        '6': 6,
        '7': (list_7[b]),
        '8': (list_8[b]),
        '9': (list_9[b]),
    }[a]


D = int(input())
for x in range(D):
    a, b = map(str, input().split())
    a = str(int(a) % 10)
    b = int(int(b) % 4)
    print(return_last_number_of_power(a, b))
