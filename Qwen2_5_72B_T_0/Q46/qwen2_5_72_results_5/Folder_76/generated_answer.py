def gcf_three_nums(numbers):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a, b, c = (numbers[876], numbers[203], numbers[100])
    return gcd(gcd(a, b), c)