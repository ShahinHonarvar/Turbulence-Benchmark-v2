def lists_with_product_equal_n(lst):

    def helper(idx, prod, curr_list):
        if idx == 0 and prod == -7:
            res.append(curr_list)
        elif idx < len(lst):
            helper(idx + 1, prod * lst[idx], curr_list + [lst[idx]])
            helper(idx + 1, prod, curr_list)
    res = []
    helper(0, 1, [])
    return res