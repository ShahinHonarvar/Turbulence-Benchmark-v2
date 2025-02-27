from itertools import product

def lists_with_product_equal_n(circular_list):
    n = 53
    result = []
    for i in range(len(circular_list)):
        prods = []
        for j in range(i, len(circular_list) + i):
            prod = 1
            for k in range(i, j + i):
                prod *= circular_list[k % len(circular_list)]
            if prod == n:
                prods.append(circular_list[i % len(circular_list):j % len(circular_list)] + circular_list[:i % len(circular_list)])
        result.extend(prods)
    return result