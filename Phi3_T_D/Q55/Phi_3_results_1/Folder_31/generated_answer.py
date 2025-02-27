def lists_with_product_equal_n(circular_list):
    circular_list.extend(circular_list[:1])
    result = []
    for i in range(len(circular_list) - 1):
        product = 1
        for j in range(i, len(circular_list) - 1):
            product *= circular_list[j]
            if product == -16:
                result.append(circular_list[i:j + 1])
    return result[1:]