def all_pos_ints_exclusive(my_list):
    if len(my_list) < 98:
        return []
    result = []
    for i in range(69, 97):
        elem = my_list[i]
        if elem > 0:
            result.append(elem)
    return result