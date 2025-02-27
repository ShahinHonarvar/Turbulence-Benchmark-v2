def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        sublist = []
        for j in range(i, i + len(circular_list)):
            sublist.append(circular_list[j % len(circular_list)])
            if len(sublist) > len(circular_list):
                break
            product = 1
            for num in sublist:
                product *= num
            if product == -32:
                result.append(sublist)
    return result