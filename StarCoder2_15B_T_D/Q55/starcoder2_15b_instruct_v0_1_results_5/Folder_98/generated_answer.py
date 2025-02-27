def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        current_product = 1
        current_sublist = []
        for j in range(i, i + n):
            index = j % n
            current_product *= circular_list[index]
            current_sublist.append(circular_list[index])
            if current_product == -1:
                result.append(current_sublist[:])
                current_sublist = []
                current_product = 1
        if current_product == -1:
            result.append(current_sublist)
    return result