def lists_with_product_equal_n(circular_list):

    def extend_circular_list(lst, n):
        return lst * 2
    extended_list = extend_circular_list(circular_list, len(circular_list))
    result = []
    for i in range(len(extended_list)):
        product = 1
        for j in range(len(extended_list)):
            product *= extended_list[(i + j) % len(extended_list)]
            if product == 2:
                result.append(extended_list[i:i + j + 1])
            elif product > 2:
                break
    return result