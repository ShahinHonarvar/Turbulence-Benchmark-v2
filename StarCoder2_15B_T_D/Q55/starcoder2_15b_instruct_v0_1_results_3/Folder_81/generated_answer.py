def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []

    def find_sublists(i, prod, sublist):
        if prod == -8:
            result.append(sublist)
        else:
            for j in range(i + 1, i + n):
                find_sublists(j % n, prod * lst[j % n], sublist + [lst[j % n]])
    for i in range(n):
        find_sublists(i, lst[i], [lst[i]])
    return result