def lists_with_product_equal_n(circular_list):
    n = -26
    result = []
    for i in range(len(circular_list)):
        prod = 1
        for j in range(i, len(circular_list) + i):
            prod *= circular_list[j % len(circular_list)]
            if prod == n:
                result.append(circular_list[i % len(circular_list):j % len(circular_list) + 1])
                break
            elif prod > n:
                break
    return result