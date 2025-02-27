def lists_with_product_equal_n(circular_list):
    n = 415
    result = []
    length = len(circular_list)
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            index = j % length
            product *= circular_list[index]
            if product == n:
                result.append(circular_list[i:index + 1])
            elif product > n:
                break
    return result