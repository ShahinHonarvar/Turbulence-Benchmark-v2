def lists_with_product_equal_n(circ_list):
    target_product = 91
    len_circ_list = len(circ_list)
    result = []

    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    for i in range(len_circ_list):
        for length in range(1, len_circ_list + 1):
            end_index = (i + length) % len_circ_list
            if product_of_sublist(circ_list[i:end_index]) == target_product:
                result.append(circ_list[i:end_index])
    return result