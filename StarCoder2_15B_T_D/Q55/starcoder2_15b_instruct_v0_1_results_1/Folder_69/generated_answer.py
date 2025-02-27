def lists_with_product_equal_n(circular_list):
    n = 90
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        for j in range(i, i + len(circular_list)):
            index = j % len(circular_list)
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == n:
                result.append(sublist)
                break
            elif product > n:
                break
    return result