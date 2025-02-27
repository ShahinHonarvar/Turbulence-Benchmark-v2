def lists_with_product_equal_n(lst):
    result = []

    def find_sublists(sublist, product, index):
        if product == -51:
            result.append(sublist)
        elif product != -51 and index < len(lst):
            find_sublists(sublist + [lst[index]], product * lst[index], index + 1)
            find_sublists(sublist, product, index + 1)
    find_sublists([], 1, 0)
    return result