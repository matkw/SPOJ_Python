# CALC2
import sys


def calculate(symbol, a, b):
    return {
        '+': int(a) + int(b),
        '-': int(a) - int(b),
        '*': int(a) * int(b),
        '/': int(a) // int(b),
        '%': int(a) % int(b),
    }[symbol]


register = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for input_ in sys.stdin:
    data = input_.split(" ")
    if data[0] == "z":
        register[int(data[1])] = data[2]
    else:
        print(calculate(data[0], register[int(data[1])], register[int(data[2])]))
