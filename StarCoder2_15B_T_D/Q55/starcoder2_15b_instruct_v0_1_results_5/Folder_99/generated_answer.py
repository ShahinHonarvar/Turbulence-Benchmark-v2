def lists_with_product_equal_n(circular_list, n=415):
    result = []
    for i in range(len(circular_list)):
        current_product = 1
        current_sublist = []
        for j in range(i, i + len(circular_list)):
            current_product *= circular_list[j % len(circular_list)]
            current_sublist.append(circular_list[j % len(circular_list)])
            if current_product == n:
                result.append(current_sublist)
            elif current_product > n:
                break
    return result