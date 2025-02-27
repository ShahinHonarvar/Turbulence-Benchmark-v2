def lists_with_product_equal_n(circular_list):
    n = -51
    total_len = len(circular_list)
    found_sublists = []
    for start in range(total_len):
        temp_product = 1
        for end in range(start, start + total_len):
            temp_product *= circular_list[end % total_len]
            if temp_product == n:
                found_sublists.append(circular_list[start:end + 1])
            if temp_product == 0 or circular_list[end % total_len] == 0:
                break
    return found_sublists