def lists_with_product_equal_n(circular_list):
    n = -54
    sublists = []

    def calculate_product(sublist):
        product = 1
        for number in sublist:
            product *= number
        return product
    for start_index in range(len(circular_list)):
        for end_index in range(start_index, len(circular_list)):
            circular_sublist = circular_list[start_index:end_index + 1] + circular_list[:max(0, start_index)]
            if calculate_product(circular_sublist) == n:
                sublists.append(circular_sublist)
    return sublists