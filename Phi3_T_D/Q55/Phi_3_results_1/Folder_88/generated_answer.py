def lists_with_product_equal_n(circular_list):
    product_target = -56
    num_elements = len(circular_list)
    sublists = []
    for start in range(num_elements):
        product = 1
        sublist = []
        for end in range(start, start + num_elements):
            element = circular_list[end % num_elements]
            product *= element
            sublist.append(element)
            if product == product_target:
                sublists.append(list(sublist))
            if product > abs(product_target):
                break
    return sublists