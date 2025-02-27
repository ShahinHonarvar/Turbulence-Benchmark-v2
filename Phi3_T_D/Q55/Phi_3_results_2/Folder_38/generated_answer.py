def lists_with_product_equal_n(circular_list):
    target_product = -23
    n = len(circular_list)
    result = []
    for i in range(n):
        temp_product = 1
        for j in range(i, n + i):
            temp_product *= circular_list[j % n]
            if temp_product == target_product:
                result.append(circular_list[i:j + 1])
            if temp_product == 0 or circular_list[j % n] == 0:
                break
    return result