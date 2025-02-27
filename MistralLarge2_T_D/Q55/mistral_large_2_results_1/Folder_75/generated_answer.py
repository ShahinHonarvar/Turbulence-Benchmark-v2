def lists_with_product_equal_n(circular_list):
    n = 13
    size = len(circular_list)
    results = []
    for start in range(size):
        product = 1
        for end in range(size):
            product *= circular_list[(start + end) % size]
            if product == n:
                results.append(circular_list[start:start + end + 1])
            elif product > n:
                break
    return results