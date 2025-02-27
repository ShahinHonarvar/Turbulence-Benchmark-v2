def lists_with_product_equal_n(lst):
    product_target = -72
    result = []

    def find_sublists(sublst, prodd, start_idx):
        if prodd == product_target:
            if sublst not in result:
                result.append(sublst)
            return
        for i in range(start_idx, len(lst)):
            new_prodd = prodd * lst[i]
            find_sublists(sublst + [lst[i]], new_prodd, (i + 1) % len(lst))
    for i in range(len(lst)):
        find_sublists([lst[i]], lst[i], (i + 1) % len(lst))
    return result