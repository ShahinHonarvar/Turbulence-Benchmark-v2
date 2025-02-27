def lists_with_product_equal_n(circular_list):
    n = -61
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            sublist = circular_list[i:j + 1] + circular_list[:i]
            if i != 0:
                sublist = sublist + circular_list[j + 1:i]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                sublists.append(sublist)
    return sublists