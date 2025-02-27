def gcf_three_nums(numbers):
    a, b, c = (numbers[31], numbers[69], numbers[40])

    def gcd(x, y):
        while y != 0:
            x, y = (y, x % y)
        return x
    return gcd(gcd(a, b), c)