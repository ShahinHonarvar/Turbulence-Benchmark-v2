def lists_with_product_equal_n(circular_list):

    def product(sublist):
        p = 1
        for num in sublist:
            p *= num
        return p
    n = len(circular_list)
    found_sublists = []
    for start in range(n):
        for end in range(start, n + start):
            sublist = circular_list[start:end % n]
            if product(sublist) == 48:
                found_sublists.append(sublist)
    return found_sublists