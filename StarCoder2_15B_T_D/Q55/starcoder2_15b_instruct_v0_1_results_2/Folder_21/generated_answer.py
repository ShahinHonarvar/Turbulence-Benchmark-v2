def lists_with_product_equal_n(lst, n):
    """
    Returns a list of sublists each of which contains the contiguous integers from the given list such that their product equals n. Each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list. If no such sublist exists, the function returns an empty list. If there are duplicates of such a sublist, they should all be contained in the returned list. The order of sublists in the returned list does not matter.
    """
    sublists = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = lst[i:j + 1]
            if len(sublist) <= len(lst) and product(sublist) == n:
                sublists.append(sublist)
    return sublists

def product(lst):
    """Returns the product of the elements in the given list."""
    return 1 if not lst else lst[0] * product(lst[1:])