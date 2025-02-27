def lists_with_product_equal_n(lst, n):

    def find_sublists(lst, product, sublist, i):
        if i == len(lst):
            if product == n:
                results.append(sublist)
            return
        find_sublists(lst, product * lst[i], sublist + [lst[i]], i + 1)
        find_sublists(lst, product, sublist, i + 1)
    results = []
    find_sublists(lst, 1, [], 0)
    return results