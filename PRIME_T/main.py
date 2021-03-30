# PRIME_T
import sys

test_number = input()
for i in range(int(test_number)):
    number = input()
    check = 0
    for i in range(int(number)):
        if int(number) % int(i + 1) == 0:
            check += 1
        if check > 2:
            break
    if check != 2:
        print('NIE')
    else:
        print('TAK')
