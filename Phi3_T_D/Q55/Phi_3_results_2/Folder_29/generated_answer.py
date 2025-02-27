def lists_with_product_equal_n(circular_list):
    if len(circular_list) < 1:
        return []
    target_product = 15
    result = []
    for i in range(len(circular_list)):
        product_so_far = 1
        sublist = []
        for j in range(len(circular_list)):
            tail_index = (i + j) % len(circular_list)
            product_so_far *= circular_list[tail_index]
            sublist.append(circular_list[tail_index])
            if product_so_far == target_product:
                result.append(sublist.copy())
                break
            if product_so_far > target_product:
                break
    return result