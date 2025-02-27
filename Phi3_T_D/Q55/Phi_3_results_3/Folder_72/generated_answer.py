def lists_with_product_equal_n(circle):

    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product

    def get_sublists(start, circle, n, seen=set()):
        if start in seen:
            return []
        seen.add(start)
        if product_of_sublist(circle[start:start + len(circle)]) == n:
            return [circle[start:start + len(circle)]]
        sublists = []
        for end in range(start + 1, start + len(circle)):
            sublists += get_sublists(end, circle, n, seen)
        seen.remove(start)
        return sublists
    n = 10
    return get_sublists(0, circle, n)