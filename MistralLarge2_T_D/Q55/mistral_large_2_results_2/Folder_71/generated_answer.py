def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for end in range(start, start + n):
            idx = end % n
            product *= circular_list[idx]
            sublist.append(circular_list[idx])
            if product == 47:
                result.append(sublist[:])
            elif product > 47:
                break
    return result