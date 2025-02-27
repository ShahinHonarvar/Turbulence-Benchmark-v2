def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def check_sublists(start, end):
        product = 1
        sublist = []
        for i in range(start, end):
            product *= circular_list[i % n]
            sublist.append(circular_list[i % n])
            if product == 74:
                result.append(sublist[:])
            elif product > 74:
                break
    for i in range(n):
        for j in range(i + 1, i + n + 1):
            check_sublists(i, j)
    return result