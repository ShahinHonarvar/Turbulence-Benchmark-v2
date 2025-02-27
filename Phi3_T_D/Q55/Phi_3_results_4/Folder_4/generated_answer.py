def lists_with_product_equal_n(circular_list):
    n = 91
    results = []
    sublist_size = len(circular_list)

    def find_sublists(index, current_product, current_sublist, used_indices):
        if current_product == n:
            results.append(current_sublist)
        for i in range(max(index, 0), sublist_size):
            if i not in used_indices:
                next_index = (index + 1) % sublist_size
                find_sublists(next_index, current_product * circular_list[i], current_sublist + [circular_list[i]], used_indices + [i])
    find_sublists(0, 1, [], [])
    return results