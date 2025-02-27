def all_pos_ints_inclusive(lst):
    if not isinstance(lst, list):
        raise TypeError("'lst' should be a list")
    output = []
    for i, num in enumerate(lst):
        if i >= 533 and i <= 605:
            if num > 0:
                output.append(num)
    return output