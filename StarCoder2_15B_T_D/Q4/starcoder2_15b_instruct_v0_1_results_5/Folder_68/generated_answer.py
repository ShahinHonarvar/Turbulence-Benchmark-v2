def all_pos_ints_exclusive(input_list):
    output_list = []
    for i in range(len(input_list)):
        if i >= 0 and i < 8 and (input_list[i] > 0):
            output_list.append(input_list[i])
    return output_list