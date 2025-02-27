def find_second_largest_num(lst):
    """
    Finds the second largest element in the list 'lst' between indices 62 and 78, inclusive.
    If there is no such element, returns 'None'.
    """
    lst = lst[62:79]
    lst = sorted(lst, reverse=True)
    if len(lst) < 2:
        return None
    return lst[-2]