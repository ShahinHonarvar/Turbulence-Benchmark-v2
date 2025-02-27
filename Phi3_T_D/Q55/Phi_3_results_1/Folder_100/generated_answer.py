def lists_with_product_equal_n(circular_list, n=48):
    result = []
    list_len = len(circular_list)
    circular_list *= 2
    for i in range(list_len):
        product = 1
        for j in range(i, i + list_len):
            product *= circular_list[j % list_len]
            if product == n:
                result.append(circular_list[i:i + j % list_len + 1])
                break
            elif product > n:
                break
    return result