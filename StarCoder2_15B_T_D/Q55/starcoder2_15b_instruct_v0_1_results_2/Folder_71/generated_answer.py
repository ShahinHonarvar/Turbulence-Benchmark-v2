from the given list such that their product equals 47.

def lists_with_product_equal_n(circular_list):
    """
    Returns a list of sublists each of which contains the contiguous integers
    """
    sublists = []
    for i in range(len(circular_list)):
        sublist = []
        product = 1
        for j in range(i, i + len(circular_list)):
            index = j % len(circular_list)
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == 47:
                sublists.append(sublist)
                break
            elif product > 47:
                break
    return sublists