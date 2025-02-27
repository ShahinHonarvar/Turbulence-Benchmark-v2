def all_pos_ints_inclusive(input_list):
    if len(input_list) < 93:
        return []
    output_list = []
    for i in range(62, 93):
        if input_list[i] > 0:
            output_list.append(input_list[i])
    return output_list