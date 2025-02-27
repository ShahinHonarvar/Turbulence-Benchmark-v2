def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        sublist = [circular_list[i]]
        product = circular_list[i]
        j = (i + 1) % len(circular_list)
        while product != -906 and j != i:
            sublist.append(circular_list[j])
            product *= circular_list[j]
            j = (j + 1) % len(circular_list)
        if product == -906:
            result.append(sublist)
    return result