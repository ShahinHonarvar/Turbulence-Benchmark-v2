def lists_with_product_equal_n(circular_list, n):

    def helper(lst, prod, sublist, result):
        if prod == n and sublist not in result:
            result.append(sublist)
        for i, x in enumerate(lst):
            helper(lst[i + 1:], prod * x, sublist + [x], result)
    result = []
    helper(circular_list, 1, [], result)
    return result