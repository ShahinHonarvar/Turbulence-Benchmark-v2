def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    product_target = 10
    found_sublists = []
    for i in range(size):
        for j in range(i + 1, i + size):
            product = 1
            sublist = []
            for index in range(i, j % size + 1):
                product *= circular_list[index % size]
                sublist.append(circular_list[index % size])
            if product == product_target:
                found_sublists.append(sublist)
    return found_sublists