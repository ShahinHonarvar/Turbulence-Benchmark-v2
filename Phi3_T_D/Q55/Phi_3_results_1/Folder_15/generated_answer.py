def lists_with_product_equal_n(circular_list):
    n = -7
    result = []
    for i in range(len(circular_list)):
        current_product = 1
        for j in range(i, len(circular_list) + i):
            current_product *= circular_list[j % len(circular_list)]
            if current_product == n:
                result.append(circular_list[i % len(circular_list):j % len(circular_list) + 1])
            elif current_product > n:
                break
    return result