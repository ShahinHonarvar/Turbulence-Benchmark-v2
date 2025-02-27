def lists_with_product_equal_n(lst):
    """
    Returns a list of sublists each of which contains the contiguous integers from the given list
    such that their product equals -10.
    """
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -10:
                result.append(sublist)
    return result