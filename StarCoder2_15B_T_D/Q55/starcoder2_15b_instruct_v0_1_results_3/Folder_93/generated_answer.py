def lists_with_product_equal_n(circular_list):
    n = -91
    result = []
    for i in range(len(circular_list)):
        sublist = []
        current_product = 1
        j = i
        while current_product != n:
            sublist.append(circular_list[j])
            current_product *= circular_list[j]
            j = (j + 1) % len(circular_list)
            if len(sublist) >= len(circular_list):
                break
        if current_product == n:
            result.append(sublist)
    return result