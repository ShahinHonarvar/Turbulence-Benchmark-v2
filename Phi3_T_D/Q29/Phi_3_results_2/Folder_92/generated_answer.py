def gcf_two_nums(nums_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(nums_list[0], nums_list[0])