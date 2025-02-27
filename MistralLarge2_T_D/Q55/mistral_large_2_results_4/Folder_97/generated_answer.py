def lists_with_product_equal_n(circular_list):
    n = -938
    len_list = len(circular_list)
    result = []
    for i in range(len_list):
        for j in range(i, i + len_list):
            sublist = circular_list[i:j + 1] if j < len_list else circular_list[i:] + circular_list[:j - len_list + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result