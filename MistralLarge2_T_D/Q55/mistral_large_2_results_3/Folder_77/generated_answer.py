def lists_with_product_equal_n(circ_list):
    n = 632
    size = len(circ_list)
    result = []

    def check_sublist(start, end):
        product = 1
        sublist = []
        for i in range(start, end + 1):
            product *= circ_list[i % size]
            sublist.append(circ_list[i % size])
        if product == n:
            result.append(sublist)
    for i in range(size):
        for j in range(i, i + size):
            check_sublist(i, j)
    return result