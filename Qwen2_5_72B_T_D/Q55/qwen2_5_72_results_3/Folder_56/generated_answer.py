def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target_product = -65
    result = []
    for start in range(n):
        product = 1
        for current in range(n):
            idx = (start + current) % n
            product *= circular_list[idx]
            if product == target_product:
                result.append(circular_list[start:idx + 1])
            if abs(product) > abs(target_product):
                break
    return result