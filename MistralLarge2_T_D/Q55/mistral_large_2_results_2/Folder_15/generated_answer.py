def lists_with_product_equal_n(circular_list):
    if not circular_list:
        return []
    n = -7
    length = len(circular_list)
    result = []
    for i in range(length):
        product = 1
        sublist = []
        for j in range(length):
            index = (i + j) % length
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == n:
                result.append(sublist[:])
            if product != n and product != 1 and (n % product != 0):
                break
    return result