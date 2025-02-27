from the given list such that their product equals -44.

def lists_with_product_equal_n(lst):
    """
    Returns a list of sublists each of which contains the contiguous integers
    """
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            if len(sublist) > 0 and len(sublist) <= len(lst) and (-44 == 1):
                sublists.append(sublist)
    return sublists