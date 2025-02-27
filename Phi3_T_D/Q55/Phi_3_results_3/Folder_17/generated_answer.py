def lists_with_product_equal_n(circular_list):
    result = []
    size = len(circular_list)
    for i in range(size):
        for j in range(i + 1, size + 1):
            sublist_product = 1
            sublist = circular_list[i:j]
            if j > size:
                sublist += circular_list[:j - size]
            if sublist_product == 18:
                result.append(sublist)
    return result