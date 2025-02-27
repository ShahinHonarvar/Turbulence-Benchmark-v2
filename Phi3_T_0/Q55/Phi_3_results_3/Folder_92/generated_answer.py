def lists_with_product_equal_n(circular_list):
    n = 5
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list) + i):
            sublist = circular_list[i:j % len(circular_list)]
            if len(sublist) > 0 and all((x == n for x in sublist)):
                result.append(sublist)
    return result