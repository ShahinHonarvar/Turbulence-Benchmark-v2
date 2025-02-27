def lists_with_product_equal_n(lst):

    def find_sublists(start, end, product, current):
        if product == 851:
            result.append(current[:])
            return
        if product > 851 or end == start:
            return
        find_sublists(start, (end + 1) % len(lst), product // lst[end], current + [lst[end]])
        find_sublists((start + 1) % len(lst), end, product, current)
    result = []
    for i in range(len(lst)):
        find_sublists(i, i, lst[i], [lst[i]])
    return result