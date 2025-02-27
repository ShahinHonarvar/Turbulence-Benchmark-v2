def gcf_three_nums(numbers):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a = numbers[876]
    b = numbers[203]
    c = numbers[100]
    return gcd(gcd(a, b), c)