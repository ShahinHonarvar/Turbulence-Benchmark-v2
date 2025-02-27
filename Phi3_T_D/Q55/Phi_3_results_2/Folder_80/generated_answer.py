def lists_with_product_equal_n(circular_list):
    n = 43
    target_sublists = []
    for i in range(len(circular_list)):
        remaining_length = len(circular_list)
        product = 1
        for j in range(remaining_length):
            product *= circular_list[(i + j) % len(circular_list)]
            if product == n:
                target_sublists.append(circular_list[i:i + j + 1])
                break
            elif product > n:
                break
    return target_sublists