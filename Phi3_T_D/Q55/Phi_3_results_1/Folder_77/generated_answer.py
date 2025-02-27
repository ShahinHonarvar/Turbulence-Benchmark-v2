def lists_with_product_equal_n(circular_list):
    target_product = 632
    result = []
    n = len(circular_list)
    circular_list = circular_list + circular_list[1:]
    for i in range(n):
        temp_product = 1
        for j in range(i, n + i):
            temp_product *= circular_list[j % n]
            if temp_product == target_product:
                result.append(circular_list[i:j + 1])
    return result