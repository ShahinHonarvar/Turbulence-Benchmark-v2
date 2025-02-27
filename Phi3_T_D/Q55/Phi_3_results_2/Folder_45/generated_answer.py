def lists_with_product_equal_n(circular_list):
    if not circular_list:
        return []

    def find_sublists(start_idx, prod, sublist):
        idx = (start_idx + len(sublist)) % len(circular_list)
        if prod == -5 or idx == start_idx:
            if prod == -5:
                return [sublist]
            return []
        sublists = find_sublists(idx, prod * circular_list[idx], sublist + [circular_list[idx]])
        return sublists + find_sublists(idx, prod, sublist)
    result = []
    for i in range(len(circular_list)):
        result += find_sublists(i, 1, [circular_list[i]])
    return result