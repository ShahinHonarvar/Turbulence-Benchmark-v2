def lists_with_product_equal_n(circular_list):
    target_product = 32
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            real_index = end % length
            product *= circular_list[real_index]
            if product == target_product:
                result.append(circular_list[start:real_index + 1])
            elif product > target_product:
                break
    return result