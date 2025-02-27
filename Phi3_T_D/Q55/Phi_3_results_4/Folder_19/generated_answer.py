def lists_with_product_equal_n(circular_list):
    n = -54
    found_sublists = []
    list_len = len(circular_list)
    for i in range(list_len):
        for j in range(i, list_len):
            product = 1
            sublist = circular_list[i:j + 1]
            for num in sublist:
                product *= num
            if product == n:
                found_sublists.append(sublist)
            if j == list_len:
                break
    return found_sublists