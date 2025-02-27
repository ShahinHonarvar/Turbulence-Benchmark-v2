def lists_with_product_equal_n(circular_list):
    target_product = 32
    n = len(circular_list)
    results = []
    for start in range(n):
        product = 1
        for end in range(n):
            actual_end = (start + end) % n
            product *= circular_list[actual_end]
            if product == target_product:
                results.append(circular_list[start:actual_end + 1])
            elif product > target_product:
                break
    return results