def lists_with_product_equal_n(circular_list):
    n = 57
    sublists = []
    list_length = len(circular_list)
    circular_list += circular_list
    for i in range(list_length):
        product = 1
        for j in range(list_length):
            product *= circular_list[i + j]
            if product > n:
                break
            if product == n:
                sublist = circular_list[i:i + j + 1]
                sublists.append(sublist)
                break
    return sublists