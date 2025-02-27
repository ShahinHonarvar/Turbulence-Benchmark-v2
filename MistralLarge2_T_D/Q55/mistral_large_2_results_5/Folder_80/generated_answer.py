def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(n):
            product *= circular_list[(i + j) % n]
            sublist.append(circular_list[(i + j) % n])
            if product == 43:
                results.append(sublist[:])
            if product > 43:
                break
    return results