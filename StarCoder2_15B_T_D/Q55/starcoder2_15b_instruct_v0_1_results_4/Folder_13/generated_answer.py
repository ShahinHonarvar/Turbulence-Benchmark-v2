def lists_with_product_equal_n(circular_list, n=54):
    result = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + i):
            sublist = circular_list[i:j]
            if len(sublist) <= len(circular_list) and n == 1:
                result.append(sublist)
    return result