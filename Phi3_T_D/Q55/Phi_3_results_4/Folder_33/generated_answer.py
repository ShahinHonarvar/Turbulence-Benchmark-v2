def lists_with_product_equal_n(circular_list):
    n = -115
    sublists_with_n = []
    for i, val in enumerate(circular_list):
        prod = val
        sublist = [val]
        j = (i + 1) % len(circular_list)
        while prod * circular_list[j] == n and prod != n:
            prod *= circular_list[j]
            sublist.append(circular_list[j])
            j = (j + 1) % len(circular_list)
        if prod == n and len(sublist) <= len(circular_list):
            sublists_with_n.append(sublist)
    return sublists_with_n