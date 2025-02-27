def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + i):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -72:
                sublists.append(sublist)
    return sublists