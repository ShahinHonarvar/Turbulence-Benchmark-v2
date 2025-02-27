def lists_with_product_equal_n(circular_list):
    n = -91
    size = len(circular_list)
    result = []
    for start in range(size):
        product = 1
        for end in range(size):
            product *= circular_list[(start + end) % size]
            if product == n:
                sublist = [circular_list[(start + i) % size] for i in range(end + 1)]
                result.append(sublist)
            elif product > n:
                break
    return result