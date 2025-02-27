def lists_with_product_equal_n(circular_list):
    target_product = 33
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            actual_index = (start + end) % n
            product *= circular_list[actual_index]
            if product == target_product:
                result.append(circular_list[start:actual_index + 1])
            elif product > target_product:
                break
    return result