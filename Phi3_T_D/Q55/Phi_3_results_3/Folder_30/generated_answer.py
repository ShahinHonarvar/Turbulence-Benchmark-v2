def lists_with_product_equal_n(circular_list):
    to_return = []
    list_len = len(circular_list)
    for i in range(list_len):
        product = 1
        sublist = []
        for j in range(i, list_len + i):
            current_index = j % list_len
            product *= circular_list[current_index]
            sublist.append(circular_list[current_index])
            if product == 99:
                to_return.append(sublist[:])
                break
            elif product > 99:
                break
    return to_return