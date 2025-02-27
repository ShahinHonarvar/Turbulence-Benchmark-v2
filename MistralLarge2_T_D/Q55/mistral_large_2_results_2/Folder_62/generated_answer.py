def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for start in range(n):
        product = 1
        for end in range(n):
            product *= circular_list[(start + end) % n]
            if product == 100:
                results.append(circular_list[start:start + end + 1])
            elif product > 100:
                break
    return results