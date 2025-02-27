def lists_with_product_equal_n(lst):
    n = -23
    sublists = []

    def find_sublists(start_index, current_list, current_product):
        if start_index == len(lst):
            if current_product == n:
                sublists.append(current_list)
            return
        for i in range(start_index, len(lst)):
            find_sublists(i + 1, current_list + [lst[i]], current_product * lst[i])
    find_sublists(0, [], 1)
    return sublists