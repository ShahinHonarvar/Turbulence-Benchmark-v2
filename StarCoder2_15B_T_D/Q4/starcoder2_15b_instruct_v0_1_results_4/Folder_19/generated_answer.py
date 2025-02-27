def all_pos_ints_exclusive(ints_list):
    positive_ints = []
    for i, num in enumerate(ints_list):
        if num > 0 and 2 <= i < 5:
            positive_ints.append(num)
    return positive_ints