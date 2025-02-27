def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target_product = 27
    results = []
    for start in range(n):
        product = 1
        sublist = []
        for end in range(start, start + n):
            index = end % n
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == target_product:
                results.append(sublist.copy())
                break
            elif product > target_product:
                break
    return results