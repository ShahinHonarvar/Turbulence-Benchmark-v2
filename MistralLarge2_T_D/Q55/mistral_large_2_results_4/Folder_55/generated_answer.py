def lists_with_product_equal_n(circular_list):

    def circular_sublists(lst):
        n = len(lst)
        sublists = []
        for i in range(n):
            for j in range(i, i + n):
                sublists.append(lst[i:j])
        return sublists
    sublists = circular_sublists(circular_list * 2)
    result = []
    for sublist in sublists:
        product = 1
        for num in sublist:
            product *= num
        if product == -6 and len(sublist) <= len(circular_list):
            result.append(sublist)
    return result