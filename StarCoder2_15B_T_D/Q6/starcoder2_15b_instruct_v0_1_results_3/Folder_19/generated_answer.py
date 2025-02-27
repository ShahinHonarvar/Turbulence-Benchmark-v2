def all_neg_ints_exclusive(lst):
    output = []
    for i, num in enumerate(lst):
        if num < 0 and 2 <= i < 5:
            output.append(num)
    return output