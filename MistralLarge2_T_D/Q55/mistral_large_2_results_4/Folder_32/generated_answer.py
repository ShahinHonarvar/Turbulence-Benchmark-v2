def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            idx = (start + end) % n
            product *= circular_list[idx]
            if product == 76:
                sublist = [circular_list[(start + i) % n] for i in range(end + 1)]
                result.append(sublist)
            elif product > 76:
                break
    return result