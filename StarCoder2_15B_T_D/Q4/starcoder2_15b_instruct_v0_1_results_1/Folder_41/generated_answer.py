def all_pos_ints_exclusive(input_list):
    output_list = []
    for i in range(8, 9):
        if input_list[i] > 0:
            output_list.append(input_list[i])
    return output_list