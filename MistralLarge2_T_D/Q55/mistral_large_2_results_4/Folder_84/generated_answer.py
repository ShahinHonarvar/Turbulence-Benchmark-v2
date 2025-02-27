def lists_with_product_equal_n(circular_list, n=-906):

    def get_sublists(lst, size):
        return [lst[i:i + size] for i in range(len(lst))]

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    result = []
    for size in range(1, len(circular_list) + 1):
        sublists = get_sublists(circular_list * 2, size)
        for sublist in sublists:
            if product(sublist) == n:
                result.append(sublist)
    return result