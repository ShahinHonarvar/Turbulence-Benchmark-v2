def if_decimal_is_divisible(bin_str):

    def fibonacci_sequence(n):
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib[n - 1]
    decimal = int(bin_str, 2)
    fib_38th = fibonacci_sequence(38)
    return decimal % fib_38th == 0