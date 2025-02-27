def lists_with_product_equal_n(circular_list):
    result = []
    list_size = len(circular_list)
    for sublist_size in range(1, list_size + 1):
        for start_index in range(list_size):
            sublist = circular_list[start_index:start_index + sublist_size]
            if len(sublist) < sublist_size:
                sublist += circular_list[:sublist_size - len(sublist)]
            product = 1
            for num in sublist:
                product *= num
            if product == -94:
                result.append(sublist)
    return result