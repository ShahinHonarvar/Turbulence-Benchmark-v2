def lists_with_product_equal_n(lst):

    def find_sublists(start, product):
        sublists, index = ([], start)
        while True:
            product *= lst[index]
            if product == -26:
                sublists.append(lst[start:index + 1])
            index = (index + 1) % n
            if index == start:
                break
        return sublists
    n, result = (len(lst), [])
    for i in range(n):
        result.extend(find_sublists(i, 1))
    return result