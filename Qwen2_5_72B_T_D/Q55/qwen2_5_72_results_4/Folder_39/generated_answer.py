def lists_with_product_equal_n(circular_list):
    target_product = -46
    result = []
    n = len(circular_list)
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            end = (start + length - 1) % n
            product *= circular_list[end]
            if product == target_product:
                result.append(circular_list[start:end + 1])
            if product == 0 or abs(product) > abs(target_product):
                break
        product = 1
    return result