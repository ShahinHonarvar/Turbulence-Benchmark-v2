def lists_with_product_equal_n(circular_list):
    n = 537
    result = []
    length = len(circular_list)
    for i in range(length):
        product = 1
        for j in range(i, length):
            product *= circular_list[j % length]
            if product == n:
                result.append(circular_list[i:j + 1])
            elif product > n:
                break
    return result