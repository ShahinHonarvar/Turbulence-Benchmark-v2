def lists_with_product_equal_n(circular_list):
    n = -779
    length = len(circular_list)
    result = []
    for i in range(length):
        for j in range(i, length + i):
            product = 1
            sublist = []
            for k in range(i, j % length + i):
                sublist.append(circular_list[k])
                product *= circular_list[k]
            if product == n:
                result.append(sublist)
    return result