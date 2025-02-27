def lists_with_product_equal_n(lst):

    def find_sublists(i, product, current_sublist):
        if product == 5:
            result.append(current_sublist[:])
        if i == len(lst) * 2 or product > 5:
            return
        current_sublist.append(lst[i % len(lst)])
        find_sublists(i + 1, product * lst[i % len(lst)], current_sublist)
        current_sublist.pop()
        find_sublists(i + 1, product, current_sublist)
    result = []
    for start in range(len(lst)):
        find_sublists(start, 1, [])
    return result