from itertools import cycle, combinations

def lists_with_product_equal_n(circ_list):
    target_product = -690
    results = []
    for i in range(1, len(circ_list) + 1):
        for sub_list in combinations(cycle(circ_list), i):
            if prod(sub_list) == target_product:
                results.append(list(sub_list))
    return results

def prod(iterable):
    result = 1
    for x in iterable:
        result *= x
    return result