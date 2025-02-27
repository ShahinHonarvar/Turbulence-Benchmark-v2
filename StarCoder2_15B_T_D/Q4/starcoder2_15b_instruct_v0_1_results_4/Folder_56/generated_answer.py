def all_pos_ints_exclusive(my_list):
    pos_ints = [num for num in my_list if num > 0]
    if len(pos_ints) < 9:
        return []
    else:
        return pos_ints[7:9]