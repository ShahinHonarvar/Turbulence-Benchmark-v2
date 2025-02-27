def lists_with_product_equal_n(circular_list):

    def find_sublists(start, n):
        product = 1
        sublist = []
        for i in range(n):
            idx = (start + i) % n
            product *= circular_list[idx]
            sublist.append(circular_list[idx])
            if product == -26:
                result.append(sublist[:])
            if product == 0:
                break
        return
    result = []
    n = len(circular_list)
    for i in range(n):
        find_sublists(i, n)
    return result