def lists_with_product_equal_n(circular_list):
    target_product = 415
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            index = (start + length - 1) % n
            product *= circular_list[index]
            if product == target_product:
                result.append(circular_list[start:index + 1])
            elif product > target_product:
                break
    return result