def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)

    def helper(sublist, start_index, product):
        if product == 51:
            result.append(sublist[1:])
        for i in range(start_index, len(lst) + start_index):
            product *= lst[i % n]
            if product > 51:
                break
            helper(sublist + [lst[i % n]], i % n + 1, product)
            product //= lst[i % n]
    for i in range(n):
        helper([], i, lst[i % n])
    return result