def lists_with_product_equal_n(lst):

    def circular_sublists(lst):
        n = len(lst)
        for i in range(n):
            for j in range(i, i + n):
                yield lst[i:j + 1]
    return [sublist for sublist in circular_sublists(lst) if len(sublist) > 0 and all(sublist) and (eval('*'.join(map(str, sublist))) == 0)]