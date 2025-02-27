def gcf_three_nums(numbers):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(gcd(numbers[8], numbers[2]), numbers[1])