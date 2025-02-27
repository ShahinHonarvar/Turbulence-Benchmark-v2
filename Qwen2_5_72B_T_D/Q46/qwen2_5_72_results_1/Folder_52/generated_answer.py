def gcf_three_nums(numbers):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a = numbers[19]
    b = numbers[49]
    c = numbers[74]
    return gcd(gcd(a, b), c)