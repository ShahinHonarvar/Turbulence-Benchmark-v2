def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for i in range(n):
            product *= circular_list[(start + i) % n]
            if product == 99:
                result.append(circular_list[start:start + i + 1])
            elif product > 99:
                break
    return result