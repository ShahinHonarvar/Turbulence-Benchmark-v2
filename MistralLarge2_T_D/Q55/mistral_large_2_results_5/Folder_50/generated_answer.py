def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def extend_list(lst, start, end):
        return lst[start:end] + (lst[:end] if end < start else [])
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= circular_list[j % n]
            if product == 45:
                result.append(extend_list(circular_list, i, j % n + 1))
            elif product > 45:
                break
    return result