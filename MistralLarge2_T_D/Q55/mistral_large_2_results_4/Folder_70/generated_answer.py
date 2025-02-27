def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for start in range(n):
        product = 1
        sublist = []
        for i in range(n):
            idx = (start + i) % n
            product *= circular_list[idx]
            sublist.append(circular_list[idx])
            if product == 32:
                results.append(sublist[:])
            elif product > 32:
                break
    return results