# FLAMASTE
C = int(input())
for i in range(C):
    my_string = input()
    symbol = my_string[0]
    counter = 0
    for j in range(0, len(my_string)):
        if my_string[j] == symbol:
            counter += 1
        else:
            if counter > 2:
                print(symbol + str(counter), end="")
            else:
                for x in range(counter):
                    print(symbol, end="")
            counter = 1
            symbol = my_string[j]
        if j == len(my_string) - 1:
            if counter > 2:
                print(symbol + str(counter), end="")
            else:
                for x in range(counter):
                    print(symbol, end="")
    print()
