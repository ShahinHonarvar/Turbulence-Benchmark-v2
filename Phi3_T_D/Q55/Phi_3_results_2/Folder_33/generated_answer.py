def lists_with_product_equal_n(circular_list, target_product):
    if len(circular_list) == 0:
        return []

    def product_sublist(start, end):
        cur_product = 1
        for idx in range(start, end % len(circular_list)):
            cur_product *= circular_list[idx]
        return cur_product == target_product
    result = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + i):
            if product_sublist(i, j):
                result.append(circular_list[i:j % len(circular_list)])
    return result