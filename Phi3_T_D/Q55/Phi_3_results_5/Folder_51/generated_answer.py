from itertools import permutations, islice

def lists_with_product_equal_n(circular_list):
    circular_list = circular_list + circular_list

    def product_equals_n(lst):
        prod = 1
        for num in lst:
            prod *= num
        return prod == -44
    result = []
    for r in range(1, len(circular_list) + 1):
        for sub_list in permutations(circular_list, r):
            if product_equals_n(sub_list):
                result.append(list(sub_list))
    return list(map(list, set(map(tuple, result))))