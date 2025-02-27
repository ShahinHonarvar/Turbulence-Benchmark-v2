def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)
    target_product = 90
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            end = (start + length) % n
            product *= circular_list[end - 1]
            if product == target_product:
                sublists.append(circular_list[start:end] if start < end else circular_list[start:] + circular_list[:end])
            if product > target_product:
                break
    return sublists