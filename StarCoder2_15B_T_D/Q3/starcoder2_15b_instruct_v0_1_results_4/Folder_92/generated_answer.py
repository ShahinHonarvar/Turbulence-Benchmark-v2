def all_pos_ints_inclusive(integers):
    result = []
    for i, integer in enumerate(integers):
        if integer > 0 and (i == 0 or i == 1):
            result.append(integer)
    return result