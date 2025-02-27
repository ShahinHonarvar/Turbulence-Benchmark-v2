def lists_with_product_equal_n(circular_list):
    n = -9
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list) + i):
            sublist = circular_list[i:j % len(circular_list)]
            if len(sublist) > 0 and n == abs((prod := math.prod(sublist))):
                result.append(sublist)
    return result