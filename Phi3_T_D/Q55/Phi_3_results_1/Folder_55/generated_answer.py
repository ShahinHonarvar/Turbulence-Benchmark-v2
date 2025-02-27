def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        subset = []
        for j in range(i, i + len(circular_list)):
            idx = j % len(circular_list)
            subset.append(circular_list[idx])
            if len(subset) > 1 and (len(subset) == 1 or subset[-1] * subset[-2] != -6):
                break
            elif len(subset) == 2 and subset[0] * subset[1] == -6:
                result.append(subset[:])
    return result