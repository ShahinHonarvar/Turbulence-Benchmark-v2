def all_neg_ints_exclusive(int_list):
    result = []
    for i, num in enumerate(int_list):
        if num < 0 and 64 < i < 80:
            result.append(num)
    return result