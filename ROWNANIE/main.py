# ROWNANIE
import sys
for datas in sys.stdin:
    data = datas.split(" ")
    delta = float(data[1]) * float(data[1]) - 4 * float(data[0]) * float(data[2])
    if delta > 0:
        print(2)
    if delta == 0:
        print(1)
    if delta < 0:
        print(0)
