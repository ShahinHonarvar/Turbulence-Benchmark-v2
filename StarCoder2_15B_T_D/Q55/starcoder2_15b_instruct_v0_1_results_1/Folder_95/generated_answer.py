def lists_with_product_equal_n(circular_list, n=28):
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1):
            sublist = circular_list[i:j]
            if len(sublist) > len(circular_list):
                sublist = sublist[:len(circular_list)]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                sublists.append(sublist)
    return sublists