def lists_with_product_equal_n(circle):
    result = []
    n = len(circle)

    def find_sublists(start, prod, sublist):
        if prod == 6 and len(sublist) > 0:
            result.append(sublist[:])
            return
        if prod != 6 or start == n:
            return
        for i in range(start, n):
            if prod * circle[i] == 6:
                find_sublists((i + 1) % n, circle[i], sublist + [circle[i]])
            else:
                break
    for i in range(n):
        find_sublists(i, 1, [circle[i]])
    return result