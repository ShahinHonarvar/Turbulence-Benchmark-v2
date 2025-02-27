def gcf_three_nums(int_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(gcd(int_list[1], int_list[6]), int_list[8])