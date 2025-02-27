def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    sublists = []
    for i in range(length):
        for j in range(i + 1, length + i):
            sublist = circular_list[i:j]
            product = 1
            for element in sublist:
                product *= element
            if product == 990:
                sublists.append(sublist)
    return sublists