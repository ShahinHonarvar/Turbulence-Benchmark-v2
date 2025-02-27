def lists_with_product_equal_n(lst):

    def helper(sub_lst, i, index, result):
        if len(sub_lst) != 0 and sub_lst[0] == sub_lst[-1]:
            product = 1
            for num in sub_lst:
                product *= num
            if product == target:
                result.append(sub_lst[:])
            return
        if index >= len(lst):
            return
        helper(sub_lst, i, index + 1, result)
        helper(sub_lst + [lst[index]], i + 1, index + 1, result)
    target = -1
    halves = len(lst) // 2
    found = []
    helper([], 0, 0, found)
    results = []
    for i in range(halves):
        found_sublists = []
        helper([], i, i, found_sublists)
        for sublist in found_sublists:
            rotated = sublist[1:] + sublist[:1]
            if rotated not in results and rotated in found_sublists:
                results.append(rotated)
                found_sublists.remove(sublist)
        found = found_sublists
    return results