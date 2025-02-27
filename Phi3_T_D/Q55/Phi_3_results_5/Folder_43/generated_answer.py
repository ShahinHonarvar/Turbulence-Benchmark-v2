def lists_with_product_equal_n(circular_list):
    n = -26
    size = len(circular_list)
    sublists = []
    for i in range(size):
        for j in range(i, size + i):
            product = 1
            temp_sublist = []
            for idx in range(i, j % size):
                product *= circular_list[idx % size]
                temp_sublist.append(circular_list[idx % size])
                if product == n and len(temp_sublist) <= size:
                    sublists.append(temp_sublist[:])
            if product == n and len(temp_sublist) <= size:
                sublists.append(temp_sublist)
    return sublists