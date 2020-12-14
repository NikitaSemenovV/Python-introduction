def scd(target):
    arr = [2]
    i = 3
    c = 0
    sum = 2
    while sum < target:
        if all(i % n != 0 for n in arr):
            sum += i
            c += 1
            arr.append(i)
        i += 1
    return c


def fst(target):
    i = 1
    sum = 0
    while sum < target:
        sum += 2 ** i
        i += 1
    return i


if __name__ == '__main__':
    ###
    print("while 1")
    print("При 1000 = ", fst(1000))
    print("При 10000 = ", fst(10000))
    print("while 2")
    print("При 1000 = ", scd(1000))
    print("При 10000 = ", scd(10000))
    print("while 3")
    i = 1
    path = 10
    sum = 0
    while i < 31:
        sum += path
        path += path * 0.15
        i += 1
    print(sum)
    print("while 4")
    i = 1
    path = 10
    sum = 0
    while path < 20:
        path += path * 0.1
        i += 1
    print("Пункт а = ", i)
    i = 1
    path = 10
    sum = 0
    while sum <= 100:
        path += path * 0.1
        sum += path
        i += 1
    print("Пункт б = ", i)