def lists_with_product_equal_n(circular_list):
    product_target = -69
    result = []
    length = len(circular_list)
    if not circular_list or length == 0:
        return result
    for i in range(length):
        temp_product = 1
        sublist = []
        for j in range(i, i + length):
            index = j % length
            temp_product *= circular_list[index]
            sublist.append(circular_list[index])
            if temp_product == product_target:
                result.append(sublist.copy())
            elif temp_product * circular_list[i] > product_target:
                break
    return result