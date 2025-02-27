def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(n):
            index = (i + j) % n
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == -9:
                result.append(sublist[:])
            if product != -9 and j >= n - 1:
                break
            if product == 0:
                break
    return result