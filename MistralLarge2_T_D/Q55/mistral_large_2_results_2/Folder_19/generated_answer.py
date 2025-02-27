def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []

    def get_sublists(start, length):
        sublist = []
        for i in range(length):
            sublist.append(circular_list[(start + i) % n])
        return sublist
    for length in range(1, n + 1):
        for start in range(n):
            sublist = get_sublists(start, length)
            product = 1
            for num in sublist:
                product *= num
            if product == -54:
                results.append(sublist)
    return results