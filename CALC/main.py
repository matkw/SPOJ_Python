# CALC
import sys


def calculate(symbol, a, b):
    return {
        '+': int(a) + int(b),
        '-': int(a) - int(b),
        '*': int(a) * int(b),
        '/': int(a) // int(b),
        '%': int(a) % int(b),
    }[symbol]


for input_ in sys.stdin:
    data = input_.split(" ")
    print(calculate(data[0], data[1], data[2]))
