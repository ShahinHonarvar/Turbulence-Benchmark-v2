def lists_with_product_equal_n(circular_list):
    target_product = -26
    n = len(circular_list)
    results = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            index = (start + length - 1) % n
            product *= circular_list[index]
            if product == target_product:
                results.append(circular_list[start:index + 1])
            elif abs(product) > abs(target_product):
                break
    return results