def if_decimal_is_divisible(binary_str):

    def is_fibonacci(num):
        a, b = (0, 1)
        while b < num:
            a, b = (b, a + b)
        return b == num

    def decimal_from_binary(binary_str):
        return int(binary_str, 2)

    def find_147th_fibonacci():
        a, b = (0, 1)
        for _ in range(147):
            a, b = (b, a + b)
        return a
    return decimal_from_binary(binary_str) % find_147th_fibonacci() == 0