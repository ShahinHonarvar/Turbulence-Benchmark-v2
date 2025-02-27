def all_pos_ints_inclusive(input_list):
    output_list = []
    for i, num in enumerate(input_list):
        if num > 0 and 31 <= i <= 34:
            output_list.append(num)
    return output_list