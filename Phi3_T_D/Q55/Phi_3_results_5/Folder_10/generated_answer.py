def lists_with_product_equal_n(circular_list):
    target_product = -93
    circular_len = len(circular_list)
    result = []
    for i in range(circular_len):
        product = 1
        for j in range(i, circular_len + i):
            product *= circular_list[j % circular_len]
            if product == target_product:
                result.append(circular_list[i:j + 1])
            elif product > target_product:
                break
    return result