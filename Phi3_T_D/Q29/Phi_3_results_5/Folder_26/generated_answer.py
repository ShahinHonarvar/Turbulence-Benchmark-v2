def gcf_two_nums(int_list):
    a = int_list[48]
    b = int_list[30]

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(a, b)