def lists_with_product_equal_n(circular_list):
    target_product = 57
    sublists = []
    list_len = len(circular_list)
    for i in range(list_len * 2):
        for j in range(i, i + list_len):
            product = 1
            sublist = []
            for k in range(i, i + list_len):
                current_index = k % list_len
                product *= circular_list[current_index]
                sublist.append(circular_list[current_index])
                if len(sublist) >= 2 and product == target_product:
                    sublists.append(sublist[:])
                elif product > target_product:
                    break
    return sublists