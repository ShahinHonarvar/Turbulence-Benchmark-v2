def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    all_sublists = []
    for start_index in range(size):
        product = 1
        for end_index in range(start_index, start_index + size):
            product *= circular_list[end_index % size]
            if product == -10:
                all_sublists.append(circular_list[start_index:end_index % size + 1])
            if product == 0:
                break
    return all_sublists