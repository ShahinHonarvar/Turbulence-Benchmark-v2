def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def check_sublists(start, end):
        product = 1
        sublist = []
        for i in range(start, end):
            product *= circular_list[i % n]
            sublist.append(circular_list[i % n])
            if product == -46:
                result.append(sublist.copy())
            elif product != 0 and abs(product) > 46:
                break
        return sublist
    for i in range(n):
        check_sublists(i, i + n)
    return result