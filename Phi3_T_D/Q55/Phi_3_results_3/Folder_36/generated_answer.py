def lists_with_product_equal_n(circular_list, n=714):

    def product(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod
    max_len = len(circular_list)
    found_sublists = []
    for length in range(1, max_len + 1):
        for start_index in range(max_len):
            sublist = circular_list[start_index:] + circular_list[:start_index]
            sliced_sublist = sublist[:length]
            if product(sliced_sublist) == n:
                found_sublists.append(sliced_sublist)
    return found_sublists