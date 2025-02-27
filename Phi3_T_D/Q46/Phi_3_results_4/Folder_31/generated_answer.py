def gcf_three_nums(num_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    index_gcd = gcd(num_list[90], gcd(num_list[54], num_list[96]))
    return index_gcd