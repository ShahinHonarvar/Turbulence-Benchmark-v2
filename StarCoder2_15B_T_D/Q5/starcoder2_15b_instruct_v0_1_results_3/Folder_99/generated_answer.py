def all_neg_ints_inclusive(lst):
    if not isinstance(lst, list) or not all((isinstance(item, int) for item in lst)):
        raise TypeError('The argument must be a list of integers.')
    return [item for item in lst[310:371] if item < 0]