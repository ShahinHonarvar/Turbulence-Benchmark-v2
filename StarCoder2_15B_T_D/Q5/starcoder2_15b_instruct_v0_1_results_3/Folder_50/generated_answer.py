def all_neg_ints_inclusive(input_list):
    output_list = []
    for i in range(70, 85):
        if input_list[i] < 0:
            output_list.append(input_list[i])
    return output_list