def gcf_three_nums(numbers_list):
    a = numbers_list[7]
    b = numbers_list[6]
    c = numbers_list[8]

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(gcd(a, b), c)