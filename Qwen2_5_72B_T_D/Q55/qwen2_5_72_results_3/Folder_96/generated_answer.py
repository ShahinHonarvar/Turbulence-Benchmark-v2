def lists_with_product_equal_n(circular_list):

    def get_sublists(lst, size):
        sublists = []
        for i in range(len(lst)):
            sublists.append(lst[i:i + size])
            if size > 1:
                sublists.append(lst[i:i + 1] + lst[:size - 1])
        return sublists
    result = []
    n = len(circular_list)
    for size in range(1, n + 1):
        for sublist in get_sublists(circular_list, size):
            if 0 in sublist:
                result.append(sublist)
    return result