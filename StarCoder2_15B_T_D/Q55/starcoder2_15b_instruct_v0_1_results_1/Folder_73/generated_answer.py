def lists_with_product_equal_n(circular_list, n):
    result = []
    for start in range(len(circular_list)):
        current_product = 1
        current_list = []
        for i in range(start, start + len(circular_list)):
            current_product *= circular_list[i % len(circular_list)]
            current_list.append(circular_list[i % len(circular_list)])
            if current_product == n:
                result.append(current_list)
            if current_product == 0:
                break
    return result