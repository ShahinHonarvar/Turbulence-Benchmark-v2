def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for start in range(n):
        product = 1
        for end in range(n):
            product *= circular_list[(start + end) % n]
            if product == -10:
                results.append(circular_list[start:start + end + 1] + circular_list[:(start + end + 1) // n])
    return results