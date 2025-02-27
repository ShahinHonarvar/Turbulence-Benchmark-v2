def lists_with_product_equal_n(circular_list):

    def get_product(sublist):
        product = 1
        for item in sublist:
            product *= item
        return product
    size = len(circular_list)
    found_sublists = []
    for i in range(size):
        for j in range(i, size + i):
            current_slice = circular_list[i:j % size]
            if get_product(current_slice) == 36:
                found_sublists.append(current_slice)
    return found_sublists