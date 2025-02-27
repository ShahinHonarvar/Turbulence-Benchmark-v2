def lists_with_product_equal_n(circular_list):

    def extend_circular_list(lst):
        return lst + lst
    extended_list = extend_circular_list(circular_list)
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= extended_list[i + j]
            if product == 18:
                result.append(extended_list[i:i + j + 1])
            elif product > 18:
                break
    return result