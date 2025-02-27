def lists_with_product_equal_n(lst):

    def get_sublists_with_product(lst, target_product, start_index):
        if target_product == 1 or len(lst) == 0:
            return []
        result = []
        current_product = 1
        current_sublist = []
        for i, num in enumerate(lst):
            current_product *= num
            current_sublist.append(num)
            if current_product == target_product:
                result.append(current_sublist[:])
            if current_product > target_product:
                return get_sublists_with_product(lst[i - len(current_sublist) + 1:], target_product, start_index + i - len(current_sublist) + 1)
        return result
    result = []
    for i in range(len(lst)):
        result += get_sublists_with_product(lst[i:] + lst[:i], 90, i)
    return result