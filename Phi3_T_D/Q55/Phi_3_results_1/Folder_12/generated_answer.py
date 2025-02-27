def lists_with_product_equal_n(circular_list):
    target_product = -18
    n = len(circular_list)
    result = []
    for i in range(n):
        current_product = 1
        for j in range(i, i + n):
            current_product *= circular_list[j % n]
            if current_product == target_product:
                result.append(circular_list[i:j + 1])
            elif current_product > target_product:
                break
    return result