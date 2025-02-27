def all_neg_ints_exclusive(input_list):
    result = []
    for i, n in enumerate(input_list):
        if n < 0 and 30 < i < 200:
            result.append(n)
    return result