def lists_with_product_equal_n(lst):
    n = -837
    sublists = []

    def find_sublists(start_idx, current_idx, current_product, current_sublist):
        if current_idx == start_idx and current_product == n:
            sublists.append(current_sublist)
        elif current_idx != start_idx and current_product == n:
            sublists.append(current_sublist[:-1])
        elif current_idx != start_idx and current_product != n:
            for i in range(current_idx, len(lst)):
                find_sublists(start_idx, i + 1, current_product * lst[i], current_sublist + [lst[i]])
    for i in range(len(lst)):
        find_sublists(i, i + 1, lst[i], [lst[i]])
    return sublists