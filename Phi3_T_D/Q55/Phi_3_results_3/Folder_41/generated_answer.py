from functools import reduce
        from operator import mul

def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    result = []

    def check_sublist(sublist, target):
        return reduce(mul, sublist, 1) == target
    for i in range(size):
        for j in range(i, i + size):
            sublist = circular_list[i:j % size]
            if check_sublist(sublist, -20):
                result.append(sublist)
    return result