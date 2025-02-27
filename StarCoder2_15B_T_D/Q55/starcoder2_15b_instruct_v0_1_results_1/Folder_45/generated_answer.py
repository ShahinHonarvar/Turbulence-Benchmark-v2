def lists_with_product_equal_n(lst):
    """
    Finds all sublists of lst whose product is equal to -5.
    """
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = lst[i:j + 1]
            if len(sublist) <= len(lst) and prod(sublist) == -5:
                result.append(sublist)
    return result

def prod(lst):
    """
    Returns the product of all elements in lst.
    """
    p = 1
    for x in lst:
        p *= x
    return p