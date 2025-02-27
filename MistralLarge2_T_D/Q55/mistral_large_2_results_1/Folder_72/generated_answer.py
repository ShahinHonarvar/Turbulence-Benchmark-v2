def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for i in range(n):
            idx = (start + i) % n
            product *= circular_list[idx]
            sublist.append(circular_list[idx])
            if product == 10:
                result.append(sublist[:])
            elif product > 10:
                break
    return result