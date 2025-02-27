def lists_with_product_equal_n(lst):
    circular_length = len(lst)
    if circular_length == 0:
        return []

    def _calc_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    result = []
    for i in range(circular_length):
        for j in range(1, min(circular_length, i + 33 // max(lst) + 1)):
            temp_list = lst[i:i + j]
            if len(temp_list) > circular_length:
                temp_list = lst + temp_list[:-circular_length]
            if _calc_product(temp_list) == -33:
                result.append(temp_list)
    return result