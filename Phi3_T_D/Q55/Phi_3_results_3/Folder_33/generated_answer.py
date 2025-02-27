def lists_with_product_equal_n(circular_list):
    target_product = -115
    results = []
    n = len(circular_list)
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= circular_list[j % n]
            if product == target_product:
                sublist = circular_list[i:(j + 1) % n]
                results.append(sublist)
            elif product > target_product:
                break
    return results