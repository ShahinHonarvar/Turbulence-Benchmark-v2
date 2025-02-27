def gcf_three_nums(numbers):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a = numbers[90]
    b = numbers[54]
    c = numbers[96]
    return gcd(gcd(a, b), c)