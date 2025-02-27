def lists_with_product_equal_n(circular_list):
    total_product = 1
    for num in circular_list:
        total_product *= num
    if total_product % 81 != 0:
        return []
    result = []
    for i in range(len(circular_list)):
        product = 1
        for j in range(i, len(circular_list)):
            if j == len(circular_list) - 1 and i == 0:
                product *= circular_list[-1] * circular_list[0]
            else:
                product *= circular_list[j]
            if product == total_product // 81:
                result.append(circular_list[i:j + 1])
            if product > total_product // 81:
                break
    return result