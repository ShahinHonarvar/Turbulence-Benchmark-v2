def lists_with_product_equal_n(circular_list):

    def has_zero(lst):
        return 0 in lst

    def find_contiguous_sublists(n, lst):

        def product(sublist):
            p = 1
            for num in sublist:
                p *= num
            return p
        sublists = []
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                sublist = lst[i:j + 1] if not has_zero(lst[i:j + 1]) else []
                if product(sublist) == n:
                    sublists.append(sublist)
        return sublists
    result = []
    for _ in range(len(circular_list)):
        sublists = find_contiguous_sublists(-97, circular_list)
        if sublists:
            result.extend(sublists)
            break
        circular_list.append(circular_list.pop(0))
    return result