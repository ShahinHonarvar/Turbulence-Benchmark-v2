def lists_with_product_equal_n(circular_list):
    n = 733
    result = []
    for i in range(len(circular_list)):
        prod = 1
        subset = []
        for j in range(i, i + len(circular_list)):
            index = j % len(circular_list)
            prod *= circular_list[index]
            subset.append(circular_list[index])
            if prod == n:
                result.append(subset.copy())
                break
            if prod > n:
                break
    return result