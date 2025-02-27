def lists_with_product_equal_n(circular_list):
    product_target = -15
    sublists = []
    list_length = len(circular_list)
    for i in range(list_length):
        product_so_far = 1
        current_sublist = []
        for j in range(i, i + list_length):
            index = j % list_length
            product_so_far *= circular_list[index]
            current_sublist.append(circular_list[index])
            if product_so_far == product_target:
                sublists.append(current_sublist.copy())
            if product_so_far == 0 or circular_list[index] == 0:
                break
    return sublists