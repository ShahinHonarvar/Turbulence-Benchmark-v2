def lists_with_product_equal_n(circular_list):

    def circular_sublists(lst):
        n = len(lst)
        sublists = []
        for i in range(n):
            for j in range(1, n + 1):
                sublists.append(lst[i:i + j])
        return sublists
    sublists = circular_sublists(circular_list)
    result = []
    for sublist in sublists:
        product = 1
        for num in sublist:
            product *= num
        if product == -97:
            result.append(sublist)
    return result