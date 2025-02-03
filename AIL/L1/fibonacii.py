def fib(num: int) -> int:
    n1 = 0
    n2 = 1
    fib_seq = []
    for i in range(num):
        fib_seq.append(n2)
        temp = n2
        n2 = n1 + n2
        n1 = temp

    return fib_seq

print(fib(7))

