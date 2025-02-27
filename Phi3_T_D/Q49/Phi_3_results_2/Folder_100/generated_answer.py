def if_decimal_is_divisible(binary_str):

    def fib_190():
        a, b = (0, 1)
        count = 0
        while count < 190:
            a, b = (b, a + b)
            count += 1
        return a
    decimal_value = int(binary_str, 2)
    fib_190th_value = fib_190()
    return decimal_value % fib_190th_value == 0