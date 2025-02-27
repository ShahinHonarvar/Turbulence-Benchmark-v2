def all_neg_ints_exclusive(ints):
    result = [x for x in ints if x < 0]
    if len(result) > 0:
        return result[:8]
    else:
        return []