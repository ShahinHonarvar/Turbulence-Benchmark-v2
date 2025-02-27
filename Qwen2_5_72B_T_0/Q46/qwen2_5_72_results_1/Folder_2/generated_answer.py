def gcf_three_nums(numbers):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a, b, c = (numbers[307], numbers[920], numbers[463])
    return gcd(gcd(a, b), c)