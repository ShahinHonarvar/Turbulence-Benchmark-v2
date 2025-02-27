def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def check_sublist(start, end):
        product = 1
        sublist = []
        for i in range(start, end):
            product *= circular_list[i % n]
            sublist.append(circular_list[i % n])
            if product == 85:
                result.append(sublist.copy())
            elif product > 85:
                break
        return
    for i in range(n):
        for j in range(i + 1, i + n + 1):
            check_sublist(i, j)
    return result