def lists_with_product_equal_n(circular_list):

    def product_of_list(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    size = len(circular_list)
    all_sublists = []
    for start in range(size):
        for end in range(1, size + 1):
            sublist = circular_list[start:] + circular_list[:end]
            if len(sublist) <= size and product_of_list(sublist) == -75:
                all_sublists.append(sublist)
    return all_sublists