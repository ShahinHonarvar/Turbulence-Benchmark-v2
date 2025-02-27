def all_pos_ints_exclusive(lst):
    all_pos_ints = [num for num in lst if num > 0]
    if not all_pos_ints:
        return []
    return all_pos_ints[:5]