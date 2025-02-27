def lists_with_product_equal_n(circular_list):

    def is_sublist_product_equal_n(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == -1
    n = len(circular_list)
    lists = []
    for i in range(n):
        for j in range(i + 1, n + i):
            sublist = circular_list[i:j]
            if is_sublist_product_equal_n(sublist):
                lists.append(sublist)
    return lists