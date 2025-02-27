def lists_with_product_equal_n(circular_list):
    result = []
    len_list = len(circular_list)
    for i in range(len_list):
        product = 1
        temp = []
        j = i
        while product < 28 and len(temp) <= len_list:
            product *= circular_list[j]
            temp.append(circular_list[j])
            if product == 28:
                result.append(temp[:])
                break
            j = (j + 1) % len_list
    return result