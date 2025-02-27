def lists_with_product_equal_n(circular_list):
    target_product = -81
    length = len(circular_list)
    sublists = []
    for size in range(1, length + 1):
        for start in range(length):
            contiguous_sublist = circular_list[start:start + size] + circular_list[0:max(0, start + size - length)]
            product = 1
            for number in contiguous_sublist:
                product *= number
            if product == target_product:
                sublists.append(contiguous_sublist)
    return sublists