def all_pos_ints_inclusive(my_list):
    filtered_list = filter(lambda x: x > 0, my_list)
    result = [x for i, x in enumerate(filtered_list) if 13 <= i <= 68]
    return result