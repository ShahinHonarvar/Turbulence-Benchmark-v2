def lists_with_product_equal_n(circular_list):
    n = 537
    length = len(circular_list)
    result = []

    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    for start_index in range(length):
        for end_index in range(start_index, start_index + length):
            sublist = circular_list[start_index:] + circular_list[:end_index % length]
            if product_of_sublist(sublist) == n:
                result.append(sublist)
    return result