def lists_with_product_equal_n(circular_list):
    """
    Returns a list of sublists of contiguous integers from circular_list whose product equals 46.
    Each sublist can be of any size as long as it is smaller than or equal to the size of circular_list.
    If no such sublist exists, returns an empty list.
    If there are duplicates, they should all be contained in the returned list.
    The order of sublists in the returned list does not matter.
    """
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1):
            sublist = circular_list[i:j]
            if len(sublist) <= len(circular_list) and prod(sublist) == 46:
                sublists.append(sublist)
    return sublists

def prod(lst):
    """Returns the product of all elements in lst."""
    p = 1
    for x in lst:
        p *= x
    return p