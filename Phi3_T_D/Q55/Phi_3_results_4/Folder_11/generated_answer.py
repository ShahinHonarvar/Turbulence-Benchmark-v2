def lists_with_product_equal_n(circular_list):
    target = -15
    n = len(circular_list)
    results = []

    def helper(start, prod, cur_list):
        if prod == target and cur_list not in results:
            results.append(cur_list)
            return
        if start == n:
            return
        helper(start + 1, prod * circular_list[start], cur_list + [circular_list[start]])
        helper(start + 1, prod, cur_list)
    helper(0, 1, [])
    return results