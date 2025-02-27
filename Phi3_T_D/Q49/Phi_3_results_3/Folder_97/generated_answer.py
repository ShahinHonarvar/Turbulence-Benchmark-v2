def if_decimal_is_divisible(binary_str):

    def fib_up_to(n):
        a, b = (0, 1)
        fib_nums = []
        while len(fib_nums) < n:
            a, b = (b, a + b)
            fib_nums.append(a)
        return fib_nums[n - 1]
    fib_114th = fib_up_to(114)
    decimal = int(binary_str, 2)
    return decimal % fib_114th == 0