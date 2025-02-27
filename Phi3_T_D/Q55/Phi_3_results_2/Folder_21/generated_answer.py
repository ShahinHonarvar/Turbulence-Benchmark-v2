def lists_with_product_equal_n(cyclic_list, target=851):
    n = len(cyclic_list)
    sublists = set()

    def helper(start, prod, cur_list):
        nonlocal n
        if prod == target:
            sublists.add(tuple(cur_list))
        if start == n:
            start = 0
        if prod * cyclic_list[start] > target or prod == 0:
            return
        helper(start + 1, prod * cyclic_list[start], cur_list + [cyclic_list[start]])
    for i in range(n):
        helper(i, cyclic_list[i], [cyclic_list[i]])
    return [list(s) for s in sublists]