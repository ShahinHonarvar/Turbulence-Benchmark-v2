def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target_product = 714
    result = []

    def find_sublists(start, prod, sublist):
        if prod == target_product:
            result.append(sublist)
            return
        if prod != 0 and prod % target_product == 0 and (target_product % prod != 0):
            return
        for i in range(n):
            new_start = (start + i) % n
            new_prod = prod * circular_list[new_start]
            find_sublists(new_start + 1, new_prod, sublist + [circular_list[new_start]])
    for i in range(n):
        find_sublists(i, 1, [])
    return result