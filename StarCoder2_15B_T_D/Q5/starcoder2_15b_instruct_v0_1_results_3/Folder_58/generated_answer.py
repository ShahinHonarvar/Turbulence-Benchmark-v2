def all_neg_ints_inclusive(input_list):
    result = []
    for i in range(209, 557):
        if input_list[i] < 0:
            result.append(input_list[i])
    return result