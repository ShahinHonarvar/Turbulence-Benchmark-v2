def lists_with_product_equal_n(circular_list):

    def is_product_of_sublist(sublist, n):
        product = 1
        for num in sublist:
            product *= num
            if product == n:
                return True
        return False
    n = 415
    result = []
    list_size = len(circular_list)
    for start in range(list_size):
        for end in range(start, list_size):
            sublist = circular_list[start:end] + circular_list[:start:end - start + 1]
            if is_product_of_sublist(sublist, n):
                result.append(sublist)
    return result