def lists_with_product_equal_n(circular_list, n):
    result = []
    for i in range(len(circular_list)):
        current_product = 1
        current_list = []
        for j in range(i, i + len(circular_list)):
            current_product *= circular_list[j % len(circular_list)]
            current_list.append(circular_list[j % len(circular_list)])
            if current_product == n:
                result.append(current_list)
            elif current_product > n:
                break
    return result