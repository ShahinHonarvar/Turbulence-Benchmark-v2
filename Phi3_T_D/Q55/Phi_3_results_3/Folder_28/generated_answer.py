def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    product_target = 85
    result = []

    def helper(start, end, current_product, current_list):
        if start == end:
            if current_product == product_target:
                result.append(current_list)
            return
        if current_list:
            helper(start, end, current_product * circular_list[end], current_list + [circular_list[end]])
        helper(start, end, current_product, current_list)
    for i in range(2, n):
        helper(0, i, circular_list[0], [circular_list[0]])
    if n > 1 and circular_list[0] * circular_list[-1] == product_target:
        result.append([circular_list[-1], circular_list[0]])
    return result