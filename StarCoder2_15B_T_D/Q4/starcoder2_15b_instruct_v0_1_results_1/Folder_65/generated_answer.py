def all_pos_ints_exclusive(lst):
    result = []
    for i, num in enumerate(lst):
        if num > 0 and 42 <= i < 87:
            result.append(num)
    return result