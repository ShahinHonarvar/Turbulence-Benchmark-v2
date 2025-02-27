def lists_with_product_equal_n(circular_list, target=83):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= circular_list[j % n]
            if product == -83:
                result.append(circular_list[i:j + 1])
                break
            elif product > -83:
                break
    return result