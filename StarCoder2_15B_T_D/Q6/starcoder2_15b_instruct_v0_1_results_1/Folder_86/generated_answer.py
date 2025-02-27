def all_neg_ints_exclusive(input_list):
    output_list = []
    for i in range(len(input_list)):
        if i >= 18 and i < 60 and (input_list[i] < 0):
            output_list.append(input_list[i])
    return output_list