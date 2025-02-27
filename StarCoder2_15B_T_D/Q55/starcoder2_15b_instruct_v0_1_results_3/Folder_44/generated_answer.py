def lists_with_product_equal_n(lst, n):
    result = []

    def helper(current_list, current_product, index):
        if current_product == n:
            result.append(current_list)
        if index >= len(lst):
            return
        helper(current_list + [lst[index]], current_product * lst[index], index + 1)
        helper(current_list, current_product, index + 1)
    helper([], 1, 0)
    return result