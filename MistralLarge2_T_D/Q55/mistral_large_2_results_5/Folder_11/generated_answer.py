def lists_with_product_equal_n(circular_list):

    def get_sublists(lst):
        n = len(lst)
        sublists = []
        for i in range(n):
            for j in range(i + 1, n + 1):
                sublists.append(lst[i:j])
                sublists.append(lst[i:] + lst[:j])
        return sublists
    sublists = get_sublists(circular_list)
    result = [sublist for sublist in sublists if len(sublist) > 0 and eval('*'.join(map(str, sublist))) == -15]
    return result