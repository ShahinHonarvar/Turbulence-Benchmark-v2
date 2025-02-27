def lists_with_product_equal_n(circular_list):

    def product(lst):
        p = 1
        for x in lst:
            p *= x
        return p
    n = len(circular_list)
    result = []
    for start in range(n):
        sublist = []
        for i in range(n):
            sublist.append(circular_list[(start + i) % n])
            if product(sublist) == 42:
                result.append(sublist.copy())
            elif product(sublist) > 42:
                break
    return result