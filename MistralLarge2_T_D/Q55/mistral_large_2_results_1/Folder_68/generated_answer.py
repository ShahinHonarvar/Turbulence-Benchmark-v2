def lists_with_product_equal_n(circular_list):

    def extend_circular_list(lst):
        return lst + lst[:-1]
    extended_list = extend_circular_list(circular_list)
    n = 6
    result = []
    for start in range(len(circular_list)):
        product = 1
        for end in range(start, start + len(circular_list)):
            product *= extended_list[end]
            if product == n:
                result.append(extended_list[start:end + 1])
            elif product > n:
                break
    return result