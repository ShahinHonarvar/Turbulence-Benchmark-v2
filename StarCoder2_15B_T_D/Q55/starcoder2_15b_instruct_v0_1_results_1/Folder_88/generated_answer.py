def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        sublist = []
        product = 1
        for j in range(i, i + len(circular_list)):
            index = j % len(circular_list)
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == -56:
                result.append(sublist)
            elif product < -56:
                break
    return result