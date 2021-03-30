# PRIME_T

def is_prime(number):
    if number < 2:
        return 0
    i = 2
    while int(i)*int(i) <= int(number):
        if number % i == 0:
            return 0
        i += 1
    return 1


test_number = input()
for i in range(int(test_number)):
    number = input()
    if is_prime(int(number)) == 0:
        print("NIE")
    else:
        print("TAK")
