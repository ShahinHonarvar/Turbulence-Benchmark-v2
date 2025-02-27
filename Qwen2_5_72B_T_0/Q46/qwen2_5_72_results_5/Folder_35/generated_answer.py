def gcf_three_nums(numbers):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a, b, c = (numbers[742], numbers[888], numbers[629])
    return gcd(gcd(a, b), c)