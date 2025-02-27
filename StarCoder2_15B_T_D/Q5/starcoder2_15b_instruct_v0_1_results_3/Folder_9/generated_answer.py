def all_neg_ints_inclusive(lst):
    output = []
    for i, num in enumerate(lst):
        if num < 0 and 70 <= i <= 200:
            output.append(num)
    return output