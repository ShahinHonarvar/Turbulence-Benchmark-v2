def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            end = (start + size) % n
            product *= circular_list[end]
            if product == -94:
                result.append(circular_list[start:start + size])
            if product == 0:
                break
    return result