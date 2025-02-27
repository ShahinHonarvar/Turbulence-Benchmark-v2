def lists_with_product_equal_n(circular_list):
    target_product = 83
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for current in range(n):
            index = (start + current) % n
            product *= circular_list[index]
            if product == target_product:
                result.append(circular_list[start:index + 1])
            if product > target_product:
                break
    return result