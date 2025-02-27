def gcf_three_nums(numbers):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a, b, c = (numbers[78], numbers[19], numbers[13])
    return gcd(gcd(a, b), c)