def lists_with_product_equal_n(lst):
    n = 247
    result = []

    def find_sublists(lst, curr_prod, curr_sublist):
        if curr_prod == n:
            result.append(curr_sublist)
        for i in range(len(lst)):
            find_sublists(lst[i + 1:], curr_prod * lst[i], curr_sublist + [lst[i]])
    find_sublists(lst, 1, [])
    return result