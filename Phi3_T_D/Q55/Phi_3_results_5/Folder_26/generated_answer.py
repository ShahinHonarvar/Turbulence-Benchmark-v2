def lists_with_product_equal_n(circular_list):
    n = 93
    min_len = 2
    found_sublists = []
    for i in range(len(circular_list)):
        for sub_len in range(min_len, len(circular_list) + 1):
            product = 1
            for j in range(i, i + sub_len):
                product *= circular_list[j % len(circular_list)]
            if product == n:
                found_sublists.append(circular_list[i:i + sub_len])
    return found_sublists