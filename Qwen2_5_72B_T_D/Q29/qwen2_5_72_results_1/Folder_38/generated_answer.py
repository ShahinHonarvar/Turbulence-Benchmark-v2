def gcf_two_nums(numbers):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(numbers[88], numbers[35])