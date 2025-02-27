def lists_with_product_equal_n(lst, n=-89):

    def circular_sublists(lst):
        sublists = []
        size = len(lst)
        for i in range(size):
            for j in range(i + 1, i + size):
                sublists.append(lst[i:j])
                if j == size:
                    sublists.append(lst[i:] + lst[:j - size])
        return sublists
    sublists = circular_sublists(lst)
    result = []
    for sublist in sublists:
        product = 1
        for num in sublist:
            product *= num
        if product == n:
            result.append(sublist)
    return result