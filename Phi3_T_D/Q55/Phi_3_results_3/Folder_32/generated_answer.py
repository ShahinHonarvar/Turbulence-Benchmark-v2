def lists_with_product_equal_n(circular_list):
    target_product = 76
    result = []
    length = len(circular_list)
    for start in range(length):
        prod = 1
        sublist = []
        for i in range(length):
            prod *= circular_list[(start + i) % length]
            if prod == target_product:
                sublist.append(circular_list[(start + i) % length])
                result.append(sublist[:])
                break
            elif prod > target_product:
                break
    return result