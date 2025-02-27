from math import gcd

def gcf_three_nums(lst):

    def find_multiple_gcd(num_indices, nums_list):
        result = nums_list[num_indices[0]]
        for index in num_indices[1:]:
            result = gcd(result, nums_list[index])
        return result
    indices = [31, 25, 80]
    return find_multiple_gcd(indices, lst)