def all_pos_ints_inclusive(int_list):
    result = []
    for int in int_list[31:35]:
        if int > 0:
            result.append(int)
    return result