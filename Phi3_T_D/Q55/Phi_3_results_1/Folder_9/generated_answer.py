def lists_with_product_equal_n(circular_list, n=-36):
    len_list = len(circular_list)
    result = []
    for i in range(len_list):
        for j in range(i + 1, len_list + 1):
            sublist = circular_list[i:j] + circular_list[:i]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result