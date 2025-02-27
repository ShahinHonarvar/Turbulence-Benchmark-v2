def find_smallest_num(lst):
    if len(lst) < 78:
        raise ValueError('List must contain at least 78 elements.')
    return min(lst[66:78])