def all_neg_ints_exclusive(ints):
    negatives = []
    for current_int in ints[18:60]:
        if current_int < 0:
            negatives.append(current_int)
    return negatives