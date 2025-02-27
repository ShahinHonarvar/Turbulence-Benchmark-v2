def gcf_three_nums(numbers):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    first = gcd(numbers[20], numbers[51])
    return gcd(first, numbers[62])