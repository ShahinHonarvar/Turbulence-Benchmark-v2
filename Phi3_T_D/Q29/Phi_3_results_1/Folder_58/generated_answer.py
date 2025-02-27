def gcf_two_nums(int_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(int_list[128], int_list[581])