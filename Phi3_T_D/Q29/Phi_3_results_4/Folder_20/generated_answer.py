def gcf_two_nums(numbers):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    if len(numbers) > 94:
        return gcd(numbers[19], numbers[94])
    else:
        raise IndexError('List must have at least 95 elements')