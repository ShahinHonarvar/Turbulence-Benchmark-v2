def lists_with_product_equal_n(circular_list, n):
    """
    Returns a list of sublists each of which contains the contiguous integers from the given
    circular list such that their product equals n. Each sublist in the returned list can be of
    any size as long as it is smaller than or equal to the size of the given list. If no such
    sublist exists, the function returns an empty list. If there are duplicates of such a sublist,
    they should all be contained in the returned list. The order of sublists in the returned list
    does not matter.
    """
    product = 1
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list)):
            product *= circular_list[j % len(circular_list)]
            if product == n:
                sublists.append(circular_list[i:j % len(circular_list) + 1])
            elif product > n:
                break
        product = 1
    return sublists