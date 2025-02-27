def gcf_three_nums(numbers):
    a = numbers[13]
    b = numbers[76]
    c = numbers[44]

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(gcd(a, b), c)