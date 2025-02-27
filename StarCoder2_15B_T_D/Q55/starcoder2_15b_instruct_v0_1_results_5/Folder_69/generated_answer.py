def lists_with_product_equal_n(lst):
    n = 90
    result = []

    def find_sublists(current_list, current_product, start_index):
        if current_product == n:
            result.append(current_list)
        for i in range(start_index, len(lst)):
            find_sublists(current_list + [lst[i]], current_product * lst[i], i + 1)
    find_sublists([], 1, 0)
    return result