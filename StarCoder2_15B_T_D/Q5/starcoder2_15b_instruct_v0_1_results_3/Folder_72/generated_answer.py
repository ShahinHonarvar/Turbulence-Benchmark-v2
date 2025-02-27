def all_neg_ints_inclusive(num_list):
    result = []
    for num in num_list[29:52]:
        if num < 0:
            result.append(num)
    return result