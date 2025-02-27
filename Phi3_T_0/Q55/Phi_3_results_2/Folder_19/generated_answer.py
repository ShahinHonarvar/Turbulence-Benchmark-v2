def lists_with_product_equal_n(circular_list):
    target_product = -54
    result = []
    n = len(circular_list)
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i + n):
            index = j % n
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == target_product:
                result.append(sublist.copy())
                break
            elif product > target_product:
                break
    return result