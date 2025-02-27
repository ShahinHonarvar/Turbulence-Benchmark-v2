def lists_with_product_equal_n(circular_list):
    target_product = 33
    result = []
    length = len(circular_list)
    for i in range(length):
        current_product = 1
        for j in range(i, length + i):
            current_product *= circular_list[j % length]
            if current_product == target_product:
                result.append(circular_list[i:j + 1])
                break
            elif current_product > target_product:
                break
    return result