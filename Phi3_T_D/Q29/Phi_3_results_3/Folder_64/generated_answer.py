def gcf_two_nums(int_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(int_list[6], int_list[9])