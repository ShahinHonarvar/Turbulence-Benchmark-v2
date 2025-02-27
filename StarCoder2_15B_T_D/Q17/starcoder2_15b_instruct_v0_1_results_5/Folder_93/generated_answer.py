def all_ints_div_by_both_two_nums(input_list):
    output_list = []
    for i in range(len(input_list)):
        if i >= 86 and i <= 89 and (input_list[i] % 61 == 0) and (input_list[i] % 79 == 0):
            output_list.append(input_list[i])
    return output_list