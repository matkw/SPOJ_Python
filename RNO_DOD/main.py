t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    numbers = input()
    number = numbers.split(' ')
    sum = 0
    for x in number:
        sum += int(x)
    print(sum)