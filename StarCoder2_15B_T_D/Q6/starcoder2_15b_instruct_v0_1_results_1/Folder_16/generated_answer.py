def all_neg_ints_exclusive(input_list):
    output_list = []
    for i, num in enumerate(input_list):
        if num < 0 and 86 <= i < 90:
            output_list.append(num)
    return output_list