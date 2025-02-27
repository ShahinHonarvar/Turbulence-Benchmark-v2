def lists_with_product_equal_n(circular_list, n):

    def is_sublist_product_equal_n(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == n
    result = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + i):
            sublist = circular_list[i:j]
            if is_sublist_product_equal_n(sublist):
                result.append(sublist)
    return result