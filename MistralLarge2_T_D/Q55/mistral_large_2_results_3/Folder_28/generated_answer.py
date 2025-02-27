def lists_with_product_equal_n(circular_list):
    n = 85
    length = len(circular_list)
    results = []

    def product(lst):
        p = 1
        for x in lst:
            p *= x
        return p
    for i in range(length):
        for j in range(i, i + length):
            sublist = [circular_list[k % length] for k in range(i, j + 1)]
            if product(sublist) == n:
                results.append(sublist)
    return results