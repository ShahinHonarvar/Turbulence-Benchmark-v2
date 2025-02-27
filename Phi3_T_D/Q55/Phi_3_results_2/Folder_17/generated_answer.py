def lists_with_product_equal_n(circular_list):
    n = 18
    result = []
    for i in range(len(circular_list)):
        prod = 1
        for j in range(i, len(circular_list) + i):
            prod *= circular_list[j % len(circular_list)]
            if prod == n:
                result.append(circular_list[i:j % len(circular_list) + 1])
            elif prod > n:
                break
    return result