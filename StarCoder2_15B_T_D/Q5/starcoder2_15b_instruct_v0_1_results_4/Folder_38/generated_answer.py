def all_neg_ints_inclusive(integers):
    neg_ints = []
    for i, integer in enumerate(integers):
        if integer < 0 and 22 <= i <= 63:
            neg_ints.append(integer)
    return neg_ints