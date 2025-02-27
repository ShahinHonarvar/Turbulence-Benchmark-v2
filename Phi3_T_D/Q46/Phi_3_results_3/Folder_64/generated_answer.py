def gcf_three_nums(numbers):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a, b, c = (numbers[0], numbers[8], numbers[3])
    return gcd(gcd(a, b), c)