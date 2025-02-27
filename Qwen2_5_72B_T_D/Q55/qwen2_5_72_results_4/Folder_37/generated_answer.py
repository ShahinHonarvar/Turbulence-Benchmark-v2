def lists_with_product_equal_n(circular_list):
    target_product = -76
    length = len(circular_list)
    results = []
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            index = end % length
            product *= circular_list[index]
            if product == target_product:
                results.append(circular_list[start:index + 1])
            elif abs(product) > abs(target_product):
                break
    return results