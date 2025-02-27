def lists_with_product_equal_n(circular_list):
    target_product = 93
    n = len(circular_list)
    results = []
    for start in range(n):
        for end in range(1, n + 1):
            sublist = circular_list[start:] + circular_list[:end]
            if len(sublist) <= n and product(sublist) == target_product:
                results.append(sublist)
    return results

def product(lst):
    p = 1
    for num in lst:
        p *= num
    return p