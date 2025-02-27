def lists_with_product_equal_n(circular_list):

    def extend_list(lst, n):
        return lst * n
    n = len(circular_list)
    extended_list = extend_list(circular_list, 2)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= extended_list[j]
            if product == 48:
                result.append(extended_list[i:j + 1])
            elif product > 48:
                break
    return result