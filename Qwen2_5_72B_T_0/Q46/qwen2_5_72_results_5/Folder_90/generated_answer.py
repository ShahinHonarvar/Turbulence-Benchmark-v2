def gcf_three_nums(numbers):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a = numbers[818]
    b = numbers[606]
    c = numbers[873]
    return gcd(gcd(a, b), c)