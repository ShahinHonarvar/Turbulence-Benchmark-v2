def Fibonacci(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[n - 1]

def if_decimal_is_divisible(binary_str):
    fib_77th = Fibonacci(77)
    decimal = int(binary_str, 2)
    return decimal % fib_77th == 0