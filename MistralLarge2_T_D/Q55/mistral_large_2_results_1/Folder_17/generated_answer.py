def lists_with_product_equal_n(circular_list):

    def circular_sublists(lst):
        sublists = []
        n = len(lst)
        for i in range(n):
            for j in range(1, n + 1):
                sublists.append(lst[i:i + j])
        return sublists
    sublists = circular_sublists(circular_list)
    return [sublist for sublist in sublists if sublist and eval('*'.join(map(str, sublist))) == 18]