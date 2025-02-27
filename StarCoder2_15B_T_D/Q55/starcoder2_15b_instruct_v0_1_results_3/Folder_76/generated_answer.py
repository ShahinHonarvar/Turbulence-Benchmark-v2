def lists_with_product_equal_n(lst):

    def sublists_with_product(lst, target, curr_prod=1, curr_sublist=[]):
        if curr_prod == target:
            yield curr_sublist
        for i, num in enumerate(lst):
            if curr_prod * num > target:
                continue
            yield from sublists_with_product(lst[i + 1:], target, curr_prod * num, curr_sublist + [num])
    lst_size = len(lst)
    return [sublist for sublist in sublists_with_product(lst + lst, 247) if len(sublist) <= lst_size]