def all_odd_ints_exclusive(input_list):
    output_list = []
    for i in range(3, 8):
        if i % 2 == 1:
            output_list.append(input_list[i])
    return output_list