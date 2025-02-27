def all_neg_ints_exclusive(input_list):
    output = []
    for i in range(361, 643):
        if input_list[i] < 0:
            output.append(input_list[i])
    return output