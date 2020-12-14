def fib(n):
    arr = [1, 1]
    for i in range(3, n + 1):
        tmp = sum(arr)
        arr = [arr[1], tmp]
    return arr[1]


def fib3(n):
    arr = [1, 1, 1]
    for i in range(4, n + 1):
        tmp = sum(arr)
        arr = [arr[1], arr[2], tmp]
    return arr[2]


def squares(n):
    return [i ** 2 for i in range(1,n+1,2)]

if __name__ == '__main__':
    ###
    # for 1
    print("for 1")
    print(fib(7))
    # for 2
    print("for 2")
    print(fib3(7))
    # for 3
    print("for 3")
    print(squares(7))
    # for 4
    print("for 4")
    a=10
    b = 21
    s = sum(range(a, b))
    m = 1
    for i in range(a, b):
        m *= i
    print("{:d} {:d}".format(s, m))
    # for 5
    print("for 5")
    a = 10
    b = 20
    print([i for i in range(a+1,b) if i % 2 == 0])
    print([i for i in range(a+1,b) if i % 2 == 1])
    # for 6
    print("for 6")
    arr = [1, -1, 2, -2, 3, -3, 4, 5]
    print([i for i in arr if i > 0])
    print([i for i in arr if i < 0])