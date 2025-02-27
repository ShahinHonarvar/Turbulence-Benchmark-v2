from itertools import permutations, cycle

def lists_with_product_equal_n(circular_list):

    def has_product_equal_n(sublist, product):
        sublist_product = 1
        for num in sublist:
            sublist_product *= num
        return sublist_product == product
    product_target = -93
    result = []
    n = len(circular_list)
    if n == 0:
        return result
    for i in range(1, n + 1):
        for subset in permutations(circular_list, i):
            if has_product_equal_n(subset, product_target):
                result.append(subset)
    return result