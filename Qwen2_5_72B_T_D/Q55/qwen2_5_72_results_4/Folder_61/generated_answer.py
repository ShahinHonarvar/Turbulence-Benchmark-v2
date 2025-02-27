def lists_with_product_equal_n(circular_list):
    sublists = []
    list_length = len(circular_list)
    for start in range(list_length):
        product = 1
        for end in range(start, start + list_length):
            real_end = end % list_length
            product *= circular_list[real_end]
            if product == -10:
                sublists.append(circular_list[start:real_end + 1])
            if product == 0:
                break
    return sublists