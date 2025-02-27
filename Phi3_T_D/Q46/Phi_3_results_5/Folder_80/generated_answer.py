def gcf_three_nums(int_list):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(gcd(int_list[13], int_list[76]), int_list[44])