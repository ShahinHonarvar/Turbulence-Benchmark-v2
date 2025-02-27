def all_neg_ints_exclusive(input_list):
    output_list = []
    for i, num in enumerate(input_list):
        if num < 0 and 20 <= i < 51:
            output_list.append(num)
    return output_list