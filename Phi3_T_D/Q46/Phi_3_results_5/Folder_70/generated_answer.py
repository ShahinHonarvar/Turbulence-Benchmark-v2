def gcf_three_nums(int_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(int_list[990], gcd(int_list[671], int_list[711]))