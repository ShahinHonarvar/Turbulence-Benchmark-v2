def gcf_three_nums(numbers):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    try:
        a = numbers[412]
        b = numbers[932]
        c = numbers[337]
        result = gcd(gcd(a, b), c)
        return result
    except IndexError:
        return None