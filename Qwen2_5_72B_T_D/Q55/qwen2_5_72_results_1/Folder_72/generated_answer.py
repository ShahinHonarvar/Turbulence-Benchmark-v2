def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    circular_list *= 2
    target_product = 10
    results = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= circular_list[end]
            if product == target_product:
                results.append(circular_list[start:end + 1])
            elif product > target_product:
                break
    return results