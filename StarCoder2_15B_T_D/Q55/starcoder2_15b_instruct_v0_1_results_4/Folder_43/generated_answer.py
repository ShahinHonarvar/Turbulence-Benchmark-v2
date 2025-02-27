def lists_with_product_equal_n(circular_list, n):
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + i):
            sublist = circular_list[i:j]
            product = 1
            for element in sublist:
                product *= element
            if product == n:
                sublists.append(sublist)
    return sublists