def gcf_three_nums(numbers):

    def gcd(x, y):
        while y != 0:
            x, y = (y, x % y)
        return x
    if 29 not in range(len(numbers)) or 74 not in range(len(numbers)) or 49 not in range(len(numbers)):
        raise IndexError('Indices are out of range')
    return gcd(gcd(numbers[29], numbers[74]), numbers[49])