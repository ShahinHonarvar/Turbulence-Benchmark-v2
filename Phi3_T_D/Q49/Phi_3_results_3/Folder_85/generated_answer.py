def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)

    def fibonacci(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        prev, curr = (0, 1)
        for _ in range(2, n + 1):
            prev, curr = (curr, prev + curr)
        return curr
    fib_45 = fibonacci(45)
    return decimal_num % fib_45 == 0